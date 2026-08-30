#--------------------imports-------------------------♡
from .lights import light_system
from .solar_field import run_solar_field
#----------------------------------------------------♡

# file for handling habitat power and batteries

#--------------------constants-----------------------♡
#---------backup bank----------♡
max_transfer_speed_kw = 5000.0    # speed the power moves from bank - primary
secondary_reserve_floor_pct = 0.10    # keep 10% if not in emergency

#-------primary battery--------♡
primary_high_threshold_pct = 0.95    # start sending power to secondary
primary_low_threshold_pct = 0.25    # start pulling from secondary
primary_critical_pct = 0.20    # emergency, heavier pull from secondary
#---------------------------------------------------♡


#---------------battery power flow------------------♡
def manage_battery_bank(state, net_energy_kwh, dt_min):
    hours_per_step = dt_min / 60.0
    max_transfer_kwh = max_transfer_speed_kw * hours_per_step
    primary_max_kwh = state.primary_battery_max_capacity_kwh
    bank_max_kwh = state.battery_bank_max_capacity_kwh

    primary_after_net_kwh = state.primary_battery_stored_kwh + net_energy_kwh
    primary_after_net_kwh = max(0.0, min(primary_max_kwh, primary_after_net_kwh))

    primary_pct = primary_after_net_kwh / primary_max_kwh
    bank_pct = state.battery_bank_stored_kwh / bank_max_kwh

    bank_transfer_kwh = 0.0

    if primary_pct >= primary_high_threshold_pct:
        excess_above_threshold_kwh = primary_after_net_kwh - (primary_max_kwh * primary_high_threshold_pct)
        room_in_bank_kwh = bank_max_kwh - state.battery_bank_stored_kwh

        bank_transfer_kwh = min(excess_above_threshold_kwh, room_in_bank_kwh, max_transfer_kwh)

        new_primary_kwh = primary_after_net_kwh - bank_transfer_kwh
        new_bank_kwh = state.battery_bank_stored_kwh + bank_transfer_kwh

    elif primary_pct <= primary_low_threshold_pct and bank_pct > secondary_reserve_floor_pct:
        deficit_kwh = (primary_max_kwh * primary_low_threshold_pct) - primary_after_net_kwh

        if primary_pct <= primary_critical_pct:
            deficit_kwh *= 1.5

        bank_available_kwh = state.battery_bank_stored_kwh - (bank_max_kwh * secondary_reserve_floor_pct)
        bank_transfer_kwh = -min(deficit_kwh, bank_available_kwh, max_transfer_kwh)

        new_primary_kwh = min(primary_max_kwh, primary_after_net_kwh - bank_transfer_kwh)
        new_bank_kwh = state.battery_bank_stored_kwh + bank_transfer_kwh

    else: 
        new_primary_kwh = primary_after_net_kwh
        new_bank_kwh = state.battery_bank_stored_kwh

    return new_primary_kwh, new_bank_kwh, bank_transfer_kwh


#------------------total power usage-----------------♡
def get_total_power_usage(amine_bed_power_used_kw, oga_power_used_kw, light_power_used_kw, w_light_power_used_kw, gh_led_power_kw, gh_equipment_power_kw, gh_chx_power_kw, radiator_power_kw, heater_power_kw, chx_power_used_kw, upa_power_used_kw, wpa_power_used_kw, bpa_power_used_kw, sabatier_power_used_kw, isru_water_power_used_kw, isru_atm_power_used_kw, solar_field_power_used_kw):
    total_power_used_kw = (amine_bed_power_used_kw + oga_power_used_kw + light_power_used_kw + w_light_power_used_kw + gh_led_power_kw + gh_equipment_power_kw + gh_chx_power_kw + radiator_power_kw + heater_power_kw + chx_power_used_kw  + upa_power_used_kw + wpa_power_used_kw + bpa_power_used_kw + sabatier_power_used_kw + isru_water_power_used_kw + isru_atm_power_used_kw + solar_field_power_used_kw)

    return total_power_used_kw

def get_total_energy_usage(amine_bed_energy_used_kwh, oga_energy_used_kwh, light_energy_used_kwh, w_light_energy_used_kwh, gh_led_energy_kwh, gh_equipment_energy_kwh, gh_chx_energy_kwh, radiator_energy_kwh, heater_energy_kwh, chx_energy_used_kwh, upa_energy_used_kwh, wpa_energy_used_kwh, bpa_energy_used_kwh, sabatier_energy_used_kwh, isru_water_energy_used_kwh, isru_atm_energy_used_kwh, solar_field_energy_used_kwh):
    total_energy_used_kwh = (amine_bed_energy_used_kwh + oga_energy_used_kwh + light_energy_used_kwh + w_light_energy_used_kwh + gh_led_energy_kwh + gh_equipment_energy_kwh + gh_chx_energy_kwh + radiator_energy_kwh + heater_energy_kwh + chx_energy_used_kwh + upa_energy_used_kwh + wpa_energy_used_kwh + bpa_energy_used_kwh + sabatier_energy_used_kwh + isru_water_energy_used_kwh + isru_atm_energy_used_kwh + solar_field_energy_used_kwh)  

    return total_energy_used_kwh


#------------------full power system-----------------♡
def run_system_power(
    state,
    co2_results,
    oga_results,
    light_results,
    thermal_outputs,
    humidity_results,
    greenhouse_outputs,
    water_outputs,
    sabatier_outputs,
    isru_water_outputs,
    isru_atm_outputs,
    dt_min
    ):

    solar_field_updates, solar_field_outputs = run_solar_field(state, dt_min)

    total_power_used_kw = get_total_power_usage(
        co2_results["amine_bed_power_used_kw"],
        oga_results["oga_power_used_kw"],
        light_results["light_power_used_kw"],
        light_results["w_light_power_used_kw"],
        greenhouse_outputs.get("gh_led_power_kw", 0.0),
        greenhouse_outputs.get("gh_equipment_power_kw", 0.0),
        greenhouse_outputs.get("gh_chx_power_kw", 0.0),
        thermal_outputs.get("radiator_power_kw", 0.0),
        thermal_outputs.get("heater_power_kw", 0.0),
        humidity_results.get("chx_power_used_kw", 0.0),
        water_outputs.get("upa_power_used_kw", 0.0),
        water_outputs.get("wpa_power_used_kw", 0.0),
        water_outputs.get("bpa_power_used_kw", 0.0),
        sabatier_outputs.get("sabatier_power_used_kw", 0.0),
        isru_water_outputs.get("isru_water_power_used_kw", 0.0),
        isru_atm_outputs.get("isru_atm_power_used_kw", 0.0),
        solar_field_outputs["solar_field_power_used_kw"],
    )

    total_energy_used_kwh = get_total_energy_usage(
    co2_results["amine_bed_energy_used_kwh"],
    oga_results["oga_energy_used_kwh"],
    light_results["light_energy_used_kwh"],
    light_results["w_light_energy_used_kwh"],
    greenhouse_outputs.get("gh_led_energy_kwh", 0.0),
    greenhouse_outputs.get("gh_equipment_energy_kwh", 0.0),
    greenhouse_outputs.get("gh_chx_energy_kwh", 0.0),
    thermal_outputs.get("radiator_energy_kwh", 0.0),
    thermal_outputs.get("heater_energy_kwh", 0.0),
    humidity_results.get("chx_energy_used_kwh", 0.0),
    water_outputs.get("upa_energy_used_kwh", 0.0),
    water_outputs.get("wpa_energy_used_kwh", 0.0),
    water_outputs.get("bpa_energy_used_kwh", 0.0),
    sabatier_outputs.get("sabatier_energy_used_kwh", 0.0),
    isru_water_outputs.get("isru_water_energy_used_kwh", 0.0),
    isru_atm_outputs.get("isru_atm_energy_used_kwh", 0.0),
    solar_field_outputs["solar_field_energy_used_kwh"],
    )

    total_solar_generated_kw = solar_field_outputs["solar_field_generated_kw"]
    total_solar_generated_kwh = solar_field_outputs["solar_field_generated_kwh"]

    net_energy_kwh = total_solar_generated_kwh - total_energy_used_kwh
   
    new_primary_battery_stored_kwh = state.primary_battery_stored_kwh + net_energy_kwh
    new_primary_battery_stored_kwh = max(0.0, min(state.primary_battery_max_capacity_kwh, new_primary_battery_stored_kwh))
   
    battery_percentage = (new_primary_battery_stored_kwh / state.primary_battery_max_capacity_kwh)

    if battery_percentage <= 0.10:
        power_mode = "critical"

    elif battery_percentage <= 0.25:
        power_mode = "low"

    else:
        power_mode = "normal"

    total_heat_added_kw = light_results["total_light_heat_kw"]
    total_heat_added_kwh = light_results["total_light_heat_kwh"]

    #------------dict for updating state-------------♡ 
    power_updates = {
        "primary_battery_stored_kwh": new_primary_battery_stored_kwh,
        "power_mode": power_mode,
        **solar_field_updates,
    }
    
    #-----------dict for printing outputs------------♡ 
    power_outputs = {
        "blocks_online_count": solar_field_outputs["blocks_online_count"],
        "blocks_flipped_this_step": solar_field_outputs["blocks_flipped_this_step"],
        "blocks_cleaned_this_step": solar_field_outputs["blocks_cleaned_this_step"],

        "total_solar_generated_kw": total_solar_generated_kw,
        "total_solar_generated_kwh": total_solar_generated_kwh,
        
        "total_power_used_kw": total_power_used_kw,
        "total_energy_used_kwh": total_energy_used_kwh,
        
        "total_heat_added_kw": total_heat_added_kw,
        "total_heat_added_kwh": total_heat_added_kwh,

        "solar_field_power_used_kw": solar_field_outputs["solar_field_power_used_kw"],
        "solar_field_energy_used_kwh": solar_field_outputs["solar_field_energy_used_kwh"],

        **light_results,
        "net_energy_kwh": net_energy_kwh,
    }

    return power_updates, power_outputs


#------------deciding low power priorites------------♡
def apply_low_power_mode_lights(power_mode, adjusted_light_level, wellness_light_level):
    if power_mode == "low":
        adjusted_light_level = max(0.02, adjusted_light_level * 0.5)
        wellness_light_level = 0.0
    
    elif power_mode == "critical":
        adjusted_light_level = max(0.02, adjusted_light_level * 0.3)
        wellness_light_level = 0.0

    return adjusted_light_level, wellness_light_level
