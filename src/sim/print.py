#--------------------imports-------------------------♡
from .mars_time import get_sol_time
from .buffer_gas import mca
from .alerts import get_status
#----------------------------------------------------♡


#--------------------constants-----------------------♡
width = 33
deco = "\n♡ " + "-" * 30 + " ♡"
split = "-" * width
left_split = "⋙" * 5
right_split = "⋘" * 5
#----------------------------------------------------♡


#----------------------header------------------------♡
def print_header():
    print(deco)
    print("Adore2113's MarsHSim".center(width))
    print(deco)
#----------------------------------------------------♡

#-------------------section header-------------------♡
def print_section_header(title):
    print(f"\n{left_split}  {title}  {right_split}")
#----------------------------------------------------♡

#------------------time / environment----------------♡
def environment(state, outputs):
    print(f"{'Sol:':<19} {sol} | {hour:02d}:{minutes:02d} LMST")
    print(f"{'Habitat Temp:':<22} {state.hab_temp_c:.3f} °C")    # change back to 2f
    print(f"{'Mars Temp:':<22} {outputs['mars_temp_c']:.2f} °C")
    print(f"{'Peak Sun Today:':<22} {state.peak_sunlight_today:.3f} /1.0")
    print(f"{'Low Sun Streak:':<22} {state.low_sunlight_streak_sols} sols")
    print(f"{'Sunlight per m²:':<22} {state.daylight_m2_kw:.3f} kW")
    

#-------------------system status--------------------♡
def environment(state, outputs):
    print_section_header(system status)

  
#------------------time / environment----------------♡
def environment(state, outputs):
    print_section_header(time / environment)

#--------------------atmosphere----------------------♡
def environment(state, outputs):
    print_section_header(atmosphere)

#-----------------------crew-------------------------♡
def environment(state, outputs):
    print_section_header(crew)

#--------------------oxygen / oga--------------------♡
def environment(state, outputs):
    print_section_header(oxygen / oga)

#--------------------co2 scrubber--------------------♡
def environment(state, outputs):
    print_section_header(co2 scrubber)

#--------------------buffer gas----------------------♡
def environment(state, outputs):
    print_section_header(buffer gas)

#-----------------------power------------------------♡
def environment(state, outputs):
    print_section_header(power)

#----------------------thermal-----------------------♡
def environment(state, outputs):
    print_section_header(thermal)

#-------------------humidity / chx-------------------♡
def environment(state, outputs):
    print_section_header(humidity / chx)

#----------------------water-------------------------♡
def environment(state, outputs):
    print_section_header(water)

#-----------------------isru-------------------------♡
def environment(state, outputs):
    print_section_header(isru)

#---------------------sabatier-----------------------♡
def environment(state, outputs):
    print_section_header(sabatier)

#--------------------greenhouse----------------------♡
def environment(state, outputs):
    print_section_header(greenhouse)

#-----------------------dust-------------------------♡
def environment(state, outputs):
    print_section_header(dust)

#----------------------alerts------------------------♡
def environment(state, outputs):
    print_section_header(alerts)


def print_sim(state, outputs):
    ...