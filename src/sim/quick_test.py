from src.sim.state import Habitat_State
from src.sim.engine import step, gas_alert, mca

s0 = Habitat_State(
    # time
    mission_time_s = 0,
    
    # lights
    light_level = 0.0,

    # crew
    crew_count = 30,

    #later these will be handled properly for schedules and some random events
    crew_activity = "normal",
   # crew_activity = "sleep",
    #crew_activity = "exercise",
    #crew_activity = "intense",

    hab_vol_m3 = 2000.0,
    hab_temp_c = 23,

    # atmosphere
    target_pressure_kpa = 60.0,
    min_safe_pressure_kpa = 55.0,
    max_safe_pressure_kpa = 70.0,

    target_o2_kpa = 20.0,
    target_co2_kpa = 0.4,
    target_n2_kpa = 17.0,
    target_ar_kpa = 22.6,

    o2_kpa = 20.0,
    co2_kpa = 0.4,
    n2_kpa = 18.0,
    ar_kpa = 21.6, 

    n2_stored_kpa = 60.0,   # ~1365 kg
    ar_stored_kpa = 30.0,   # ~973.5 kg
    co2_stored_kpa = 0.0,   # temporarily putting the co2 that the scrubber removes to here
    h2_stored_kg = 0.0,  
 
    amine_beds = [
        {"status": "online", "capacity": 3.0, "co2_load": 0.0},
        {"status": "regenerating", "capacity": 3.0, "co2_load": 1.0},
        {"status": "standby", "capacity": 3.0, "co2_load": 0.0},
        {"status": "standby", "capacity": 3.0, "co2_load": 0.0}
    ],
    scrub_per_bed_kpa = 0.0035,

    water_for_oga_kg = 1000.0, # placeholder name and amount

    battery_max_capacity_kwh = 4000.0,
    battery_stored_kwh = 4000.0,    # starting with max capacity, for now
    solar_capacity_kw = 120.0,    # placeholder value until I do more research
    solar_efficiency = 0.8,    # starting with 80% efficiency to start, for now

    #from here down these are placeholders
    relative_humidity = 40.0,

    potable_water_l = 5000.0,
    grey_water_l = 0.0,
    waste_brine_l = 0.0,

    leak_rate_kpa_per_hr = 0.0,
    smoke_ppm = 0.0,
    radiation_msv_per_day = 0.7
)


def sol_time(seconds):
    # one mars sol is 24h 39min 35sec
    total_sol_seconds = 88775
    sol_seconds = seconds % total_sol_seconds

    hour_24 = sol_seconds // 3600
    # 1h = 60min, 1min = 60 sec, 60*60 = 3600
    minutes = (sol_seconds % 3600) // 60
    
    meridiem = "AM"
    hour_12 = hour_24

    if hour_24 >= 12:
        meridiem = "PM"
    if hour_24 > 12:
        hour_12 = hour_24 - 12
    if hour_24 == 0:
        hour_12 = 12

    return hour_12, minutes, meridiem

    
def print_state(state, scrubbed_amount, alerts):
    hour, minutes, meridiem = sol_time(state.mission_time_s)
    print(f"Sol: n/a | {hour}:{minutes:02d} {meridiem} LMST")
    print(f"Light level: {state.light_level}")
    print(f"Oxygen: {state.o2_kpa}")
    print(f"Hydrogen stored: {state.h2_stored_kg}")
    print(f"Carbon Dioxide Scrubbed: {scrubbed_amount:.4f}")
    print(f"Carbon Dioxide: {state.co2_kpa}")
    if alerts:
        print(f"Alert: {alerts}")
    print(f"Nitrogen: {state.n2_kpa}")
    print(f"Argon: {state.ar_kpa}")
    print(f"Total Pressure: {mca(state)}")
    print(f"Water remaining: {state.water_for_oga_kg}")
    print()


state = s0
for i in range(12):
    state, scrubbed_amount = step(state)
    alerts = gas_alert(state)
    print_state(state, scrubbed_amount, alerts)