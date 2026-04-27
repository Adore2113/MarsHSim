#--------------------imports-------------------------♡
from .mars_time import current_mars_season, determine_sunlight_amount
#----------------------------------------------------♡

# file for temperature and humidity

#--------------------constants-----------------------♡
max_radiators_online = 7
max_heaters_online = 6
default_radiator_emission = 0.90

kelvin_offset = 273.15   # add to celsius to convert to kelvin
w_per_kw = 1000.0   # watts to kilowatts
stefan_boltzmann_const = 5.67e-8

max_daylight_m2_kw = 0.59
sunlight_facing_hab_m2 = 48.0

base_chx_power_kw = 0.35
base_chx_waste_heat_fraction = 0.60
chx_removal_efficiency = 0.85
condensation_heat_kj_per_kg = 2260.0
water_vapor_per_m3 = 0.0008

hysteresis_c = 0.5
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
        base_temp_c = -15.0
        day_night_variation = 12.0
    
    else:
        base_temp_c = -25.0
        day_night_variation = 10.0

    temp_offset = (sunlight - 0.5) * 2 * day_night_variation
    mars_temp_c = base_temp_c + temp_offset
    mars_temp_k = mars_temp_c + kelvin_offset

    return mars_temp_c, mars_temp_k


#------------------solar heat gain-------------------♡
def get_solar_heat_gain_kw(state):
    effective_area_m2 = sunlight_facing_hab_m2 * state.solar_absorptivity
    transmittance = 0.75    # fraction of how much heat gets through
    
    solar_heat_gain_kw = state.daylight_m2_kw * effective_area_m2 * transmittance
    
    return solar_heat_gain_kw


#------------------passive heat loss-----------------♡
def heat_loss_from_outside_kw(state):
    temp_difference_c = state.hab_temp_c - state.mars_temp_c

    heat_loss_kw = temp_difference_c * state.insulation_strength_kw_per_c
    
    return heat_loss_kw


#----------------------heaters-----------------------♡
def heaters_online(state):
    new_heaters = []
    heaters_online_count = 0

    heat_needed_c = state.target_temp_c - state.hab_temp_c
   
    #--------how many heaters needed online----------♡ 
    if heat_needed_c > (2.0 + hysteresis_c):
        target_heaters_online =  max_heaters_online
    
    elif heat_needed_c > (1.2 + hysteresis_c):
        target_heaters_online = 5
    
    elif heat_needed_c > (0.5 + hysteresis_c):
        target_heaters_online = 3
    
    elif heat_needed_c > (0.2 + hysteresis_c):
        target_heaters_online = 2
    
    else:
        target_heaters_online = 0

    #-------handling primary radiators first--------♡ 
    primary_heaters_needed = target_heaters_online

    for heater in state.heaters:
        new_heater = heater.copy()

        if new_heater["status"] == "standby" and primary_heaters_needed > 0:
            if new_heater["type"] == "primary":
                new_heater["status"] = "online"
                primary_heaters_needed -= 1
            
            elif new_heater["type"] == "backup" and primary_heaters_needed <= 2:
                new_heater["status"] = "online"

    #---------------switch to standby---------------♡ 
        elif new_heater["status"] == "online":
            if heaters_online_count >= target_heaters_online:
                
                if new_heater["type"] == "backup" or heaters_online_count > 2:
                    new_heater["status"] = "standby"

        if new_heater["status"] == "online":
            heaters_online_count += 1

        new_heaters.append(new_heater)

    return new_heaters, heaters_online_count


#----------------heater heat produced----------------♡
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


#---------------------radiators----------------------♡
def radiators_online(state):
    new_radiators = []
    radiators_online_count = 0

    cooling_needed_c = state.hab_temp_c - state.target_temp_c

    #---------how many heaters needed online---------♡ 
    if cooling_needed_c > (2.0 + hysteresis_c):
        target_online = max_radiators_online
    
    elif cooling_needed_c > (1.2 + hysteresis_c):
        target_online = 6
    
    elif cooling_needed_c > (0.6 + hysteresis_c):
        target_online = 4
    
    elif cooling_needed_c > (0.2 + hysteresis_c):
        target_online = 2
    
    else:
        target_online = 0

    primary_radiators_needed = target_online
    
    #----------handling primary beds first----------♡ 
    for rad in state.radiators:
        new_rad = rad.copy()

        if new_rad["status"] == "standby" and primary_radiators_needed > 0:
            if new_rad["type"] == "primary":
                new_rad["status"] = "online"
                primary_radiators_needed -= 1
            
            elif new_rad["type"] == "backup" and primary_radiators_needed <= 2:
                new_rad["status"] = "online"

    #---------------switch to standby---------------♡ 
        elif new_rad["status"] == "online":
            if radiators_online_count >= target_online:
                if new_rad["type"] == "backup" or radiators_online_count > 2:
                    new_rad["status"] = "standby"

        if new_rad["status"] == "online":
            radiators_online_count += 1

        new_radiators.append(new_rad)

    return new_radiators, radiators_online_count


#----------------radiatior cooling-------------------♡
def rad_heat_rejection_kw(state, mars_temp_k, new_radiators):
    total_rejection_kw = 0.0
    sb_const = stefan_boltzmann_const
    hab_temp_k = state.hab_temp_c + kelvin_offset 

    for rad in new_radiators:
        if rad["status"] == "online":
            covered_area_m2 = rad["area_m2"] * rad["dust_factor"]
            
            effective_emission = default_radiator_emission * rad["efficiency"]
            
            rad_temp_difference = hab_temp_k ** 4 - mars_temp_k ** 4

            heat_rejected_w = effective_emission * sb_const * covered_area_m2 * rad_temp_difference
            total_rejection_kw += heat_rejected_w / w_per_kw

    return max(0.0, total_rejection_kw)
    

#-------------radiator power consumption-------------♡
def radiator_power(radiators_online_count, dt_min):
    hours_per_step = dt_min / 60
    power_per_radiator_kw = 0.08

    radiator_power_kw = radiators_online_count * power_per_radiator_kw
    radiator_energy_kwh = radiator_power_kw * hours_per_step
    
    return radiator_power_kw, radiator_energy_kwh
    

#-----------determine habitat thermal mode-----------♡
def determine_thermal_mode(state, heat_loss_kw, hab_heat_kw, solar_heat_gain_kw):
    new_heaters, heaters_online_count = heaters_online(state)
    new_radiators, radiators_online_count = radiators_online(state)

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
    
    temp_without_heaters_c = hab_heat_kw + solar_heat_gain_kw - heat_loss_kw

    if temp_without_heaters_c < -5.0 and heaters_online_count == 0:
        for new_heater in new_heaters:
            if new_heater["status"] == "standby":
                new_heater["status"] = "online"
                heaters_online_count += 1
                
                break

    if heaters_online_count > 0:
        hab_temp_mode = "Heating"

    elif radiators_online_count > 0:
        hab_temp_mode = "Cooling"

    elif state.hab_temp_c < state.target_temp_c - hysteresis_c:
        hab_temp_mode = "Below Target"

    elif state.hab_temp_c > state.target_temp_c + hysteresis_c:
        hab_temp_mode = "Above Target"

    else:
        hab_temp_mode = "Neutral"

    return hab_temp_mode, new_heaters, heaters_online_count, new_radiators, radiators_online_count


#------running thermal control for one timestep------♡
def run_thermal_control(state, crew_heat_kw, oga_heat_kw, co2_scrubber_heat_kw, light_heat_kw, wellness_light_heat_kw, chx_heat_added_kw, dt_min, sunlight_amount):
    hours_per_step = dt_min / 60.0
    mars_temp_c, mars_temp_k = determine_mars_temp_c(state)

    hab_heat_kw = crew_heat_kw + oga_heat_kw + co2_scrubber_heat_kw + light_heat_kw + wellness_light_heat_kw + chx_heat_added_kw

    if sunlight_amount is None:
        sunlight_amount = determine_sunlight_amount(state)

    solar_heat_gain_kw = get_solar_heat_gain_kw(state)
    
    heat_loss_kw = heat_loss_from_outside_kw(state)
    
    hab_temp_mode, new_heaters, heaters_online_count, new_radiators, radiators_online_count = determine_thermal_mode(state, heat_loss_kw, hab_heat_kw, solar_heat_gain_kw)
    
    heat_loss_kw = heat_loss_from_outside_kw(state)
    
    heater_heat_kw = heater_heat_added_kw(new_heaters)
    heater_power_kw, heater_energy_kwh = heater_power(new_heaters, dt_min)

    radiator_heat_rejection_kw = rad_heat_rejection_kw(state, mars_temp_k, new_radiators)
    radiator_power_kw, radiator_energy_kwh = radiator_power(radiators_online_count, dt_min)

    net_heat_kw = hab_heat_kw + heater_heat_kw  + solar_heat_gain_kw - heat_loss_kw - radiator_heat_rejection_kw
    temp_change_c = (net_heat_kw * hours_per_step) / state.thermal_mass_kwh_per_c
    
    new_hab_temp_c = state.hab_temp_c + temp_change_c

    #----------------dict for updates----------------♡ 
    thermal_updates = {
        "hab_temp_c": new_hab_temp_c,
        "mars_temp_c": mars_temp_c,
        "heaters": new_heaters,
        "radiators": new_radiators,
    }
    
    #-----------dict for printing outputs------------♡ 
    thermal_outputs = {
        "mars_temp_c": mars_temp_c,

        "solar_heat_gain_kw" : solar_heat_gain_kw,
        "heat_loss_kw": heat_loss_kw,
        
        "radiator_heat_rejection_kw": radiator_heat_rejection_kw,
        "radiators_online_count": radiators_online_count,
        "radiator_power_kw": radiator_power_kw,
        "radiator_energy_kwh": radiator_energy_kwh,
        
        "heater_heat_kw": heater_heat_kw,
        "heaters_online_count": heaters_online_count,
        "heater_power_kw": heater_power_kw,
        "heater_energy_kwh": heater_energy_kwh,
        
        "thermal_alerts": hab_temp_mode,
        "net_heat_kw": net_heat_kw,
        "temp_change_c": temp_change_c,
        "hab_temp_mode" : hab_temp_mode
    }

    return thermal_updates, thermal_outputs

#---------------------temp alerts--------------------♡
def get_thermal_alerts(state):
    thermal_alerts = []
    
    if state.hab_temp_c > 28.0:
        thermal_alerts.append("CRITICAL: Habitat too hot")
    
    elif state.hab_temp_c < 18.0:
        thermal_alerts.append("CRITICAL: Habitat too cold")

    else:
        if state.hab_temp_c > state.max_comfort_temp_c:
            thermal_alerts.append("WARNING: Habitat getting hot")
        
        if state.hab_temp_c < state.min_comfort_temp_c:
            thermal_alerts.append("WARNING: Habitat getting cold")
            
    return thermal_alerts


#----------condensing heat exchanger (CHX)-----------♡
def run_chx(vapor_removed_kg, dt_min):
    hours_per_step = dt_min / 60.0
    seconds_per_step = dt_min * 60.0

    chx_power_used_kw = 0.0
    chx_energy_used_kwh = 0.0
    
    chx_cooling_kw = 0.0
    chx_cooling_kwh = 0.0
    
    chx_heat_added_kw = 0.0
    chx_heat_added_kwh = 0.0

    if vapor_removed_kg > 0.0:
        chx_power_used_kw = base_chx_power_kw
        chx_energy_used_kwh = chx_power_used_kw * hours_per_step
        
        chx_cooling_kj = vapor_removed_kg * condensation_heat_kj_per_kg
        chx_cooling_kw = chx_cooling_kj / seconds_per_step
        chx_cooling_kwh = chx_cooling_kw * hours_per_step

        chx_waste_heat_added_kw = chx_power_used_kw * base_chx_waste_heat_fraction       

        chx_heat_added_kw = chx_waste_heat_added_kw - chx_cooling_kw
        chx_heat_added_kwh = chx_heat_added_kw * hours_per_step
    
    return chx_power_used_kw, chx_energy_used_kwh, chx_cooling_kw, chx_cooling_kwh, chx_heat_added_kw, chx_heat_added_kwh


#-----------------updating humidity------------------♡
def update_humidity(state, breath_vapor_added_kg, skin_vapor_added_kg, dt_min):
    total_vapor_added_kg = breath_vapor_added_kg + skin_vapor_added_kg
    vapor_per_pct_kg = (water_vapor_per_m3 * state.hab_vol_m3) / 100.0
    
    target_vapor_kg = state.target_humidity_pct * vapor_per_pct_kg
    current_vapor_kg = (state.current_humidity_pct * vapor_per_pct_kg) + total_vapor_added_kg
    
    excess_vapor_kg = max(0.0, current_vapor_kg - target_vapor_kg)
    vapor_removed_kg = excess_vapor_kg * chx_removal_efficiency

    new_vapor_kg = current_vapor_kg - vapor_removed_kg
    new_humidity_pct = new_vapor_kg / vapor_per_pct_kg
    new_humidity_pct = max(20.0, min(80.0, new_humidity_pct))
    
    chx_power_used_kw, chx_energy_used_kwh, chx_cooling_kw, chx_cooling_kwh, chx_heat_added_kw, chx_heat_added_kwh = run_chx(vapor_removed_kg, dt_min)

    return {
        "new_humidity_pct": new_humidity_pct,

        "vapor_added_kg": total_vapor_added_kg,
        "vapor_removed_kg": vapor_removed_kg,
        "target_vapor_kg": target_vapor_kg,
        "new_vapor_kg": new_vapor_kg,

        "chx_power_used_kw": chx_power_used_kw,
        "chx_energy_used_kwh": chx_energy_used_kwh,

        "chx_cooling_kw": chx_cooling_kw,
        "chx_cooling_kwh": chx_cooling_kwh,

        "chx_heat_added_kw": chx_heat_added_kw,
        "chx_heat_added_kwh": chx_heat_added_kwh,
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
