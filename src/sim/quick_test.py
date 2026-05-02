#--------------------imports-------------------------♡
from src.sim.state import Habitat_State
from src.sim.engine import step
from src.sim.mars_time import get_sol_time
from .buffer_gas_system import mca
from .alerts import get_alerts, get_status
#----------------------------------------------------♡


s0 = Habitat_State(
    #---------------time and daylight----------------♡
    mission_time_s = 0,

    daylight_m2_kw = 0.0,
    peak_sunlight_today = 0.0,
    low_sunlight_streak_sols = 0,
    
    #--------------------lights----------------------♡
    light_level = 0.0,

    #---------------------crew-----------------------♡
    crew_count = 30,
    crew_activity = "normal",
  
    #--------------------habitat---------------------♡
    hab_vol_m3 = 2000.0,

    #--------------------thermal---------------------♡
    hab_temp_c = 23.0,
    target_temp_c = 23.0,
    min_comfort_temp_c = 20.0,
    max_comfort_temp_c = 25.0,

    mars_temp_c = -20.0,

    current_humidity_pct = 48.0,
    target_humidity_pct = 48.0,

    insulation_strength_kw_per_c = 1.20,
    thermal_mass_kwh_per_c = 280.0,

    radiators = [
        {"id": 1, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
        {"id": 2, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
        {"id": 3, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
        {"id": 4, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
        {"id": 5, "status": "standby", "area_m2": 68, "efficiency": 0.95, "dust_factor": 1.0, "type": "primary"},
       
        {"id": 6, "status": "standby", "area_m2": 55, "efficiency": 0.85, "dust_factor": 1.0, "type": "backup"},
        {"id": 7, "status": "standby", "area_m2": 55, "efficiency": 0.85, "dust_factor": 1.0, "type": "backup"},
    ],

    heaters = [
        {"id": 1, "status": "standby", "power_kw": 9.0, "efficiency": 1.0, "type": "primary"},
        {"id": 2, "status": "standby", "power_kw": 9.0, "efficiency": 1.0, "type": "primary"},
        {"id": 3, "status": "standby", "power_kw": 9.0, "efficiency": 1.0, "type": "primary"},
        {"id": 4, "status": "standby", "power_kw": 9.0, "efficiency": 1.0, "type": "primary"},
        
        {"id": 5, "status": "standby", "power_kw": 8.0, "efficiency": 0.98, "type": "backup"},
        {"id": 6, "status": "standby", "power_kw": 8.0, "efficiency": 0.98, "type": "backup"},
    ],

#-------------------atmosphere-------------------♡
    #---------gas targets----------♡    
    target_pressure_kpa = 65.0,
    target_o2_kpa = 20.0,
    target_co2_kpa = 0.4,
    target_n2_kpa = 22.0,
    target_ar_kpa = 22.6,
    target_ch4_kg = 0.05,

    #-------min safe levels--------♡
    min_safe_pressure_kpa = 55.0,
   # min_safe_o2_kpa = ,
   # min_safe_co2_kpa = ,
   # min_safe_n2_kpa = ,
   # min_safe_ar_kpa = ,
    min_safe_ch4_kg = 0.5,

    #--------max safe levels-------♡
    max_safe_pressure_kpa = 70.0,
    #max_safe_o2_kpa = ,
    #max_safe_co2_kpa = ,
    #max_safe_n2_kpa = ,
    #max_safe_ar_kpa = ,
    #max_safe_ch4_kg = ,

    #------current gas levels------♡
    o2_kpa = 20.0,
    co2_kpa = 0.4,
    n2_kpa = 18.0,
    ar_kpa = 21.6,
    ch4_kg = 0.0,
    h2_kg = 0.0,    # figure this out

    #--------gas in storage--------♡
    n2_stored_kpa = 60.0,
    ar_stored_kpa = 30.0,
    co2_stored_kpa = 0.0,
    h2_stored_kg = 0.0,
    ch4_stored_kg = 0.0, 

    #------gas storage limits------♡
   # o2_storage_capacity_kg = 
   # co2_storage_capacity_kg = 
   # n2_storage_capacity_kg = 
   # ar_storage_capacity_kg = 
    ch4_storage_capacity_kg = 400.0,


    #------------------amine_beds--------------------♡
    amine_beds = [
        {"id": 1, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "primary"},
        {"id": 2, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "primary"},
        {"id": 3, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "primary"},
        {"id": 4, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "primary"},
        
        {"id": 5, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "backup"},
        {"id": 6, "status": "standby", "capacity": 3.0, "co2_load": 0.0, "type": "backup"},
    ],
    scrub_per_bed_kpa = 0.0035,

    #-----------------power / solar------------------♡
    battery_max_capacity_kwh = 1300.0,
    battery_stored_kwh = 1100.0,
    
    solar_arrays = [
        {"id": 1, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 2, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 3, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 4, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 5, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 6, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 7, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},
        {"id": 8, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "primary"},

        {"id": 9, "status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "backup"},
        {"id": 10,"status": "standby", "area_m2": 50, "efficiency": 0.28, "dust_factor": 1.0, "type": "backup"}
    ], 
    
    solar_absorptivity = 0.68,
    
    #---------------------water----------------------♡
    potable_water_storage_kg = 5000.0,
    gray_water_storage_kg = 0.0,
    black_water_storage_kg = 0.0,
    condensate_storage_kg = 0.0,
    brine_storage_kg = 0.0,

    potable_water_storage_capacity_kg = 6500.0,
    gray_water_storage_capacity_kg = 1200.0,
    black_water_storage_capacity_kg = 800.0,
    condensate_storage_capacity_kg = 250.0,
    brine_storage_capacity_kg = 400.0,

    #------------------placeholders------------------♡
    leak_rate_kpa_per_hr = 0.0,
    smoke_ppm = 0.0,
    radiation_msv_per_day = 0.7,

    #----------------wellness lights-----------------♡
    wellness_lights_on = False,

    #--------------------sabatier--------------------♡
    sabatier_on = False,
    #------------------------------------------------♡
        )


def print_state(state, outputs, alerts):
    sol, hour, minutes = get_sol_time(state)
    status = get_status(alerts)
    temp_change_per_hour = outputs.get("temp_change_c", 0) * 12    # change this later

    WIDTH = 33

    print("\n♡ " + "-" * 30 + " ♡")
    print("Adore2113's MarsHSim".center(WIDTH))
    print("♡ " + "-" * 30 + " ♡")

    #---------------time and daylight----------------♡
    print(f"{'Sol:':<19} {sol} | {hour:02d}:{minutes:02d} LMST")
    print(f"{'Habitat Temp:':<22} {state.hab_temp_c:.2f} °C")
    print(f"{'Mars Temp:':<22} {outputs['mars_temp_c']:.2f} °C")
    print(f"{'Peak Sun Today:':<22} {state.peak_sunlight_today:.3f} /1.0")
    print(f"{'Low Sun Streak:':<22} {state.low_sunlight_streak_sols} sols")
    print(f"{'Sunlight per m²:':<22} {state.daylight_m2_kw:.3f} kW")

    #----------------habitat status------------------♡
    print((f"\n♡  [  SYSTEM STATUS: {status}  ]  ♡").center(WIDTH))
    
    if alerts:
            print((f"♡      [  ALERT: {status}  ]      ♡").center(WIDTH))
    
    #-------------atmosphere / pressure--------------♡
    print(("\n♡      [   ATMOSPHERE    ]       ♡").center(WIDTH))  
    print(f"{'Total Pressure:':<22} {mca(state):.2f} kPa")    
    print(f"{'Oxygen:':<22} {state.o2_kpa:.2f} kPa")
    print(f"{'Carbon Dioxide:':<22} {state.co2_kpa:.2f} kPa")
    print(f"{'Nitrogen:':<22} {state.n2_kpa:.2f} kPa")
    print(f"{'Argon:':<22} {state.ar_kpa:.2f} kPa\n")
   
    print(f"Gas Added: {outputs['total_buffer_gas_added_kpa']:.3f} kPa")
    print(f"{'Gas Vented:':<22} {outputs.get('buffer_gas_vented_kpa'):.3f} kPa")
    print(f"Buffer Gas Mode: {outputs['buffer_gas_mode']}")
    print(f"Pressure Gap: {outputs['pressure_gap_kpa']:.3f} kPa")
    
    #-------------------resources--------------------♡
    print(("\n♡         [ RESOURCES ]          ♡").center(WIDTH))
    print(f"{'Potable Water:':<22} {state.potable_water_storage_kg:.2f} kg")
    print(f"{'Gray Water:':<22} {state.gray_water_storage_kg:.2f} kg")
    print(f"{'Black Water:':<22} {state.black_water_storage_kg:.2f} kg")
    print(f"{'Condensate:':<22} {state.condensate_storage_kg:.2f} kg")
    print(f"{'Brine:':<22} {state.brine_storage_kg:.2f} kg")
    print(f"{'Hydrogen Stored:':<22} {state.h2_stored_kg:.2f} kg")

    #---------------------water----------------------♡
    print(("\n♡      [   WATER SYSTEM   ]      ♡").center(WIDTH))
    print(f"{'Potable Used:':<22} {outputs.get('potable_water_used_kg', 0):.2f} kg")
    print(f"{'OGA Water Used:':<22} {outputs.get('oga_water_used_kg', 0):.2f} kg")
    print(f"{'Gray Added:':<22} {outputs.get('gray_water_added_kg', 0):.2f} kg")
    print(f"{'Black Added:':<22} {outputs.get('black_water_added_kg', 0):.2f} kg")
    print(f"{'Condensate Added:':<22} {outputs.get('vapor_removed_kg', 0):.2f} kg")
    
    print(f"{'UPA Brine Added:':<22} {outputs.get('upa_brine_added_kg', 0):.2f} kg")
    print(f"{'UPA Black Removed:':<22} {outputs.get('upa_black_water_removed_kg', 0):.2f} kg")
    print(f"{'WPA Processed:':<22} {outputs.get('wpa_water_processed_kg', 0):.2f} kg")
    print(f"{'BPA Processed:':<22} {outputs.get('bpa_water_processed_kg', 0):.2f} kg")
    
    print(f"{'Total Recovered:':<22} {outputs.get('total_recovered_water_kg', 0):.2f} kg")
    print(f"{'UPA Recovered:':<22} {outputs.get('upa_recovered_water_kg', 0):.2f} kg")
    print(f"{'WPA Recovered:':<22} {outputs.get('wpa_recovered_water_kg', 0):.2f} kg")
    print(f"{'BPA Recovered:':<22} {outputs.get('bpa_recovered_water_kg', 0):.2f} kg")

    #-------------------subsystems-------------------♡
    print(("\n♡         [  SYSTEMS  ]          ♡").center(WIDTH))
    print(f"{'Amine Beds Online:':<22} {outputs.get('beds_online_count', 0)}")
    print(f"{'CO2 Scrubbed:':<22} {outputs.get('co2_removed_kpa', 0):.3f} kPa")

    print(f"{'Scrubber Power Used:':<22} {outputs.get('co2_scrubber_power_used_kw', 0):.2f} kW")
    print(f"{'Scrubber Heat:':<22} {outputs.get('co2_scrubber_heat_kw', 0):.2f} kW")
    print(f"{'Scrubber Energy:':<22} {outputs.get('co2_scrubber_energy_used_kwh', 0):.2f} kWh")
    
    print(f"{'O2 Added:':<22} {outputs.get('o2_added_kpa', 0):.3f} kPa")
    print(f"{'OGA Heat:':<22} {outputs.get('oga_heat_kw', 0):.2f} kW")
    print(f"{'Lights Power:':<22} {outputs.get('light_power_used_kw', 0):.2f} kW")
    print(f"{'Lights Heat:':<22} {outputs.get('light_heat_kw', 0):.2f} kW")
 
    #--------------------power-----------------------♡
    print(("\n♡          [   POWER   ]         ♡").center(WIDTH))
    print(f"{'Total Power Used:':<22} {outputs.get('total_power_used_kw', 0):.2f} kW")
    print(f"{'Total Energy Used:':<22} {outputs.get('total_energy_used_kwh', 0):.2f} kWh")
    
    print(f"\n{'Solar Arrays Online:':<22} {outputs.get('solar_arrays_online_count', 0)} /10")
    print(f"{'Solar Generated:':<22} {outputs.get('total_solar_generated_kw', 0):.2f} kW")
    print(f"{'Battery Stored:':<22} {state.battery_stored_kwh:.2f} kWh")
    print(f"{'Wellness Lights:':<22} {'ON' if state.wellness_lights_on else 'OFF'}")

    #--------------------thermal---------------------♡
    print(("\n♡         [  THERMAL  ]          ♡").center(WIDTH))
    print((f"\n♡  [THERMAL MODE: {outputs['hab_temp_mode']}]  ♡\n").center(WIDTH))
    print(f"{'Habitat Temp:':<22} {state.hab_temp_c:.2f} °C")
    print(f"{'Mars Temp:':<22} {outputs.get('mars_temp_c', state.mars_temp_c):.2f} °C")

    print(f"{'Heat Loss:':<22} {outputs.get('heat_loss_kw', 0):.2f} kW")
    
    print(f"{'Net Heat:':<22} {outputs.get('net_heat_kw', 0):.2f} kW")
    print(f"{'Temp Trend:':<20} ~ {temp_change_per_hour:.3f} °C/hr")    
    
    print(f"{'Humidity:':<22} {outputs.get('new_humidity_pct', state.current_humidity_pct):.2f} %")
    print(f"{'Vapor Removed:':<22} {outputs.get('vapor_removed_kg', 0):.2f} kg")
    
    print(f"{'CHX Power Used:':<22} {outputs.get('chx_power_used_kw', 0):.2f} kW")
    print(f"{'CHX Heat:':<22} {outputs.get('chx_heat_added_kw', 0):.2f} kW")

    print(f"{'Radiators Online:':<22} {outputs.get('radiators_online_count', 0)}")
    print(f"{'Rad Cooling:':<22} {outputs.get('radiator_heat_rejection_kw', 0):.2f} kW")
    print(f"{'Rad Power:':<22} {outputs.get('radiator_power_kw', 0):.2f} kW\n")
        
    print(f"{'Heaters Online:':<22} {outputs.get('heaters_online_count', 0)}")
    print(f"{'Heater Heat:':<22} {outputs.get('heater_heat_kw', 0):.2f} kW")
    print(f"{'Heater Power Used:':<22} {outputs.get('heater_power_kw', 0):.2f} kW")
    print(f"{'Heater Energy:':<22} {outputs.get('heater_energy_kwh', 0):.2f} kWh")

  #  print(f"{'Thermal Mode:':<22} {outputs['hab_temp_mode']}\n")
   
    print("♡ " + "-" * 30 + " ♡")
#----------------------------------------------------♡
    

state = s0
for i in range(200):
    state, outputs = step(state)
    alerts = get_alerts(state, outputs)

    if i % 12 == 0:
        print_state(state, outputs, alerts)