from dataclasses import replace
from .state import Habitat_State
from .temp_system import get_thermal_alerts, get_humidity_alerts

#----------------get habitat status----------------♡
def get_status(all_alerts):
    hab_status = "NOMINAL"
    
    if any("critical" in alert.lower() for alert in all_alerts):
        hab_status = "CRITICAL"
    
    elif all_alerts:
        hab_status = "WARNING"

    else:
        hab_status = "NOMINAL"
    
    return hab_status


#--------------------gas alerts--------------------♡
def get_gas_alerts(state):
    gas_alerts = []

    if state.o2_kpa <= 17.0:
        gas_alerts.append("CRITICAL: Habitat oxygen levels too low")
    
    elif state.o2_kpa <= 19.5:
        gas_alerts.append("WARNING: Habitat oxygen low")
    
    if state.o2_kpa >= 22.0:
        gas_alerts.append("CRITICAL: Habitat oxygen levels too high | FIRE RISK")

    if state.co2_kpa >= 2.0:
        gas_alerts.append("CRITICAL: Carbon Dioxide too high")

    elif state.co2_kpa >= 1.0:
        gas_alerts.append("WARNING: Carbon Dioxide high")

    return gas_alerts


#-------------------power alerts-------------------♡
def get_power_alerts(state):
    power_alerts = []
    battery_percentage = state.battery_stored_kwh / state.battery_max_capacity_kwh

    if battery_percentage <= 0.10:
        power_alerts.append("ALERT: Power critical")

    elif battery_percentage <= 0.25:
        power_alerts.append("ALERT: Power low")
    
    return power_alerts


#-----------------all alerts update-----------------♡
def get_alerts(state, outputs):
    alerts = []

    alerts.extend(get_gas_alerts(state))
    alerts.extend(get_power_alerts(state))
    alerts.extend(get_thermal_alerts(outputs["new_hab_temp_c"]))
    alerts.extend(get_humidity_alerts(outputs["new_humidity_pct"]))

    return alerts


#def 
    # later add total pressure, leak detection, when scrubbers are full (saturated)
    # water supply low, n2 supply low, temp out of range
    # eventually airlocks humidity, temp loops
