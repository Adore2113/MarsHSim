#--------------------imports-------------------------♡
from .mars_time import get_sol_time
from .buffer_gas import mca
from .alerts import get_status
#----------------------------------------------------♡


#--------------------constants-----------------------♡
width = 33
deco = "\n♡ " + "-" * 30 + " ♡"
split = "-" * width
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



#------------------time / environment----------------♡
def print_environment(state, outputs):
    sol, hour, minutes = get_sol_time(state)
    temp_change_per_hour = outputs.get("temp_change_c", 0) * 12    # change this later


    print(f"{'Sol:':<19} {sol} | {hour:02d}:{minutes:02d} LMST")
    print(f"{'Habitat Temp:':<22} {state.hab_temp_c:.3f} °C")    # change back to 2f
    print(f"{'Mars Temp:':<22} {outputs['mars_temp_c']:.2f} °C")
    print(f"{'Peak Sun Today:':<22} {state.peak_sunlight_today:.3f} /1.0")
    print(f"{'Low Sun Streak:':<22} {state.low_sunlight_streak_sols} sols")
    print(f"{'Sunlight per m²:':<22} {state.daylight_m2_kw:.3f} kW")
#----------------------------------------------------♡


#-------------------system status--------------------♡
def print_system_stats(alerts):
    status = get_status(alerts)
    print_section_header(f"SYSTEM STATUS: {status}")


#--------------------atmosphere----------------------♡
def print_atmosphere(state, outputs):
    print_section_header(atmosphere)

#-----------------------crew-------------------------♡
def print_crew(state, outputs):
    print_section_header(crew)

#--------------------oxygen / oga--------------------♡
def print_oga(state, outputs):
    print_section_header(oxygen / oga)

#--------------------co2 scrubber--------------------♡
def print_co2_scrub(state, outputs):
    print_section_header(co2 scrubber)

#--------------------buffer gas----------------------♡
def print_environment(state, outputs):
    print_section_header(buffer gas)

#-----------------------power------------------------♡
def print_environment(state, outputs):
    print_section_header(power)

#----------------------thermal-----------------------♡
def print_environment(state, outputs):
    print_section_header(thermal)

#-------------------humidity / chx-------------------♡
def print_environment(state, outputs):
    print_section_header(humidity / chx)

#----------------------water-------------------------♡
def print_environment(state, outputs):
    print_section_header(water)

#-----------------------isru-------------------------♡
def print_environment(state, outputs):
    print_section_header(isru)

#---------------------sabatier-----------------------♡
def print_environment(state, outputs):
    print_section_header(sabatier)

#--------------------greenhouse----------------------♡
def print_environment(state, outputs):
    print_section_header(greenhouse)

#-----------------------dust-------------------------♡
def print_environment(state, outputs):
    print_section_header(dust)

#----------------------alerts------------------------♡
def print_environment(state, outputs):
    print_section_header(alerts)


def print_sim(state, outputs):
    ...