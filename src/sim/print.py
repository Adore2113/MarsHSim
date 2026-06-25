#--------------------imports-------------------------♡
from .mars_time import get_sol_time
from .buffer_gas import mca
from .alerts import get_status
#----------------------------------------------------♡


#--------------------constants-----------------------♡
width = 33
deco = "\n♡ " + "-" * 30 + " ♡"
split = "-" * width
lw = 22    # label width
#----------------------------------------------------♡

#----------------------header------------------------♡
def print_header():
    print(deco)
    print("Adore2113's MarsHSim".center(width))
    print(deco)
#----------------------------------------------------♡

#-------------------section header-------------------♡
def print_section_header(title):
    title_text = f"{title}"
    white_space = width - len(title_text)
    left_space = white_space // 2
    right_space = white_space - left_space

    left_split = "›" * left_space
    right_split = "‹" * right_space

    print(f"\n{left_split}{title}{right_split}")
#----------------------------------------------------♡


#---------------------full print---------------------♡
def print_sim(state, outputs, alerts):
    print_header()
    print_system_stats(alerts)
    print_environment(state, outputs)
    print_atmosphere(state, outputs)
    print_power(state, outputs)
    print_thermal(state, outputs)
    print_water(state, outputs)
    print (split)
#----------------------------------------------------♡


#-------------------system status--------------------♡
def print_system_stats(alerts):
    status = get_status(alerts)
    print_section_header(f"SYSTEM STATUS: {status}")

    if alerts:
        for alert in alerts:
            print(f"\n⚠ {alert:<{lw}}")
    
    else:
        print("\n🙂 ALL SYSTEMS NOMINAL 🙂".center(width))
#----------------------------------------------------♡

#------------------time / environment----------------♡
def print_environment(state, outputs):
    sol, hour, minutes = get_sol_time(state)

    print(f"\n{'Sol:':<19} {sol} | {hour:02d}:{minutes:02d} LMST")
    print(f"{'Habitat Temp:':<{lw}} {state.hab_temp_c:.3f} °C")
    print(f"{'Mars Temp:':<{lw}} {outputs['mars_temp_c']:.2f} °C")
    print(f"{'Food Produced:':<{lw}} {outputs.get('greenhouse_food_produced_kg', 0):.3f} kg")
    print(f"{'Temp Change/h:':<{lw}} {outputs.get('temp_change_c', 0) * 12:.2f} C")
#----------------------------------------------------♡

#--------------------atmosphere----------------------♡
def print_atmosphere(state, outputs):
    print_section_header("ATMOSPHERE")

    #------current atmosphere------♡
    print(f"{'Total Pressure:':<{lw}} {mca(state):.2f} kPa")

    print(f"{'Oxygen:':<{lw}} {state.o2_kpa:.2f} kPa")
    print(f"{'Carbon Dioxide:':<{lw}} {state.co2_kpa:.2f} kPa")
    print(f"{'Nitrogen:':<{lw}} {state.n2_kpa:.2f} kPa")
    print(f"{'Argon:':<{lw}} {state.ar_kpa:.2f} kPa")
    print(f"{'Methane:':<{lw}} {state.ch4_kpa:.2f} kPa")

    #------buffer gas control------♡
    print(f"\n{'Buffer Gas Mode:':<{lw}} {outputs['buffer_gas_mode']}")
    print(f"{'Pressure Gap:':<{lw}} {outputs['pressure_gap_kpa']:.3f} kPa")
    
    print(f"{'Buffer Gas Added:':<{lw}} {outputs['total_buffer_gas_added_kpa']:.3f} kPa")
    print(f"{'Buffer Gas Vented:':<{lw}} {outputs.get('total_buffer_gas_vented_kpa', 0.0):.3f} kPa")

    #----------stored gas----------♡
    print(f"\n{'O2 Stored:':<{lw}} {state.o2_stored_kg:.2f} kg")
    print(f"{'CO2 Stored:':<{lw}} {state.co2_stored_kg:.2f} kg")
    print(f"{'N2 Stored:':<{lw}} {state.n2_stored_kg:.2f} kg")
    print(f"{'AR Stored:':<{lw}} {state.ar_stored_kg:.2f} kg")
    print(f"{'H2 Stored:':<{lw}} {state.h2_stored_kg:.2f} kg")
    print(f"{'CH4 Stored:':<{lw}} {state.ch4_stored_kg:.2f} kg")    

    #----------stored gas----------♡
    print(f"\n{'ISRU ATM Mode:':<{lw}} {outputs.get('isru_atm_mode', 'offline')}")
    print(f"{'Compressors:':<{lw}} {outputs.get('compressors_extracting', 0)}")

    print(f"{'Beds Adsorbing:':<{lw}} {outputs.get('sorbent_beds_adsorbing', 0)}")
    print(f"{'Beds Regen:':<{lw}} {outputs.get('sorbent_beds_regenerating', 0)}")
    print(f"{'Beds Standby:':<{lw}} {outputs.get('sorbent_beds_standby', 0)}")

    print(f"{'N2 Added:':<{lw}} {outputs.get('isru_n2_added_kg', 0):.3f} kg")
    print(f"{'AR Added:':<{lw}} {outputs.get('isru_ar_added_kg', 0):.3f} kg")
    print(f"{'CO2 Captured:':<{lw}} {outputs.get('sorbent_co2_absorbed_kg', 0):.3f} kg")

    #-----------gas moved-----------♡
    print(f"\n{'Amine Beds Online:':<{lw}} {outputs.get('beds_online_count', 0)}")

    print(f"{'GH CO2 Used':<{lw}} {outputs.get('greenhouse_co2_consumed_kpa', 0):.8f} kPa")
    print(f"{'Sabatier CO2:':<{lw}} {outputs.get('sabatier_co2_consumed_kpa', 0):.4f} kPa")
    print(f"{'CO2 Scrubbed:':<{lw}} {outputs.get('co2_removed_kpa', 0):.4f} kPa")

    print(f"{'O2 Added:':<{lw}} {outputs.get('o2_added_kpa', 0):.4f} kPa")

    print(f"{'CH4 Added:':<{lw}} {outputs.get('sabatier_ch4_produced_kg', 0):.4f} kg")
    print(f"{'CH4 Vented:':<{lw}} {outputs.get('sabatier_ch4_vented_kg', 0):.4f} kg")
   
    print(f"{'H2 Used:':<{lw}} {outputs.get('sabatier_h2_consumed_kg', 0):.4f} kg")
    
    print(f"{'GH O2 Added:':<{lw}} {outputs.get('greenhouse_o2_produced_kpa', 0):.8f} kPa")
#----------------------------------------------------♡

#-----------------------power------------------------♡
def print_power(state, outputs):
    print_section_header("POWER")
    print(f"Net Energy: {outputs['net_energy_kwh']:.2f} kWh")
    #-------------solar-------------♡
    print(f"{'Peak Sun Today:':<{lw}} {state.peak_sunlight_today:.3f} /1.0")
    print(f"{'Sunlight per m²:':<{lw}} {state.daylight_m2_kw:.3f} kW")
    print(f"{'Low Sun Streak:':<{lw}} {state.low_sunlight_streak_sols} sols")

    print(f"{'Solar Arrays Online:':<{lw}} {outputs.get('solar_arrays_online_count', 0)} /10")
    print(f"{'Solar Generated:':<{lw}} {outputs.get('total_solar_generated_kw', 0):.2f} kW")
    #-------------stored------------♡
    print(f"{'Battery Stored:':<{lw}} {state.battery_stored_kwh:.2f} kWh")
    
    #----------powered on-----------♡
    print(f"\n{'Wellness Lights:':<{lw}} {'ON' if state.wellness_lights_on else 'OFF'}")
    print(f"{'GH Mode:':<{lw}} {outputs.get('greenhouse_mode', 'offline')}")

    #-----------power used----------♡
    print(f"\n{'Total Power Used:':<{lw}} {outputs.get('total_power_used_kw', 0):.2f} kW")

    print(f"{'GH Power:':<{lw}} {outputs.get('greenhouse_led_power_kw', 0):.2f} kW")
    print(f"{'Sabatier Power:':<{lw}} {outputs.get('sabatier_power_used_kw', 0):.2f} kW")
    print(f"{'Scrubber Power:':<{lw}} {outputs.get('amine_bed_power_used_kw', 0):.2f} kW")
    print(f"{'Lights Power:':<{lw}} {outputs.get('light_power_used_kw', 0):.2f} kW")
    print(f"{'CHX Power:':<{lw}} {outputs.get('chx_power_used_kw', 0):.2f} kW")
    print(f"{'Radiator Power:':<{lw}} {outputs.get('radiator_power_kw', 0):.2f} kW")
    print(f"{'Heater Power:':<{lw}} {outputs.get('heater_power_kw', 0):.2f} kW")
    print(f"{'ISRU Power:':<{lw}} {outputs.get('isru_power_used_kw', 0):.2f} kW")

    print(f"{'Total Energy Used:':<{lw}} {outputs.get('total_energy_used_kwh', 0):.2f} kWh")
#----------------------------------------------------♡

#----------------------thermal-----------------------♡
def print_thermal(state, outputs):
    temp_change_per_hour = outputs.get("temp_change_c", 0) * 12

    print_section_header(f"THERMAL MODE: {outputs['hab_temp_mode']}")
    
    #----------environment----------♡
    print(f"{'Mars Temp:':<{lw}} {outputs.get('mars_temp_c', state.mars_temp_c):.2f} °C")
    print(f"{'Habitat Temp:':<{lw}} {state.hab_temp_c:.2f} °C")
    print(f"{'Heat Loss:':<{lw}} {outputs.get('heat_loss_kw', 0):.2f} kW")

    print(f"{'Temp Trend:':<{lw}} ~ {temp_change_per_hour:.3f} °C/hr")    
    
    #-----------heat added----------♡
    print(f"\n{'Net Heat:':<{lw}} {outputs.get('net_heat_kw', 0):.2f} kW")
    
    print(f"{'Heaters Online:':<{lw}} {outputs.get('heaters_online_count', 0)}")
    print(f"{'Heater Heat:':<{lw}} {outputs.get('heater_heat_kw', 0):.2f} kW")

    print(f"{'ISRU Heat:':<{lw}} {outputs.get('isru_heat_added_kw', 0):.2f} kW")
    print(f"{'GH Heat:':<{lw}} {outputs.get('total_greenhouse_heat_kw', 0):.3f} kW")
    print(f"{'Sabatier Heat:':<{lw}} {outputs.get('sabatier_heat_added_kw', 0):.2f} kW")
    print(f"{'Amine Bed Heat:':<{lw}} {outputs.get('amine_bed_heat_added_kw', 0):.2f} kW")
    print(f"{'Light Heat:':<{lw}} {outputs.get('light_heat_kw', 0):.2f} kW")
    print(f"{'CHX Heat:':<{lw}} {outputs.get('chx_heat_added_kw', 0):.2f} kW")
    print(f"{'OGA Heat:':<{lw}} {outputs.get('oga_heat_kw', 0):.2f} kW")

    #-----------cooling-------------♡
    print(f"\n{'Radiators Online:':<{lw}} {outputs.get('radiators_online_count', 0)}")
    print(f"{'Radiator Cooling:':<{lw}} {outputs.get('radiator_heat_rejection_kw', 0):.2f} kW")
#----------------------------------------------------♡

#-----------------------ISRU-------------------------♡
def print_isru(state, outputs):
    print_section_header("ISRU")
    print(f"{'ISRU Mode:':<{lw}} {outputs.get('isru_mode', 'offline')}")

    print(f"{'Pipes Extracting:':<{lw}} {outputs.get('pipes_extracting', 0)}")
    print(f"{'Pipes Deploying:':<{lw}} {outputs.get('pipes_deploying', 0)}")
    print(f"{'Pipes Retracting:':<{lw}} {outputs.get('pipes_retracting', 0)}")
    print(f"{'Total Pipes Active:':<{lw}} {outputs.get('total_pipes_active', 0)}")
#----------------------------------------------------♡

#----------------------water-------------------------♡
def print_water(state, outputs):
    print_section_header("WATER")

    #---------humidity / CHX--------♡
    print(f"{'Vapor Added:':<{lw}} {outputs.get('vapor_added_kg', 0):.3f} kg")
    print(f"{'Humidity:':<{lw}} {outputs.get('new_humidity_pct', state.current_humidity_pct):.2f} %")
    print(f"{'Vapor Removed:':<{lw}} {outputs.get('vapor_removed_kg', 0):.2f} kg")

    #----------greenhouse-----------♡
    print(f"{'GH Transpiration:':<{lw}} {outputs.get('greenhouse_transpiration_kg', 0):.3f} kg")
    print(f"\n{'GH Water Needed:':<{lw}} {outputs.get('greenhouse_water_needed_kg', 0):.3f} kg")
    print(f"{'GH Water Used:':<{lw}} {outputs.get('greenhouse_water_consumed_kg', 0):.2f} kg")
    print(f"{'GH Recirculated:':<{lw}} {outputs.get('greenhouse_water_recirculated_kg', 0):.3f} kg")

    #----------processing-----------♡
    print(f"\n{'UPA Black Removed:':<{lw}} {outputs.get('upa_black_water_removed_kg', 0):.2f} kg")
    print(f"{'WPA Processed:':<{lw}} {outputs.get('wpa_water_processed_kg', 0):.2f} kg")
    print(f"{'BPA Processed:':<{lw}} {outputs.get('bpa_water_processed_kg', 0):.2f} kg")

    #----------water used-----------♡
    print(f"{'Potable Used:':<{lw}} {outputs.get('potable_water_used_kg', 0):.2f} kg")
    print(f"{'OGA Water Used:':<{lw}} {outputs.get('oga_water_used_kg', 0):.2f} kg")

    #--------water recovered--------♡
    print(f"\n{'Total Recovered:':<{lw}} {outputs.get('total_recovered_water_kg', 0):.2f} kg")
    print(f"{'UPA Recovered:':<{lw}} {outputs.get('upa_recovered_water_kg', 0):.2f} kg")
    print(f"{'WPA Recovered:':<{lw}} {outputs.get('wpa_recovered_water_kg', 0):.2f} kg")
    print(f"{'BPA Recovered:':<{lw}} {outputs.get('bpa_recovered_water_kg', 0):.2f} kg")

    #----------water added----------♡
    print(f"\n{'Gray Added:':<{lw}} {outputs.get('gray_water_added_kg', 0):.2f} kg")
    print(f"{'Black Added:':<{lw}} {outputs.get('black_water_added_kg', 0):.2f} kg")
    print(f"{'Condensate Added:':<{lw}} {outputs.get('vapor_removed_kg', 0):.2f} kg")
    print(f"{'UPA Brine Added:':<{lw}} {outputs.get('upa_brine_added_kg', 0):.2f} kg")
    print(f"{'Sabatier Water Added:':<{lw}} {outputs.get('sabatier_water_produced_kg', 0):.3f} kg")
    print(f"{'Raw Water Added:':<{lw}} {outputs.get('isru_raw_water_added_kg', 0):.2f} kg")

    #-----------storage-------------♡
    print(f"\n{'Potable Water:':<{lw}} {state.potable_water_storage_kg:.2f} kg")
    print(f"{'Gray Water:':<{lw}} {state.gray_water_storage_kg:.2f} kg")
    print(f"{'Black Water:':<{lw}} {state.black_water_storage_kg:.2f} kg")
    print(f"{'Condensate:':<{lw}} {state.condensate_storage_kg:.2f} kg")
    print(f"{'Brine:':<{lw}} {state.brine_storage_kg:.2f} kg")
    print(f"{'Raw Water Stored:':<{lw}} {state.raw_isru_water_storage_kg:.2f} kg")
#----------------------------------------------------♡
