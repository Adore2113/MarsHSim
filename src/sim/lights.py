# file for habitat interior lighting and wellness lights

#--------------------imports---------------------------♡
from .mars_time import get_sol_time, get_sunlight_amount
#------------------------------------------------------♡

#--------------------constants-----------------------♡
#---------main lights----------♡
min_light_level = 0.2

base_light_power_kw = 2.0
base_light_heat_kw = 0.5

#-------wellness lights--------♡
base_w_light_power_kw = 0.5
base_w_light_heat_kw = 0.1
#----------------------------------------------------♡

#-----------habitat main light power info------------♡
def light_system(state, dt_min, power_mode):
    hours_per_step = dt_min / 60.0
    _, sol_hour, minutes = get_sol_time(state)

    sunlight_amount = get_sunlight_amount(state)
    low_sunlight_streak = state.low_sunlight_streak_sols

    #------------------main lights-------------------♡ 
    crew_awake_hours = 6 <= sol_hour < 21 or (sol_hour == 21 and minutes < 30)

    if crew_awake_hours:
        base_light_level = 1.0

    else:
        base_light_level = min_light_level

    sunlight_dimming = sunlight_amount * 0.6    # sunlight level changes light level need for power saving
    light_level_dimmed = base_light_level - sunlight_dimming
    adjusted_light_level = max(min_light_level, light_level_dimmed)

    #----------------wellness lights-----------------♡ 
    if low_sunlight_streak >= 3:
        wellness_lights_on = True
        wellness_light_level = 1.0
    
    elif low_sunlight_streak <= 1:
        wellness_lights_on = False
        wellness_light_level = 0.0
    
    else:
        wellness_lights_on = state.wellness_lights_on
        
        if wellness_lights_on:
            wellness_light_level = 1.0

        else:
            wellness_light_level = 0.0
    
    adjusted_light_level, wellness_light_level = apply_low_power_mode_lights(power_mode, adjusted_light_level, wellness_light_level)

    light_power_used_kw = base_light_power_kw * adjusted_light_level
    light_heat_kw = base_light_heat_kw * adjusted_light_level

    w_light_power_used_kw = base_w_light_power_kw * wellness_light_level
    w_light_heat_kw = base_w_light_heat_kw * wellness_light_level

    #------------total light heat added--------------♡ 
    total_light_heat_kw = light_heat_kw + w_light_heat_kw

    return {
        "adjusted_light_level": adjusted_light_level,
        "light_heat_kw": light_heat_kw,
        "light_heat_kwh": light_heat_kw * hours_per_step,
        "light_power_used_kw": light_power_used_kw,
        "light_energy_used_kwh": light_power_used_kw * hours_per_step,

        "wellness_lights_on": wellness_lights_on,
        "wellness_light_level": wellness_light_level,
        "w_light_power_used_kw": w_light_power_used_kw,
        "w_light_energy_used_kwh": w_light_power_used_kw * hours_per_step,
        "w_light_heat_kw": w_light_heat_kw,
        "w_light_heat_kwh": w_light_heat_kw * hours_per_step,

        "total_light_heat_kw": total_light_heat_kw,
        "total_light_heat_kwh": total_light_heat_kw * hours_per_step,
        }


#------------deciding low power priorites------------♡
def apply_low_power_mode_lights(power_mode, adjusted_light_level, wellness_light_level):
    if power_mode == "low":
        adjusted_light_level = max(0.02, adjusted_light_level * 0.5)
        wellness_light_level = 0.0
    
    elif power_mode == "critical":
        adjusted_light_level = max(0.02, adjusted_light_level * 0.3)
        wellness_light_level = 0.0

    return adjusted_light_level, wellness_light_level