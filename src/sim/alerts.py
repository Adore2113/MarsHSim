#--------------------imports-------------------------♡
from .temp import get_thermal_alerts, get_humidity_alerts
#----------------------------------------------------♡


#-----------------get habitat status-----------------♡
def get_status(all_alerts):
    hab_status = "NOMINAL"
    
    if any("critical" in alert.lower() for alert in all_alerts):
        hab_status = "CRITICAL"
    
    elif any(alert.startswith("WARNING") for alert in all_alerts):
        hab_status = "WARNING"

    else:
        hab_status = "NOMINAL"
    
    return hab_status


#---------------------gas alerts---------------------♡
def get_gas_alerts(state):
    gas_alerts = []

        #--------------pressure---------------♡
    if state.total_pressure_kpa <= state.min_safe_pressure_kpa:
        gas_alerts.append("CRITICAL: Habitat pressure too low")

    elif state.total_pressure_kpa >= state.max_safe_pressure_kpa:
        gas_alerts.append("CRITICAL: Habitat pressure too high")

        #---------------oxygen----------------♡
    if state.o2_kpa <= state.min_safe_o2_kpa:
        gas_alerts.append("CRITICAL: Oxygen too low")

    elif state.o2_kpa < state.target_o2_kpa - 0.5:
        gas_alerts.append("WARNING: Oxygen below target")

    elif state.o2_kpa >= state.max_safe_o2_kpa:
        gas_alerts.append("CRITICAL: Oxygen too high | fire risk")

    elif state.o2_kpa > state.target_o2_kpa + 0.5:
        gas_alerts.append("WARNING: Oxygen above target")

        #-----------carbon dioxide------------♡
    if state.co2_kpa >= state.max_safe_co2_kpa:
        gas_alerts.append("CRITICAL: Carbon dioxide too high")

    elif state.co2_kpa > state.target_co2_kpa + 0.3:
        gas_alerts.append("WARNING: Carbon dioxide above target")

        #-------------trace gases-------------♡
    if state.ch4_kpa >= state.max_safe_ch4_kpa:
        gas_alerts.append("CRITICAL: Methane above safe limit")

    elif state.ch4_kpa > state.target_ch4_kpa:
        gas_alerts.append("WARNING: Methane detected")

    if state.h2_kpa >= state.max_safe_h2_kpa:
        gas_alerts.append("CRITICAL: Hydrogen above safe limit")

    elif state.h2_kpa > state.target_h2_kpa:
        gas_alerts.append("WARNING: Hydrogen detected")

    return gas_alerts


#--------------------power alerts--------------------♡
def get_power_alerts(state):
    power_alerts = []
    battery_pct = state.battery_stored_kwh / state.battery_max_capacity_kwh

    if battery_pct <= 0.10:
        power_alerts.append("CRITICAL: Battery power critical")

    elif battery_pct <= 0.25:
        power_alerts.append("WARNING: Battery power low")

    return power_alerts

#-------------------water alerts---------------------♡
def get_water_alerts(state):
    water_alerts = []
    potable_pct = state.potable_water_storage_kg / state.potable_water_storage_capacity_kg
    gray_pct = state.gray_water_storage_kg / state.gray_water_storage_capacity_kg
    black_pct = state.black_water_storage_kg / state.black_water_storage_capacity_kg
    brine_pct = state.brine_storage_kg / state.brine_storage_capacity_kg

    if potable_pct <= 0.10:
        water_alerts.append("CRITICAL: Potable water critically low")

    elif potable_pct <= 0.25:
        water_alerts.append("WARNING: Potable water low")

    if gray_pct >= 0.90:
        water_alerts.append("WARNING: Gray water storage almost full")

    if black_pct >= 0.90:
        water_alerts.append("WARNING: Black water storage almost full")

    if brine_pct >= 0.90:
        water_alerts.append("WARNING: Brine storage almost full")

    return water_alerts

#------------------subsytem alerts-------------------♡
def get_subsystem_alerts(state, outputs):
    subsystem_alerts = []

    if outputs.get("oga_limited_by_water", False):
        subsystem_alerts.append("WARNING: OGA limited by water supply")

    if outputs.get("sabatier_mode") == "limited co2":
        subsystem_alerts.append("WARNING: Sabatier limited by CO2 availability")

    if outputs.get("sabatier_mode") == "limited h2":
        subsystem_alerts.append("WARNING: Sabatier limited by H2 availability")

    if outputs.get("buffer_gas_mode") == "emergency_add":
        subsystem_alerts.append("CRITICAL: Emergency buffer gas addition active")

    return subsystem_alerts

#------------------all alerts update-----------------♡
def get_alerts(state, outputs):
    alerts = []

    alerts.extend(get_gas_alerts(state))
    alerts.extend(get_power_alerts(state))
    alerts.extend(get_water_alerts(state))
    alerts.extend(get_thermal_alerts(state))
    alerts.extend(get_humidity_alerts(outputs.get("new_humidity_pct", state.current_humidity_pct)))
    alerts.extend(get_subsystem_alerts(state, outputs))
    
    return alerts


#def 
    # later add total pressure, leak detection, when scrubbers are full (saturated)
    # water supply low, n2 supply low, temp out of range
    # eventually airlocks humidity, temp loops
