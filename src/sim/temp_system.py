from dataclasses import replace
from .state import Habitat_State
from .mars_time import current_mars_season, determine_sunlight_amount

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
        + outputs.get("light_heat_kw", 0.0)
        + outputs.get("buffer_gas_heat_kw", 0.0)
    ) 

#----------------get total humidity------------------♡
    # focusing on temp first


#--------------external Mars environment-------------♡
def determine_outside_temp_c(state):
    season = current_mars_season(state)
    sunlight = determine_sunlight_amount(state)

    if season == "north_spring":
        base_temp_c = -10.0
        day_night_variation = 12.0

    elif season == "north_summer":
        base_temp_c = 0.0
        day_night_variation = 15.0
    
    elif season == "north_autumn":
        base_temp_c = -12.5
        day_night_variation = 12.0
    
    else:
        base_temp_c = -20.0
        day_night_variation = 10.0

    temp_offset = (sunlight - 0.5) * 2 * day_night_variation
    outside_temp_c = base_temp_c + temp_offset
    
    return outside_temp_c


#------passive heat loss to outside environment------♡
def heat_loss_from_outside_kw(state, outside_temp_c):
    temp_difference_c = state.hab_temp_c - outside_temp_c

    if temp_difference_c <= 0:
        return 0.0
    
    heat_loss_kw = temp_difference_c * state.insulation_strength_kw_per_c
    
    return heat_loss_kw

#------running thermal control for one timestep------♡
def run_thermal_control(state, outputs, dt_min):
    hours_per_step = dt_min / 60.0

    internal_heat_kw = heat_from_outputs_kw(outputs)
    outside_temp_c = determine_outside_temp_c(state)
    
    heat_loss_kw = heat_loss_from_outside_kw(state, outside_temp_c)

    net_heat_kw = internal_heat_kw - heat_loss_kw

    temp_change_c = (net_heat_kw * hours_per_step) / state.thermal_mass_kwh_per_c
    
    new_hab_temp_c = state.hab_temp_c + temp_change_c

#---------temp alerts ( move to alerts.py? )---------♡
    thermal_alerts = []
    if new_hab_temp_c > 28.0:
        thermal_alerts.append("CRITICAL: Cabin too hot")
    
    elif new_hab_temp_c < 18.0:
        thermal_alerts.append("CRITICAL: Cabin too cold")

    return {
        "new_hab_temp_c": round(new_hab_temp_c, 2),
        "outside_temp_c": round(outside_temp_c, 2),
        "internal_heat_kw": round(internal_heat_kw, 2),
        "heat_loss_kw": round(heat_loss_kw, 2),
        "thermal_alerts": thermal_alerts,
        "net_heat_kw": round(net_heat_kw, 2),
        "temp_change_c": round(temp_change_c, 2),
        }