from dataclasses import replace
from .state import Habitat_State
from .mars_time import current_mars_season, determine_sunlight_amount

# file for temperature and humidity

#--------------------constants-----------------------♡
target_temp_c = 23.0
min_temp_c = 20.0
max_temp_c = 25.0

target_humidity_pct = 48.0
water_vapor_per_m3 = 0.0008

kelvin_offset = 273.15   # add to celsius to convert to kelvin
stefan_boltzmann_const = 5.67e-8

sunlight_heat_gain_fraction = 0.65    # PLACEHOLDER!
radiator_heat_gain_fraction = 0.30    # ^ placeholder
max_daylight_m2_kw = 0.57
sunlight_facing_hab_m2 = 45.0    # another placeholder
#---------------------------------------------------♡


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
        base_temp_c = -15
        day_night_variation = 12.0
    
    else:
        base_temp_c = -25.0
        day_night_variation = 10.0

    temp_offset = (sunlight - 0.5) * 2 * day_night_variation
    mars_temp_c = base_temp_c + temp_offset
    mars_temp_k = mars_temp_c + kelvin_offset

    return mars_temp_c, mars_temp_k


#-------------sunlight the habitat absorbs-----------♡
def get_solar_heat_gain_kw(state, sunlight_amount):
    effective_area_m2 = sunlight_facing_hab_m2 * state.solar_absorptivity
    transmittance = 0.75    # how much heat gets through
    
    sunlight_per_m2_kw= sunlight_amount * max_daylight_m2_kw * 1.0
    solar_heat_gain_kw = sunlight_per_m2_kw * effective_area_m2 * transmittance * sunlight_heat_gain_fraction

    return solar_heat_gain_kw


#------passive heat loss to outside environment------♡
def heat_loss_from_outside_kw(state, mars_temp_c):
    temp_difference_c = state.hab_temp_c - mars_temp_c

    heat_loss_kw = temp_difference_c * state.insulation_strength_kw_per_c
    
    return heat_loss_kw


#--------------which heaters are online--------------♡
def heaters_online(heaters, hab_temp_c, target_temp_c):
    new_heaters = []
    heaters_online_count = sum(1 for heater in heaters if heater["status"] == "online")
    hysteresis_c = 0.15

    heater_stages = [target_temp_c - 0.3, target_temp_c - 0.6, target_temp_c - 0.9, target_temp_c - 1.2, target_temp_c - 1.5, target_temp_c - 1.8,]

    target_online_count = heaters_online_count

    if heaters_online_count < len(heater_stages):
        next_heater_on_temp_c = heater_stages[heaters_online_count]

        if hab_temp_c <= next_heater_on_temp_c:
            target_online_count += 1

    if heaters_online_count > 0:
        next_heater_off_temp_c = heater_stages[heaters_online_count - 1] + hysteresis_c

        if hab_temp_c > next_heater_off_temp_c:
            target_online_count -= 1

    for heater in heaters:
        new_heater = heater.copy()

        if heaters_online_count < target_online_count and new_heater["status"] == "standby":
                new_heater["status"] = "online"
                heaters_online_count += 1

        elif heaters_online_count > target_online_count and new_heater["status"] == "online":
                new_heater["status"] = "standby"
                heaters_online_count -= 1

        new_heaters.append(new_heater)

    return new_heaters, heaters_online_count


#---------------electric heater system---------------♡
def heater_heat_added_kw(new_heaters):
    total_heater_heat_kw = 0.0

    for heater in new_heaters:
        if heater["status"] == "online":
            heater_output_kw = heater["power_kw"] * heater["efficiency"]
            total_heater_heat_kw += heater_output_kw

    return total_heater_heat_kw


#--------------heater power consumption--------------♡
def heater_power(new_heaters, dt_min):
    hours_per_step = dt_min / 60
    heater_power_kw = 0.0

    for heater in new_heaters:
        if heater["status"] == "online":
            heater_power_kw += heater["power_kw"]

    heater_energy_kwh = heater_power_kw * hours_per_step

    return heater_power_kw, heater_energy_kwh


#-------------which radiators are online-------------♡
def radiators_online(radiators, hab_temp_c, target_temp_c):
    new_radiators = []
    radiators_online_count = sum(1 for rad in radiators if rad["status"] == "online")
    hysteresis_c = 0.15

    radiator_stages = [target_temp_c + 0.3, target_temp_c + 0.6, target_temp_c + 0.9, target_temp_c + 1.2, target_temp_c + 1.5, target_temp_c + 1.8,]
    
    target_online_count = radiators_online_count

    if radiators_online_count < len(radiator_stages):
        next_rad_on_temp_c = radiator_stages[radiators_online_count]

        if hab_temp_c >= next_rad_on_temp_c:
            target_online_count += 1
    
    if radiators_online_count > 0:
        next_rad_off_temp_c = radiator_stages[radiators_online_count - 1] - hysteresis_c

        if hab_temp_c < next_rad_off_temp_c:
            target_online_count -= 1

    max_radiators_online_count = 6
    target_online_count = min(target_online_count, max_radiators_online_count)

    for rad in radiators:
        new_radiator = rad.copy()

        if radiators_online_count < target_online_count and new_radiator["status"] == "standby":
            new_radiator["status"] = "online"
            radiators_online_count += 1

        elif radiators_online_count > target_online_count and new_radiator["status"] == "online":
            new_radiator["status"] = "standby"
            radiators_online_count -= 1

        new_radiators.append(new_radiator)

    return new_radiators, radiators_online_count


#--------------radiatior cooling system--------------♡
def rad_heat_rejection_kw(state, mars_temp_k, new_radiators):
    total_rejection_kw = 0.0
    sb_const = stefan_boltzmann_const
    hab_temp_k = state.hab_temp_c + kelvin_offset 

    for rad in new_radiators:
        if rad["status"] == "online":
            covered_area_m2 = rad["area_m2"] * rad["dust_factor"]
            rad_efficiency = rad["efficiency"]
            
            rad_temp_difference = hab_temp_k ** 4 - mars_temp_k ** 4

            heat_rejected_w = rad_efficiency * sb_const * covered_area_m2 * rad_temp_difference
            total_rejection_kw += heat_rejected_w / 1000.0

    return max(0.0, total_rejection_kw)
    

#-------------radiator power consumption-------------♡
def radiator_power(radiators_online_count, dt_min):
    hours_per_step = dt_min / 60
    power_per_radiator_kw = 0.08

    radiator_power_kw = radiators_online_count * power_per_radiator_kw
    radiator_energy_kwh = radiator_power_kw * hours_per_step
    
    return radiator_power_kw, radiator_energy_kwh
    

#---------determine the habitat thermal mode---------♡
def determine_thermal_mode(state, hab_temp_c, target_temp_c):
    hab_temp_mode = "neutral"
    new_heaters, heaters_online_count = heaters_online(state.heaters, state.hab_temp_c, target_temp_c)
    new_radiators, radiators_online_count = radiators_online(state.radiators, state.hab_temp_c, target_temp_c)

    if heaters_online_count > 0:
        new_radiators = []

        for rad in state.radiators:
            new_rad = rad.copy()
            new_rad["status"] = "standby"
            new_radiators.append(new_rad)

        radiators_online_count = 0
    
    elif radiators_online_count > 0:
        new_heaters = []
        
        for heater in state.heaters:
            new_heater = heater.copy()
            new_heater["status"] = "standby"
            new_heaters.append(new_heater)

        heaters_online_count = 0
    
    if heaters_online_count > 0:
        hab_temp_mode = "Heating Mode"

    elif radiators_online_count > 0:
        hab_temp_mode = "Cooling Mode"

    elif hab_temp_c < target_temp_c:
        hab_temp_mode = "Below Target"

    elif hab_temp_c > target_temp_c:
        hab_temp_mode = "Above Target"

    else:
        hab_temp_mode = "Neutral"
    
    return hab_temp_mode, new_heaters, heaters_online_count, new_radiators, radiators_online_count


#------running thermal control for one timestep------♡
def run_thermal_control(state, crew_heat_kw, oga_heat_kw, co2_scrubber_heat_kw, light_heat_kw, wellness_light_heat_kw, chx_heat_added_kw, dt_min, sunlight_amount):
    hours_per_step = dt_min / 60.0
    hab_heat_kw = crew_heat_kw + oga_heat_kw + co2_scrubber_heat_kw + light_heat_kw + wellness_light_heat_kw + chx_heat_added_kw
    mars_temp_c, mars_temp_k = determine_mars_temp_c(state)
    
    if sunlight_amount is None:
        sunlight_amount = determine_sunlight_amount(state)

    solar_heat_gain_kw = get_solar_heat_gain_kw(state, sunlight_amount)
    
    hab_temp_mode, new_heaters, heaters_online_count, new_radiators, radiators_online_count = determine_thermal_mode(state, state.hab_temp_c, target_temp_c)

    heat_loss_kw = heat_loss_from_outside_kw(state, mars_temp_c)
    
    heater_heat_kw = heater_heat_added_kw(new_heaters)
    heater_power_kw, heater_energy_kwh = heater_power(new_heaters, dt_min)

    radiator_heat_rejection_kw = rad_heat_rejection_kw(state, mars_temp_k, new_radiators)
    radiator_power_kw, radiator_energy_kwh = radiator_power(radiators_online_count, dt_min)

    net_heat_kw = hab_heat_kw + heater_heat_kw  + solar_heat_gain_kw - heat_loss_kw - radiator_heat_rejection_kw
    temp_change_c = (net_heat_kw * hours_per_step) / state.thermal_mass_kwh_per_c
    
    new_hab_temp_c = state.hab_temp_c + temp_change_c

    return {
        "new_hab_temp_c": new_hab_temp_c,
        "mars_temp_c": mars_temp_c,
        "hab_heat_kw": hab_heat_kw,
        "solar_heat_gain_kw" : solar_heat_gain_kw,
        "heat_loss_kw": heat_loss_kw,
        "radiator_heat_rejection_kw": radiator_heat_rejection_kw,
        "radiators_online_count": radiators_online_count,
        "radiator_power_kw": radiator_power_kw,
        "radiator_energy_kwh": radiator_energy_kwh,
        "new_radiators": new_radiators,
        "heater_heat_kw": heater_heat_kw,
        "heaters_online_count": heaters_online_count,
        "heater_power_kw": heater_power_kw,
        "heater_energy_kwh": heater_energy_kwh,
        "new_heaters": new_heaters,
        "thermal_alerts": hab_temp_mode,
        "net_heat_kw": net_heat_kw,
        "temp_change_c": temp_change_c,
        "hab_temp_mode" : hab_temp_mode
        }


#---------------------temp alerts--------------------♡
def get_thermal_alerts(new_hab_temp_c):
    thermal_alerts = []
    
    if new_hab_temp_c > 28.0:
        thermal_alerts.append("CRITICAL: Habitat too hot")
    
    elif new_hab_temp_c < 18.0:
        thermal_alerts.append("CRITICAL: Habitat too cold")

    return thermal_alerts


#-------chx power consumption and heat produced------♡
def chx_power_and_heat(vapor_removed_kg, dt_min):
    hours_per_step = dt_min / 60.0

    chx_heat_added_kw = 0.0
    chx_heat_added_kwh = 0.0
    chx_power_used_kw = 0.0
    chx_energy_used_kwh = 0.0

    if vapor_removed_kg > 0.0:
        chx_power_used_kw = 0.35
        chx_energy_used_kwh = chx_power_used_kw * hours_per_step

        chx_heat_added_kw = 0.20
        chx_heat_added_kwh = chx_heat_added_kw * hours_per_step

    return chx_heat_added_kw, chx_heat_added_kwh, chx_power_used_kw, chx_energy_used_kwh


#----------condensing heat exchanger (CHX)-----------♡
def update_humidity(state, breath_vapor_added_kg, skin_vapor_added_kg, dt_min):
    hours_per_step = dt_min / 60.0
    chx_removal_efficiency = 0.85
    
    total_vapor_added_kg = breath_vapor_added_kg + skin_vapor_added_kg
    vapor_per_pct_kg = (water_vapor_per_m3 * state.hab_vol_m3) / 100.0
    
    target_vapor_kg = state.target_humidity_pct * vapor_per_pct_kg

    current_vapor_kg = (state.current_humidity_pct * vapor_per_pct_kg) + total_vapor_added_kg
    excess_vapor_kg = max(0.0, current_vapor_kg - target_vapor_kg)

    vapor_removed_kg = excess_vapor_kg * chx_removal_efficiency

    new_vapor_kg = current_vapor_kg - vapor_removed_kg
    new_humidity_pct = new_vapor_kg / vapor_per_pct_kg
    new_humidity_pct = max(20.0, min(80.0, new_humidity_pct))
    
    chx_heat_added_kw, chx_heat_added_kwh, chx_power_used_kw, chx_energy_used_kwh = chx_power_and_heat(vapor_removed_kg, dt_min)

    return {
        "new_humidity_pct": new_humidity_pct,
        "vapor_added_kg": total_vapor_added_kg,
        "vapor_removed_kg": vapor_removed_kg,
        "target_vapor_kg": target_vapor_kg,
        "new_vapor_kg": new_vapor_kg,
        "chx_heat_added_kw": chx_heat_added_kw,
        "chx_heat_added_kwh": chx_heat_added_kwh,
        "chx_power_used_kw": chx_power_used_kw,
        "chx_energy_used_kwh": chx_energy_used_kwh
    } 


#------------------humidity alerts-------------------♡
def get_humidity_alerts(new_humidity_pct):
    humidity_alerts = []

    if new_humidity_pct < 20.0:
        humidity_alerts.append("CRITICAL: Habitat humidity too low")

    elif new_humidity_pct < 30.0:
        humidity_alerts.append("WARNING: Habitat humidity low")

    if new_humidity_pct > 70.0:
        humidity_alerts.append("CRITICAL: Habitat humidity too high")

    elif new_humidity_pct > 60.0:
        humidity_alerts.append("WARNING: Habitat humidity high")

    return humidity_alerts
