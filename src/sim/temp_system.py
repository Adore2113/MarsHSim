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
def determine_mars_temp_c(state):
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
    mars_temp_c = base_temp_c + temp_offset
    
    return mars_temp_c


#------passive heat loss to outside environment------♡
def heat_loss_from_outside_kw(state, mars_temp_c):
    temp_difference_c = state.hab_temp_c - mars_temp_c

    heat_loss_kw = temp_difference_c * state.insulation_strength_kw_per_c
    
    return heat_loss_kw


#---------------electric heater system---------------♡


#-------------which radiators are online-------------♡
def radiators_online(radiators, cabin_temp_c, target_temp_c, max_temp_c):
    new_radiators = []
    radiatiors_online_count = sum(1 for rad in radiators if rad["status"] == "online")

    if cabin_temp_c >= max_temp_c:
        target_online_count = 6

    elif cabin_temp_c > target_temp_c:
        target_online_count = 3
    
    else:
        target_online_count = 0

    for rad in radiators:
        new_radiators = radiators.copy()

        if radiators_online_count < target_online_count and new_radiators["status"] == "standby":
            new_radiators["status"] = "online"
            radiators_online_count += 1

        elif radiators_online_count > target_online_count and new_radiators["status"] == "online":
            new_radiators["status"] = "standby"
            radiators_online_count -= 1

        new_radiators.append(new_radiators)

    return new_radiators, radiators_online_count


#--------------radiatior cooling system--------------♡
def radiator_heat_rejection_kw(state, mars_temp_k):
    total_rejection_kw = 0.0
    stefan_boltzmann_const = 5.67e-8
    cabin_temp_k = state.cabin_temp_c + 273.15 

    for rad in state.radiators:
        ...

#----------condensing heat exchanger (CHX)-----------♡
     # focusing on temp first


#------running thermal control for one timestep------♡
def run_thermal_control(state, outputs, dt_min):
    hours_per_step = dt_min / 60.0

    hab_heat_kw = heat_from_outputs_kw(outputs)
    mars_temp_c = determine_mars_temp_c(state)
    
    heat_loss_kw = heat_loss_from_outside_kw(state, mars_temp_c)

    net_heat_kw = hab_heat_kw - heat_loss_kw

    temp_change_c = (net_heat_kw * hours_per_step) / state.thermal_mass_kwh_per_c
    
    new_hab_temp_c = state.hab_temp_c + temp_change_c

#---------temp alerts ( move to alerts.py? )---------♡
    thermal_alerts = []
    if new_hab_temp_c > 28.0:
        thermal_alerts.append("CRITICAL: Cabin too hot")
    
    elif new_hab_temp_c < 18.0:
        thermal_alerts.append("CRITICAL: Cabin too cold")

    return {
        "new_hab_temp_c": new_hab_temp_c,
        "mars_temp_c": mars_temp_c,
        "hab_heat_kw": hab_heat_kw,
        "heat_loss_kw": heat_loss_kw,
        "thermal_alerts": thermal_alerts,
        "net_heat_kw": net_heat_kw,
        "temp_change_c": temp_change_c,
        }