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

    print(f"{'Peak Sun Today:':<{lw}} {state.peak_sunlight_today:.3f} /1.0")
    print(f"{'Low Sun Streak:':<{lw}} {state.low_sunlight_streak_sols} sols")

    print(f"{'Sunlight per m²:':<{lw}} {state.daylight_m2_kw:.3f} kW")
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
    
    #----------stored gas----------♡
    print(f"{'O2 Stored:':<{lw}} {state.o2_stored_kg:.2f} kg")
    print(f"{'CO2 Stored:':<{lw}} {state.h2_stored_kg:.2f} kg")
    print(f"{'N2 Stored:':<{lw}} {state.h2_stored_kg:.2f} kg")
    print(f"{'AR Stored:':<{lw}} {state.h2_stored_kg:.2f} kg")

    print(f"{'H2 Stored:':<{lw}} {state.h2_stored_kg:.2f} kg")
    print(f"{'CH4 Stored:':<{lw}} {state.ch4_stored_kg:.2f} kg")    
    
    #-----------gas moved-----------♡
    print(f"{'CO2 Consumed:':<{lw}} {outputs.get('sabatier_co2_consumed_kpa', 0):.3f} kPa")
    print(f"{'CO2 Scrubbed:':<{lw}} {outputs.get('co2_removed_kpa', 0):.3f} kPa")

    print(f"{'O2 Added:':<{lw}} {outputs.get('o2_added_kpa', 0):.3f} kPa")

    print(f"{'CH4 Produced:':<{lw}} {outputs.get('sabatier_ch4_produced_kg', 0):.2f} kg")
    print(f"{'CH4 Vented:':<{lw}} {outputs.get('sabatier_ch4_vented_kg', 0):.2f} kg")
    print(f"{'H2 Consumed:':<{lw}} {outputs.get('sabatier_h2_consumed_kg', 0):.2f} kg")
    print(f"{'O2 Produced:':<{lw}} {outputs.get('total_o2_produced_kpa', 0):.3f} kPa")

    #------buffer gas control------♡
    print(f"{'Buffer Gas Mode:':<{lw}} {outputs['buffer_gas_mode']}")
    print(f"{'Pressure Gap:':<{lw}} {outputs['pressure_gap_kpa']:.3f} kPa")
    
    print(f"{'Gas Added:':<{lw}} {outputs['total_buffer_gas_added_kpa']:.3f} kPa")
    print(f"{'Gas Vented:':<{lw}} {outputs.get('total_buffer_gas_vented_kpa', 0.0):.3f} kPa")

#----------------------------------------------------♡



#--------------------oxygen / oga--------------------♡
def print_oga(state, outputs):
    print_section_header("OXYGEN / OGA")

#--------------------co2 scrubber--------------------♡
def print_co2_scrub(state, outputs):
    print_section_header("CO2 SCRUBBER")

#--------------------buffer gas----------------------♡
def print_environment(state, outputs):
    print_section_header("BUFFER GAS")

#-----------------------power------------------------♡
def print_environment(state, outputs):
    print_section_header("POWER")

#----------------------thermal-----------------------♡
def print_environment(state, outputs):
    print_section_header("THERMAL")
    print(f"{'OGA Heat:':<22} {outputs.get('oga_heat_kw', 0):.2f} kW")



#-------------------humidity / chx-------------------♡
def print_environment(state, outputs):
    print_section_header("HUMIDITY / CHX")

#----------------------water-------------------------♡
def print_environment(state, outputs):
    print_section_header("WATER")

    print(f"{'Potable Water:':<{lw}}" f"{state.potable_water_storage_kg:.1f} kg")


#-----------------------isru-------------------------♡
def print_environment(state, outputs):
    print_section_header("ISRU")

#---------------------sabatier-----------------------♡
def print_environment(state, outputs):
    print_section_header("SABATIER")

#--------------------greenhouse----------------------♡
def print_environment(state, outputs):
    print_section_header("GREENHOUSE")

#-----------------------dust-------------------------♡
def print_environment(state, outputs):
    print_section_header("DUST")

#----------------------alerts------------------------♡
def print_environment(state, outputs):
    print_section_header("ALERTS")


def print_sim(state, outputs):
    ...



       #  print(f"{'CO2 Stored:':<{lw}}" f"{state.co2_kpa:.3f} kPa + "f"{state.co2_stored_kg:.2f} kg stored")
    #print(f"{'CO2 Consumed:':<{lw}} {outputs.get('total_co2_consumed_kpa', 0):.3f} kPa")
