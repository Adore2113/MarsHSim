from dataclasses import replace
from .state import Habitat_State
from .power_system import power_alerts



#-----------------get habitat status-----------------♡
def get_status(state):
    if state.o2_kpa <= 17.0 or state.co2_kpa >= 2.0:
        return "CRITICAL"
    
    elif state.o2_kpa <= 19.5 or state.co2_kpa >= 1.0:
        return "WARNING"
    
    else:
        return "NOMINAL"


#--------------------gas alerts----------------------♡
def gas_alert(state):
    gas_alerts = []
    
    #o2
    if state.o2_kpa <= 17.0:
        gas_alerts.append("ALERT: Oxygen critical")
    
    elif state.o2_kpa <= 19.5:
        gas_alerts.append("ALERT: Oxygen low")
    
    if state.o2_kpa >= 22.0:
        gas_alerts.append("ALERT: Oxygen very high | fire risk")

    #co2
    if state.co2_kpa >= 2.0:
        gas_alerts.append("ALERT: Carbon Dioxide critical")

    elif state.co2_kpa >= 1.0:
        gas_alerts.append("ALERT: Carbon Dioxide high")

    return gas_alerts


#--------------------power alerts--------------------♡
def power_alerts(state):
    power_alerts = []
    battery_percentage = state.battery_stored_kwh / state.battery_max_capacity_kwh

    if battery_percentage <= 0.10:
        power_alerts.append("ALERT: Power critical")

    elif battery_percentage <= 0.25:
        power_alerts.append("ALERT: Power low")
    
    return power_alerts


#-----------------------alerts-----------------------♡
#def 
    # later add total pressure, leak detection, when scrubbers are full (saturated)
    # water supply low, n2 supply low, temp out of range
    # eventually airlocks humidity, temp loops
