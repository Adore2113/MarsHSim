from dataclasses import replace
from .state import Habitat_State

default_dt_min = 5

crew_count = 30
hab_vol_m3 = 2000.0

scrub_per_bed_kpa = 0.06

def crew_metabolism(state):
# o2 drop pp: 0.0033
# co2 rise pp: 0.0029
    o2_drop = 0.0033 * state.crew_count
    co2_rise = 0.0029 * state.crew_count

    return o2_drop, co2_rise


def checking_gases(state):
    alerts = []
    if state.o2_kpa <= 19.5:
        alerts.append("ALERT: Oxygen low")
   
    if state.o2_kpa <= 17.0:
        alerts.append("ALERT: Oxygen critical")

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
# reduce scrubbing when co2 is already low
# 0.5 = scrub at 50% power, ect.
    if co2_after_crew < 0.2:
        total_scrub *= 0.5
    elif co2_after_crew <0.4:
        total_scrub += 0.75

# every 55min switch beds w. a brief co2 spike
    if state.mission_time_s != 0 and state.mission_time_s % 3300 == 0:
        total_scrub *= 0.85

    new_co2 = co2_after_crew - total_scrub

    return new_co2, total_scrub


def step(state: Habitat_State, dt_min: int = default_dt_min) -> Habitat_State:
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s

    o2_drop, co2_rise = crew_metabolism(state)

    o2_after_crew = state.o2_kpa - o2_drop
    co2_after_crew = state.co2_kpa + co2_rise

    new_co2, scrubbed_amount = removing_co2(state, co2_after_crew, next_time_s)

    o2_after_crew = max(o2_after_crew, 0)
    new_co2 = max(new_co2, 0)
    
    new_state = replace(
        state,
        mission_time_s = next_time_s,
        o2_kpa = round(o2_after_crew, 2),
        co2_kpa = round(new_co2, 2)
        )

    return new_state, scrubbed_amount


