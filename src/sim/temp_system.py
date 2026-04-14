from dataclasses import replace
from .state import Habitat_State

# file for temperature and humidity

#--------------------constants-----------------------♡
target_temp_c = 23.0
min_temp_c = 20.0
max_temp_c = 25.0
#----------------------------------------------------♡


#------------get total heat from outputs-------------♡
def heat_from_outputs_kw(outputs):
    return (
        outputs.get("crew_heat_kw", 0.0)
        + outputs.get("oga_heat_kw", 0.0)
        + outputs.get("co2_scrubber_heat_kw", 0.0)
        + outputs.get("lights_heat_kw", 0.0)
        + outputs.get("buffer_gas_heat_kw", 0.0)
    ) 

#----------------get total humidity------------------♡


#---------------internal temp system-----------------♡
#----------------------radiators---------------------♡
#------------------electric heaters------------------♡


#--------------external Mars environment-------------♡


#--------------seasonal/weather changes--------------♡


#-------calculate total temp changes generated-------♡


#------------------run_temp_system-------------------♡
