from src.sim.state import Habitat_State
from src.sim.engine import step
from src.sim.mars_time import get_sol_time
from .buffer_gas_system import mca
from .alerts import gas_alerts, get_status

s0 = Habitat_State(
# ------time----------------------------------------♡
    mission_time_s = 0,
    
# ------lights--------------------------------------♡
    light_level = 0.0,

# ------crew----------------------------------------♡
    crew_count = 30,
    crew_activity = "normal",
  
# ------habitat-------------------------------------♡
    hab_vol_m3 = 2000.0,
    hab_temp_c = 23.0,
    insulation_strength_kw_per_c = 1.0,

# ------atmosphere targets and limits---------------♡ 
    target_pressure_kpa = 60.0,
    min_safe_pressure_kpa = 55.0,
    max_safe_pressure_kpa = 70.0,

    target_o2_kpa = 20.0,
    target_co2_kpa = 0.4,
    target_n2_kpa = 17.0,
    target_ar_kpa = 22.6,

# ------current atmosphere--------------------------♡
    o2_kpa = 20.0,
    co2_kpa = 0.4,
    n2_kpa = 18.0,
    ar_kpa = 21.6, 

# ------gas storage---------------------------------♡
    n2_stored_kpa = 60.0,   # ~1365 kg
    ar_stored_kpa = 30.0,   # ~973.5 kg
    co2_stored_kpa = 0.0,   # temporarily putting the co2 that the scrubber removes to here
    h2_stored_kg = 0.0,  

# ------OGA water-----------------------------------♡
    water_for_oga_kg = 1200.0, # placeholder name and amount

# ------amine beds----------------------------------♡
    amine_beds = [
        {"id" : 1, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0},
        {"id" : 2, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0},
        {"id" : 3, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0},
        {"id" : 4, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0}
    ],
    scrub_per_bed_kpa = 0.0035,

# ------power---------------------------------------♡
    battery_max_capacity_kwh = 4000.0,
    battery_stored_kwh = 3800.0,    # starting with max capacity, for now
    
    solar_arrays = [
        {"id" : 1, "status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0},
        {"id" : 2, "status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0},
        {"id" : 3, "status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0},
        {"id" : 4, "status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0},
        {"id" : 5, "status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0},
        {"id" : 6, "status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0},
        {"id" : 7, "status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0},
        {"id" : 8, "status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0},
        {"id" : 9, "status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0},
        {"id" : 10,"status" : "standby", "area_m2" : 50, "efficiency" : 0.28, "dust_factor" : 1.0}
    ], 
    
    daylight_m2_kw = 0.0,
    peak_sunlight_today = 0.0,
    low_sunlight_streak_sols = 0,

# ------placeholders for future plans---------------♡
    relative_humidity = 45.0,

    potable_water_l = 5000.0,
    grey_water_l = 0.0,
    waste_brine_l = 0.0,

    leak_rate_kpa_per_hr = 0.0,
    smoke_ppm = 0.0,
    radiation_msv_per_day = 0.7
)
#----------------------------------------------------♡


def print_state(state, outputs, alerts):
    sol, hour, minutes = get_sol_time(state)
    status = get_status(state)
    WIDTH = 33

   # print("\n♡ ♡ ♡ ♡ Adore2113's MarsHSim ♡ ♡ ♡ ♡\n")

    print("\n♡ " + "═" * 30 + " ♡")
   # print("       Adore2113's MarsHSim")
    print("Adore2113's MarsHSim".center(WIDTH))
    print("♡ " + "═" * 30 + " ♡")
    
    print(("♡ [ TIME ] ♡").center(WIDTH))
   # print(f"{'Sol': <15} {sol} | {hour}:{minutes:02d} LMST")
   # print(f"Light level: {state.light_level:.2f}")
    print(f"{'Sol': <15} {sol} | {hour}:{minutes:02d} LMST\n")
    #print(f"{'Light Level:':<22} {state.light_level:.2f}")

    print(("♡ [ ATMOSPHERE ] ♡").center(WIDTH))
    if alerts:
        print(f"Alert: {alerts}")
    print(f"{'Oxygen:':<22} {state.o2_kpa:.2f} kPa")
    print(f"{'Carbon Dioxide:':<22} {state.co2_kpa:.2f}  kPa")
    print(f"{'Nitrogen:':<22} {state.n2_kpa:.2f} kPa")
    print(f"{'Argon:':<22} {state.ar_kpa:.2f} kPa")
    print(f"{'Total Pressure:':<22} {mca(state.o2_kpa, state.co2_kpa, state.n2_kpa, state.ar_kpa):.2f} kPa\n")

    print(("♡ [ RESOURCES ] ♡").center(WIDTH))
    print(f"{'Water Remaining:':<22} {state.water_for_oga_kg:.2f} kg")
    print(f"{'Hydrogen Stored:':<22} {state.h2_stored_kg:.2f}  kg\n")

    print(("♡ [ SYSTEMS ] ♡").center(WIDTH))
    print(f"{'CO2 Scrubbed:':<22} {outputs['co2_removed_kpa']:.2f} kPa")
    print(f"{'Scrubber Power Used:':<22} {outputs['co2_scrubber_power_used_kw']:.2f} kW")
    print(f"{'Scrubber Heat:':<22} {outputs['co2_scrubber_heat_kw']:.2f} kW")
    print(f"{'Scrubber Energy:':<22} {outputs['co2_scrubber_energy_used_kwh']:.2f} kWh")
    print(f"{'OGA Heat:':<22} {outputs['oga_heat_kw']:.2f} kW")
    print(f"{'Lights Power:':<22} {outputs['light_power_used_kw']:.2f} kW\n")

    print(("♡ [ POWER ] ♡").center(WIDTH))
    print(f"{'Total Power Used:':<22} {outputs['total_power_used_kw']:.2f} kW")
    print(f"{'Total Energy Used:':<22} {outputs['total_energy_used_kwh']:.2f} kWh")
    print(f"{'Solar Generated:':<22} {outputs['total_solar_generated_kw']:.2f} kW")
    print(f"{'Battery Stored:':<22} {state.battery_stored_kwh:.2f} kWh")

    print((f"\n♡ [ SYSTEM STATUS: {status} ] ♡\n").center(WIDTH))

    #--debug check:
    print(("♡ [ SUN DEBUG ] ♡").center(WIDTH))
    print(f"{'Daylight per m2:':<22} {state.daylight_m2_kw:.2f} kW")
    print(f"{'Peak Sun Today:':<22} {state.peak_sunlight_today:.1f} / 1.0")
    print(f"{'Low Sun Streak:':<22} {state.low_sunlight_streak_sols}")

    print("♡ " + "═" * 30 + " ♡")
    
    # ----- for printing when using the UI -----
    #print("\n♡ ♡ ♡ ♡ Adore2113's MarsHSim ♡ ♡ ♡ ♡\n")
    #print((f"[ SYSTEM STATUS: {status} ]")

    #print("[ TIME ]")
    #print(f"Sol: n/a | {hour}:{minutes:02d} {meridiem} LMST")
    #print(f"Light level: {state.light_level:.2f}")

    #print("[ ATMOSPHERE ]")
    #if alerts:
    #    print(f"Alert: {alerts}")
    #print(f"Oxygen: {state.o2_kpa:.3f} kPa")
    #print(f"Carbon Dioxide: {state.co2_kpa:.3f} kPa")
    #print(f"Nitrogen: {state.n2_kpa:.3f} kPa")
    #print(f"Argon: {state.ar_kpa:.3f} kPa")
    #print(f"Total Pressure: {mca(state.o2_kpa, state.co2_kpa, state.n2_kpa, state.ar_kpa):.3f} kPa")

    #print("[ RESOURCES ]")
    #print(f"Water remaining: {state.water_for_oga_kg:.3f} kg")
    #print(f"Hydrogen stored: {state.h2_stored_kg:.4f} kg")

    #print("[ SYSTEMS ]")
    #print(f"Carbon Dioxide Scrubbed: {outputs['co2_removed_kpa']:.4f} kPa")
    #print(f"Scrubber power used: {outputs['co2_scrubber_power_used_kw']:.4f} kW")
    #print(f"Scrubber heat: {outputs['co2_scrubber_heat_kw']:.4f} kW")
    #print(f"Scrubber energy: {outputs['co2_scrubber_energy_used_kwh']:.4f} kWh")
    #print(f"OGA heat: {outputs['oga_heat_kw']:.4f} kW")
    #print(f"Lights power: {outputs['light_power_used_kw']:.4f} kW")

    print()


state = s0
for i in range(12):    #turn this back to 12
    state, outputs = step(state)
    alerts = gas_alerts(state)
    print_state(state, outputs, alerts)

    if i % 12 == 0:
       print_state(state, outputs, alerts)