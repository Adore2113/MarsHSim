from dataclasses import replace
from .state import Habitat_State

default_dt_min = 5

crew_count = 30
hab_vol_m3 = 2000.0

target_o2 = 20.0
target_co2 = 0.4

scrub_per_bed_kpa = 0.0045

def crew_metabolism(state):
# o2 drop for 30p: 0.0033
# co2 rise for 30p: 0.0029
    o2_drop = 0.00011 * state.crew_count
    co2_rise = 0.0000967 * state.crew_count

    return o2_drop, co2_rise


def gas_alert(state):
    alerts = []
    if state.o2_kpa <= 19.5:
        alerts.append("ALERT: Oxygen low")
   
    if state.o2_kpa <= 17.0:
        alerts.append("ALERT: Oxygen critical")
    
    if state.o2_kpa >= 22.0:
        alerts.append("ALERT: Oxygen very high | fire risk")

    if state.co2_kpa >= 1.0:
        alerts.append("ALERT: Carbon Dioxide high")

    if state.co2_kpa >= 2.0:
        alerts.append("ALERT: Carbon Dioxide critical")

    return alerts


def removing_co2(state, co2_after_crew, next_time_s):  
    online_beds = 0
    for bed in state.amine_beds:
        if bed["status"] == "online":
            online_beds += 1
    
    total_scrub = online_beds * scrub_per_bed_kpa

    # every 55min switch beds w. a brief co2 spike
    if state.next_time_s % 3300 == 0 and state.next_time_s != 0:
        total_scrub *= 0.80

    co2_excess = co2_after_crew - target_co2
    co2_scrubbed = min(total_scrub, max(0.0, co2_excess))
    new_co2 = co2_after_crew - co2_scrubbed

    return new_co2, co2_scrubbed


def o2_regen(state, o2_after_crew):
# future : OGA oxygen generator
# consumes water -> consumes power -> makes o2 -> makes hydrogen (h2) byproduct
    o2_deficit = target_o2 - o2_after_crew
    #make enough o2 to fill deficit + a bit extra, never negative
    oga_o2_output = min(0.004, max(0.0, o2_deficit + 0.001))
    new_o2 = o2_after_crew + oga_o2_output

    return new_o2


def step(state: Habitat_State, dt_min: int = default_dt_min) -> Habitat_State:
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s

    o2_drop, co2_rise = crew_metabolism(state)

    o2_after_crew = state.o2_kpa - o2_drop
    co2_after_crew = state.co2_kpa + co2_rise

    new_o2 = o2_regen(state, o2_after_crew)
    new_co2, scrubbed_amount = removing_co2(state, co2_after_crew, next_time_s)

    new_state = replace(
        state,
        mission_time_s = next_time_s,
        o2_kpa = round(new_o2, 4),
        co2_kpa = round(new_co2, 4),
        )

    return new_state, scrubbed_amount


