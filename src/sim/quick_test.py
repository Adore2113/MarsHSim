from src.sim.state import Habitat_State
from src.sim.engine import step, gas_alert, mca
from src.sim.crew_metabolism import crew_metabolism

s0 = Habitat_State(
# ---time---
    mission_time_s = 0,
    
# ---lights---
    light_level = 0.0,

# ----crew----
    crew_count = 30,
    crew_activity = "normal",
  

    hab_vol_m3 = 2000.0,
    hab_temp_c = 23,

# ----atmosphere----
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
        {"id": 1, "status": "standby", "capacity": 3.0, "co2_load": 0.0},
        {"id": 2, "status": "standby", "capacity": 3.0, "co2_load": 0.0},
        {"id": 3, "status": "standby", "capacity": 3.0, "co2_load": 0.0},
        {"id": 4, "status": "standby", "capacity": 3.0, "co2_load": 0.0}
    ],
    scrub_per_bed_kpa = 0.0035,

    water_for_oga_kg = 1000.0, # placeholder name and amount

# ----power----
    battery_max_capacity_kwh = 4000.0,
    battery_stored_kwh = 4000.0,    # starting with max capacity, for now
    
    solar_arrays = [
        {"id": 1, "status": "online", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0},
        {"id": 2, "status": "online", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0},
        {"id": 3, "status": "online", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0},
        {"id": 4, "status": "online", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0},
        {"id": 5, "status": "online", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0},
        {"id": 6, "status": "online", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0},
        {"id": 7, "status": "online", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0},
        {"id": 8, "status": "online", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0},
        {"id": 9, "status": "standby",  "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0},
        {"id": 10,"status": "standby",  "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0}
    ], 

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

    
def print_state(state, outputs, alerts):
    hour, minutes, meridiem = sol_time(state.mission_time_s)
    
    print(f"Sol: n/a | {hour}:{minutes:02d} {meridiem} LMST")
    print(f"Light level: {state.light_level:.2f}")
    print(f"Oxygen: {state.o2_kpa} kPa")
    print(f"Hydrogen stored: {state.h2_stored_kg:.4f} kg")
    print(f"Carbon Dioxide Scrubbed: {outputs["co2_removed_kpa"]:.4f} kPa")
    print(f"Carbon Dioxide: {state.co2_kpa} kPa")
    
    if alerts:
        print(f"Alert: {alerts}")
    print(f"Nitrogen: {state.n2_kpa} kPa")
    print(f"Argon: {state.ar_kpa} kPa")
    print(f"Total Pressure: {mca(state.o2_kpa, state.co2_kpa, state.n2_kpa, state.ar_kpa):.4f} kPa")
    print(f"Water remaining: {state.water_for_oga_kg} kg")
    
    print(f"Scrubber power used: {outputs["co2_scrubber_power_used_kw"]:.4f} kW")
    print(f"Scrubber heat: {outputs["co2_scrubber_heat_kw"]:.4f} kW")
    print(f"Scrubber energy: {outputs["co2_scrubber_energy_used_kwh"]:.4f} kWh")
    print(f"OGA heat: {outputs["oga_heat_kw"]:.4f} kW")
    print(f"Lights power: {outputs["light_power_kw"]:.4f} kW")

    print()


state = s0
for i in range(12):
    state, outputs = step(state)
    alerts = gas_alert(state)
    print_state(state, outputs, alerts)