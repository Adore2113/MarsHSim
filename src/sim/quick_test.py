from src.sim.state import Habitat_State
from src.sim.engine import step
from src.sim.mars_time import get_sol_time
from .buffer_gas_system import mca
from .alerts import get_alerts, get_status
from .temp_system import get_thermal_alerts

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

# ------thermal control-----------------------------♡
    hab_temp_c = 23.0,
    target_humidity_pct = 48.0,
    current_humidity_pct = 48.0,

    insulation_strength_kw_per_c = 0.8,
    thermal_mass_kwh_per_c = 800.0,

    radiators = [
        {"id" : 1, "status" : "standby", "area_m2" : 60, "efficiency" : 0.9, "dust_factor" : 1.0},
        {"id" : 2, "status" : "standby", "area_m2" : 60, "efficiency" : 0.9, "dust_factor" : 1.0},
        {"id" : 3, "status" : "standby", "area_m2" : 60, "efficiency" : 0.9, "dust_factor" : 1.0},
        {"id" : 4, "status" : "standby", "area_m2" : 60, "efficiency" : 0.9, "dust_factor" : 1.0},
        {"id" : 5, "status" : "standby", "area_m2" : 60, "efficiency" : 0.9, "dust_factor" : 1.0},
        {"id" : 6, "status" : "standby", "area_m2" : 60, "efficiency" : 0.9, "dust_factor" : 1.0},
        {"id" : 7, "status" : "standby", "area_m2" : 60, "efficiency" : 0.9, "dust_factor" : 1.0},
        {"id" : 8, "status" : "standby", "area_m2" : 60, "efficiency" : 0.9, "dust_factor" : 1.0},
    ],

    heaters = [
        {"id" : 1, "status" : "standby", "power_kw" : 8.0, "efficiency" : 1.0},
        {"id" : 2, "status" : "standby", "power_kw" : 8.0, "efficiency" : 1.0},
        {"id" : 3, "status" : "standby", "power_kw" : 8.0, "efficiency" : 1.0},
        {"id" : 4, "status" : "standby", "power_kw" : 8.0, "efficiency" : 1.0},
        {"id" : 5, "status" : "standby", "power_kw" : 8.0, "efficiency" : 1.0},
        {"id" : 6, "status" : "standby", "power_kw" : 8.0, "efficiency" : 1.0},
        {"id" : 7, "status" : "standby", "power_kw" : 8.0, "efficiency" : 1.0},
        {"id" : 8, "status" : "standby", "power_kw" : 8.0, "efficiency" : 1.0},
    ],
    
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

# ------amine beds----------------------------------♡
    amine_beds = [
        {"id" : 1, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0},
        {"id" : 2, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0},
        {"id" : 3, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0},
        {"id" : 4, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0}
    #    {"id" : 5, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0},
    #    {"id" : 6, "status" : "standby", "capacity" : 3.0, "co2_load" : 0.0}
  
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
    solar_absorptivity = 0.65,
    
# ------water---------------------------------------♡

    potable_water_storage_kg = 5000.0,
    gray_water_storage_kg = 0.0,
    black_water_storage_kg = 0.0,
    condensate_storage_kg = 0.0,
    brine_storage_kg = 0.0,

    potable_water_storage_capacity_kg = 5000.0,    # placeholder
    gray_water_storage_capacity_kg = 500.0,    # placeholder
    black_water_storage_capacity_kg = 300.0,    # placeholder
    condensate_storage_capacity_kg = 80.0,    # placeholder
    brine_storage_capacity_kg = 150.0,    # placeholder

# ------placeholders for future plans---------------♡

    # ♡ Integrity / safety ♡
    leak_rate_kpa_per_hr = 0.0,
    smoke_ppm = 0.0,
    radiation_msv_per_day = 0.7,

# --------wellness lights on or off-----------------♡
    wellness_lights_on = False,
    )
#----------------------------------------------------♡


def print_state(state, outputs, alerts):
    sol, hour, minutes = get_sol_time(state)
    status = get_status(alerts)
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

    print((f"\n♡ [ SYSTEM STATUS: {status} ] ♡\n").center(WIDTH))

    print(("♡ [ ATMOSPHERE ] ♡").center(WIDTH))
    if alerts:
        print(f"Alert: {alerts}")
    print(f"{'Oxygen:':<22} {state.o2_kpa:.2f} kPa")
    print(f"{'Carbon Dioxide:':<22} {state.co2_kpa:.2f}  kPa")
    print(f"{'Nitrogen:':<22} {state.n2_kpa:.2f} kPa")
    print(f"{'Argon:':<22} {state.ar_kpa:.2f} kPa")
    print(f"{'Total Pressure:':<22} {mca(state.o2_kpa, state.co2_kpa, state.n2_kpa, state.ar_kpa):.2f} kPa\n")

    print(("♡ [ RESOURCES ] ♡").center(WIDTH))
    print(f"{'Hydrogen Stored:':<22} {state.h2_stored_kg:.2f}  kg")
    print(f"{'Potable Water:':<22} {state.potable_water_storage_kg:.2f} kg")
    print(f"{'Gray Water:':<22} {state.gray_water_storage_kg:.2f} kg")
    print(f"{'Black Water:':<22} {state.black_water_storage_kg:.2f} kg")
    print(f"{'Condensate:':<22} {state.condensate_storage_kg:.2f} kg")
    print(f"{'Brine:':<22} {state.brine_storage_kg:.2f} kg\n")

    print(("♡ [ SYSTEMS ] ♡").center(WIDTH))
    print(f"{'CO2 Scrubbed:':<22} {outputs['co2_removed_kpa']:.4f} kPa")
    print(f"{'Scrubber Power Used:':<22} {outputs['co2_scrubber_power_used_kw']:.2f} kW")
    print(f"{'Scrubber Heat:':<22} {outputs['co2_scrubber_heat_kw']:.2f} kW")
    print(f"{'Scrubber Energy:':<22} {outputs['co2_scrubber_energy_used_kwh']:.2f} kWh")
    print(f"{'O2 Added:':<22} {outputs['o2_added_kpa']:.4f} kPa")
    print(f"{'OGA Water Used:':<22} {outputs['oga_water_used_kg']:.4f} kg")
    print(f"{'OGA Heat:':<22} {outputs['oga_heat_kw']:.2f} kW")
    print(f"{'Lights Power:':<22} {outputs['light_power_used_kw']:.2f} kW\n")
    print(f"{'Lights Heat:':<22} {outputs['light_heat_kw']:.2f} kW\n")

    print(("♡ [ POWER ] ♡").center(WIDTH))
    print(f"{'Total Power Used:':<22} {outputs['total_power_used_kw']:.2f} kW")
    print(f"{'Total Energy Used:':<22} {outputs['total_energy_used_kwh']:.2f} kWh")
    print(f"{'Solar Generated:':<22} {outputs['total_solar_generated_kw']:.4f} kW")
    print(f"{'Battery Stored:':<22} {state.battery_stored_kwh:.2f} kWh\n")

    print(("♡ [ THERMAL ] ♡").center(WIDTH))
    print(f"{'Habitat Temp:':<22} {state.hab_temp_c:.2f} °C")
    print(f"{'Mars Temp:':<22} {outputs['mars_temp_c']:.2f} °C")
    
    print(f"{'Habitat Heat:':<22} {outputs['hab_heat_kw']:.2f} kW")
    print(f"{'Heat Loss:':<22} {outputs['heat_loss_kw']:.2f} kW")
    print(f"{'Net Heat:':<22} {outputs['net_heat_kw']:.2f} kW")
    print(f"{'Temp Change:':<22} {outputs['temp_change_c']:.4f} °C")
    print(f"{'Insulation Strength:':<22} {state.insulation_strength_kw_per_c:.2f} kW/°C")
    
    print(f"{'Humidity:':<22} {outputs['new_humidity_pct']:.2f} %")
    print(f"{'Vapor Removed:':<22} {outputs['vapor_removed_kg']:.4f} kg")
    
    print(f"{'CHX Power Used:':<22} {outputs['chx_power_used_kw']:.2f} kW")
    print(f"{'CHX Heat:':<22} {outputs['chx_heat_added_kw']:.2f} kW\n")

    print(f"{'Radiators Online:':<22} {outputs['radiators_online_count']}")
    print(f"{'Rad Cooling:':<22} {outputs['radiator_heat_rejection_kw']:.2f} kW")
    print(f"{'Rad Power:':<22} {outputs['radiator_power_kw']:.2f} kW")
        
    print(f"{'Heaters Online:':<22} {outputs['heaters_online_count']}")
    print(f"{'Heater Heat:':<22} {outputs['heater_heat_kw']:.2f} kW")
    print(f"{'Heater Power Used:':<22} {outputs['heater_power_kw']:.2f} kW")
    print(f"{'Heater Energy:':<22} {outputs['heater_energy_kwh']:.2f} kWh")
    
    print(f"{'Thermal Mode:':<22} {outputs['hab_temp_mode']}\n")

    print(("♡ [ WATER SYSTEM ] ♡").center(WIDTH))
    print(f"{'Potable Used:':<22} {outputs['potable_water_used_kg']:.2f} kg")
   
    print(f"{'Gray Added:':<22} {outputs['gray_water_added_kg']:.2f} kg")
    print(f"{'Black Added:':<22} {outputs['black_water_added_kg']:.2f} kg")
    print(f"{'Condensate Added:':<22} {outputs['vapor_removed_kg']:.2f} kg")
    
    print(f"{'UPA Recovered:':<22} {outputs['upa_recovered_water_kg']:.2f} kg")
    print(f"{'UPA Brine Added:':<22} {outputs['upa_brine_added_kg']:.2f} kg")
    print(f"{'UPA Black Removed:':<22} {outputs['upa_black_water_removed_kg']:.2f} kg")
    
    print(f"{'WPA Recovered:':<22} {outputs['wpa_recovered_water_kg']:.2f} kg")
    print(f"{'WPA Processed:':<22} {outputs['wpa_water_processed_kg']:.2f} kg")
    
    print(f"{'BPA Recovered:':<22} {outputs['bpa_recovered_water_kg']:.2f} kg")
    print(f"{'BPA Processed:':<22} {outputs['bpa_water_processed_kg']:.2f} kg")
    
    print(f"{'Total Recovered:':<22} {outputs['total_recovered_water_kg']:.2f} kg\n")

    #--debug check:
    print(("♡ [ SUN INFORMATION ] ♡").center(WIDTH))
    print(f"{'Daylight per m2:':<22} {state.daylight_m2_kw:.3f} kW")
    print(f"{'Peak Sun Today:':<22} {state.peak_sunlight_today:.2f} / 1.0")
    print(f"{'Low Sun Streak:':<22} {state.low_sunlight_streak_sols}")

    print("♡ " + "═" * 30 + " ♡")
    

state = s0
for i in range(12):    #turn this back to 12
    state, outputs = step(state)
    alerts = get_alerts(state, outputs)
    print_state(state, outputs, alerts)

    if i % 20 == 0:
       print_state(state, outputs, alerts)