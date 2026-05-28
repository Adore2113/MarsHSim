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

    left_split = "⋙" * left_space
    right_split = "⋘" * right_space

    print(f"\n{left_split}{title}{right_split}")
#----------------------------------------------------♡


#-------------------system status--------------------♡
def print_system_stats(alerts):
    status = get_status(alerts)
    print_section_header(f"SYSTEM STATUS: {status}")

    if alerts:
        print_section_header(f"ALERT: {status}")
#----------------------------------------------------♡


#------------------time / environment----------------♡
def print_environment(state, outputs):
    sol, hour, minutes = get_sol_time(state)
    temp_change_per_hour = outputs.get("temp_change_c", 0) * 12    # change this later

    print(f"{'Sol:':<19} {sol} | {hour:02d}:{minutes:02d} LMST")
    print(f"{'Habitat Temp:':<{lw}} {state.hab_temp_c:.3f} °C")
    print(f"{'Mars Temp:':<{lw}} {outputs['mars_temp_c']:.2f} °C")

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
    
    #------buffer gas control------♡
    print(f"{'Buffer Gas Mode:':<{lw}} {outputs['buffer_gas_mode']}")
    print(f"{'Pressure Gap:':<{lw}} {outputs['pressure_gap_kpa']:.3f} kPa")
    
    print(f"{'Gas Added:':<{lw}} {outputs['total_buffer_gas_added_kpa']:.3f} kPa")
    print(f"{'Gas Vented:':<{lw}} {outputs.get('total_buffer_gas_vented_kpa', 0.0):.3f} kPa")

    #----------stored gas----------♡
    print(f"{'O2 Stored:':<{lw}} {state.o2_stored_kg:.2f} kg")
    print(f"{'CO2 Stored:':<{lw}} {state.co2_stored_kg:.2f} kg")
    print(f"{'N2 Stored:':<{lw}} {state.n2_stored_kg:.2f} kg")
    print(f"{'AR Stored:':<{lw}} {state.ar_stored_kg:.2f} kg")

    print(f"{'H2 Stored:':<{lw}} {state.h2_stored_kg:.2f} kg")
    print(f"{'CH4 Stored:':<{lw}} {state.ch4_stored_kg:.2f} kg")    
    
    #-----------gas moved-----------♡
    print(f"{'Amine Beds Online:':<22} {outputs.get('beds_online_count', 0)}")

    print(f"{'CO2 Consumed:':<{lw}} {outputs.get('sabatier_co2_consumed_kpa', 0):.3f} kPa")
    print(f"{'CO2 Scrubbed:':<{lw}} {outputs.get('co2_removed_kpa', 0):.3f} kPa")

    print(f"{'O2 Added:':<{lw}} {outputs.get('o2_added_kpa', 0):.3f} kPa")

    print(f"{'CH4 Produced:':<{lw}} {outputs.get('sabatier_ch4_produced_kg', 0):.2f} kg")
    print(f"{'CH4 Vented:':<{lw}} {outputs.get('sabatier_ch4_vented_kg', 0):.2f} kg")
    print(f"{'H2 Consumed:':<{lw}} {outputs.get('sabatier_h2_consumed_kg', 0):.2f} kg")
    print(f"{'O2 Produced:':<{lw}} {outputs.get('total_o2_produced_kpa', 0):.3f} kPa")
#----------------------------------------------------♡


#-----------------------power------------------------♡
def print_power(state, outputs):
    print_section_header("POWER")

    #-------------solar-------------♡
    print(f"{'Peak Sun Today:':<{lw}} {state.peak_sunlight_today:.3f} /1.0")
    print(f"{'Sunlight per m²:':<{lw}} {state.daylight_m2_kw:.3f} kW")
    print(f"{'Low Sun Streak:':<{lw}} {state.low_sunlight_streak_sols} sols")

    print(f"\n{'Solar Arrays Online:':<{lw}} {outputs.get('solar_arrays_online_count', 0)} /10")
    print(f"{'Solar Generated:':<{lw}} {outputs.get('total_solar_generated_kw', 0):.2f} kW")
    #-------------stored------------♡
    print(f"{'Battery Stored:':<{lw}} {state.battery_stored_kwh:.2f} kWh")
    
    #----------powered on-----------♡
    print(f"{'Wellness Lights:':<{lw}} {'ON' if state.wellness_lights_on else 'OFF'}")
    print(f"{'Mode:':<22} {outputs.get('greenhouse_mode', 'offline')}")

    #-----------power used----------♡
    print(f"{'Total Power Used:':<{lw}} {outputs.get('total_power_used_kw', 0):.2f} kW")

    print(f"{'GH Power Used:':<{lw}} {outputs.get('total_led_power_kw', 0):.2f} kW")
    print(f"{'Power Used:':<{lw}} {outputs.get('sabatier_power_used_kw', 0):.2f} kW")
    print(f"{'Scrubber Power Used:':<{lw}} {outputs.get('amine_bed_power_used_kw', 0):.2f} kW")
    print(f"{'Lights Power:':<{lw}} {outputs.get('light_power_used_kw', 0):.2f} kW")
    print(f"{'CHX Power Used:':<{lw}} {outputs.get('chx_power_used_kw', 0):.2f} kW")
    print(f"{'Rad Power:':<{lw}} {outputs.get('radiator_power_kw', 0):.2f} kW\n")
    print(f"{'Heater Power Used:':<{lw}} {outputs.get('heater_power_kw', 0):.2f} kW")

    print(f"{'Total Energy Used:':<{lw}} {outputs.get('total_energy_used_kwh', 0):.2f} kWh")
#----------------------------------------------------♡


#----------------------thermal-----------------------♡
def print_thermal(state, outputs):
    temp_change_per_hour = outputs.get("temp_change_c", 0) * 12

    print_section_header("THERMAL")
    #----------environment----------♡

    print(f"{'Mars Temp:':<22} {outputs.get('mars_temp_c', state.mars_temp_c):.2f} °C")
    print(f"{'Habitat Temp:':<22} {state.hab_temp_c:.2f} °C")
    print(f"{'Heat Loss:':<22} {outputs.get('heat_loss_kw', 0):.2f} kW")

    print(f"{'Temp Trend:':<20} ~ {temp_change_per_hour:.3f} °C/hr")    
    
    #-----------heat added----------♡
    print(f"{'Net Heat:':<22} {outputs.get('net_heat_kw', 0):.2f} kW")
    
    print(f"{'Heaters Online:':<22} {outputs.get('heaters_online_count', 0)}")
    print(f"{'Heater Heat:':<22} {outputs.get('heater_heat_kw', 0):.2f} kW")

    print(f"{'GH Heat Added:':<22} {outputs.get('total_greenhouse_heat_kw', 0):.3f} kW")
    print(f"{'Heat Added:':<22} {outputs.get('sabatier_heat_added_kw', 0):.2f} kW")
    print(f"{'Scrubber Heat:':<22} {outputs.get('amine_bed_heat_added_kw', 0):.2f} kW")
    print(f"{'Lights Heat:':<22} {outputs.get('light_heat_kw', 0):.2f} kW")
    print(f"{'CHX Heat:':<22} {outputs.get('chx_heat_added_kw', 0):.2f} kW")
    print(f"{'OGA Heat:':<22} {outputs.get('oga_heat_kw', 0):.2f} kW")

    #-----------cooling-------------♡
    print(f"{'Radiators Online:':<22} {outputs.get('radiators_online_count', 0)}")
    print(f"{'Rad Cooling:':<22} {outputs.get('radiator_heat_rejection_kw', 0):.2f} kW")
#----------------------------------------------------♡


#----------------------water-------------------------♡
def print_water(state, outputs):
    print_section_header("WATER")

    #---------humidity / CHX--------♡
    print(f"{'Transpiration:':<22} {outputs.get('transpiration_kg', 0):.3f} kg")
    print(f"{'Humidity:':<22} {outputs.get('new_humidity_pct', state.current_humidity_pct):.2f} %")
    print(f"{'Vapor Removed:':<22} {outputs.get('vapor_removed_kg', 0):.2f} kg")


    #----------greenhouse-----------♡
    print(f"{'Water Needed:':<22} {outputs.get('total_water_needed_kg', 0):.3f} kg")
    print(f"{'Water Used:':<22} {outputs.get('total_water_consumed_kg', 0):.2f} kg")
    print(f"{'Water Recirculated:':<22} {outputs.get('total_water_recirculated_kg', 0):.3f} kg")


    #-------------isru--------------♡

    #----------processing-----------♡
    print(f"{'UPA Black Removed:':<22} {outputs.get('upa_black_water_removed_kg', 0):.2f} kg")
    print(f"{'WPA Processed:':<22} {outputs.get('wpa_water_processed_kg', 0):.2f} kg")
    print(f"{'BPA Processed:':<22} {outputs.get('bpa_water_processed_kg', 0):.2f} kg")
    

    #----------water used-----------♡
    print(f"{'Potable Used:':<22} {outputs.get('potable_water_used_kg', 0):.2f} kg")
    print(f"{'OGA Water Used:':<22} {outputs.get('oga_water_used_kg', 0):.2f} kg")

    #--------water recovered--------♡
    print(f"{'Total Recovered:':<22} {outputs.get('total_recovered_water_kg', 0):.2f} kg")
    print(f"{'UPA Recovered:':<22} {outputs.get('upa_recovered_water_kg', 0):.2f} kg")
    print(f"{'WPA Recovered:':<22} {outputs.get('wpa_recovered_water_kg', 0):.2f} kg")
    print(f"{'BPA Recovered:':<22} {outputs.get('bpa_recovered_water_kg', 0):.2f} kg")

    #----------water added----------♡
    print(f"{'Gray Added:':<22} {outputs.get('gray_water_added_kg', 0):.2f} kg")
    print(f"{'Black Added:':<22} {outputs.get('black_water_added_kg', 0):.2f} kg")
    print(f"{'Condensate Added:':<22} {outputs.get('vapor_removed_kg', 0):.2f} kg")
    print(f"{'Water Produced:':<22} {outputs.get('sabatier_water_produced_kg', 0):.2f} kg")
    print(f"{'UPA Brine Added:':<22} {outputs.get('upa_brine_added_kg', 0):.2f} kg")

    #-----------storage-------------♡
    print(f"{'Potable Water:':<22} {state.potable_water_storage_kg:.2f} kg")
    print(f"{'Gray Water:':<22} {state.gray_water_storage_kg:.2f} kg")
    print(f"{'Black Water:':<22} {state.black_water_storage_kg:.2f} kg")
    print(f"{'Condensate:':<22} {state.condensate_storage_kg:.2f} kg")
    print(f"{'Brine:':<22} {state.brine_storage_kg:.2f} kg")
#----------------------------------------------------♡


#-----------------------dust-------------------------♡
def print_environment(state, outputs):
    print_section_header("DUST")

#----------------------------------------------------♡



#----------------------------------------------------♡

def print_sim(state, outputs):
    ...
#----------------------------------------------------♡


    # print(f"{'Food Produced:':<22} {outputs.get('total_food_produced_kg', 0):.3f} kg")
    # print(f"{'CO2 Stored:':<{lw}}" f"{state.co2_kpa:.3f} kPa + "f"{state.co2_stored_kg:.2f} kg stored")
    # print(f"{'CO2 Consumed:':<{lw}} {outputs.get('total_co2_consumed_kpa', 0):.3f} kPa")
    # print((f"\n♡  [THERMAL MODE: {outputs['hab_temp_mode']}]  ♡\n").center(width))
    # print(f"{'Potable Water:':<{lw}}" f"{state.potable_water_storage_kg:.1f} kg")
    # print(f"Sabatier Water Produced: {outputs.get('sabatier_water_produced_kg', 0):.3f} kg")
