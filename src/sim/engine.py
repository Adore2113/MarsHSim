from dataclasses import replace
from .state import Habitat_State
from .oxygen_system import run_oga
from .buffer_gas_system import mca, run_buffer_gas_control
from .co2_scrubber_system import run_co2_scrub
from .crew_metabolism import crew_metabolism

# ----default timestep----
default_dt_min = 5
#hours_per_step = dt_min / 60

# ----conversions ----
kelvin_offset = 273.15   # add to celsius to convert to kelvin
o2_kg_per_kpa = 18.2
co2_kg_per_kpa = 35.8
n2_kg_per_kpa = 22.75
ar_kg_per_kpa = 32.45
pa_per_kpa = 1000   # kilopascals to pascals

# ----chemistry constants----
r = 8.314   # the universal gas constant
h2_molar_mass = 2.016   # 1 mole h2 = 2.016g b/c h2 = 2 hydrogen atoms (1.008 g/mol each)
o2_molar_mass = 32.0

# ---- temperature targets----
target_temp_c = 23.0
min_temp_c = 20.0
max_temp_c = 25.0

# ----time----
def get_sol_time(mission_time_s):
    total_sol_seconds = 88775
    sol_seconds = mission_time_s % total_sol_seconds
    hour_24 = sol_seconds // 3600
    minutes = (sol_seconds % 3600) // 60
    return hour_24, minutes


# ----crew metabolism per default timestep----

# moved to crew_metabolism.py


def lights(state, dt_min):
    hour_24, minutes = get_sol_time(state.mission_time_s)
    hours_per_step = dt_min / 60
    light_power_used_kw = 0.0
    light_power_used_kwh = 0.0
    light_heat_added_kw = 0.0
    light_heat_added_kwh = 0.0

    # consider making daytime power not 100% brightness so that 100% can be used for emergencies or for boosting crew alertness later

    if 6 <= hour_24 < 21 or (hour_24 == 21 and minutes < 30):
        light_level = 1.0
        light_power_used_kw = 2.0
        light_power_used_kwh = light_power_used_kw * hours_per_step
        light_heat_added_kw = 0.5
        light_heat_added_kwh = light_heat_added_kw * hours_per_step
    
        # make the amount used come out of storage

    else:
        light_level = 0.2
        light_power_used_kw = 0.2
        light_power_used_kwh = light_power_used_kw * hours_per_step
        light_heat_added_kw = 0.1
        light_heat_added_kwh = light_heat_added_kw * hours_per_step

    return light_level, light_heat_added_kw, light_heat_added_kwh, light_power_used_kw, light_power_used_kwh



# ----functions for amine beds scrubbing co2----
# moved to co2_srubbber_system.py

# ----OGA and water electrolysis----
# moved to oxygen_system.py

# ----checking atmosphere gas levels---- 
# moved to buffer_gas_system.py

# ----controlling atmosphere gas levels----
# moved to buffer_gas_system.py

# ----alerts ----
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

    # later add total pressure, leak detection, when scrubbers are full (saturated)
    # water supply low, n2 supply low, temp out of range
    # eventually airlocks humidity, temp loops

    return gas_alerts


def step(state: Habitat_State, dt_min: int = default_dt_min):
    dt_s = int(dt_min * 60)
    next_time_s = state.mission_time_s + dt_s

    light_level, light_heat_kw, light_heat_kwh, light_power_kw, light_power_kwh = lights(state, dt_min)
    o2_drop_kpa, co2_rise_kpa, crew_temp_rise_kw, crew_temp_rise_kwh = crew_metabolism(state, dt_min)

    o2_after_crew_kpa = state.o2_kpa - o2_drop_kpa
    co2_after_crew_kpa = state.co2_kpa + co2_rise_kpa

    oga_results = run_oga(state, o2_after_crew_kpa, dt_min)
    o2_after_oga_kpa = oga_results["o2_after_oga_kpa"]
    o2_added_kpa = oga_results["o2_added_kpa"]
    h2_produced_kg = oga_results["h2_produced_kg"]
    water_used_kg = oga_results["water_used_kg"]
    oga_heat_kw = oga_results["oga_heat_kw"]
    oga_heat_kwh = oga_results["oga_heat_kwh"]

    co2_after_scrub_kpa, co2_removed_kpa, new_co2_stored_kpa, co2_scrubber_heat_added_kw, co2_scrubber_heat_added_kwh = run_co2_scrub(state, co2_after_crew_kpa, next_time_s, dt_min)

    new_water_for_oga_kg = max(0.0, state.water_for_oga_kg - water_used_kg)
    new_h2_stored_kg = state.h2_stored_kg + h2_produced_kg

    pre_buffer_state = replace(
        state,
        mission_time_s=next_time_s,
        light_level = light_level,
        o2_kpa=round(o2_after_oga_kpa, 4),
        co2_kpa=round(co2_after_scrub_kpa, 4),
        co2_stored_kpa=round(new_co2_stored_kpa, 4),
        h2_stored_kg=round(new_h2_stored_kg, 6),
        water_for_oga_kg=round(new_water_for_oga_kg, 3),
    )

    buffer_gas_results = run_buffer_gas_control(pre_buffer_state, dt_min)

    new_state = replace(
    pre_buffer_state,
    n2_kpa=round(buffer_gas_results["n2_kpa"], 4),
    ar_kpa=round(buffer_gas_results["ar_kpa"], 4),
    n2_stored_kpa=round(buffer_gas_results["n2_stored_kpa"], 4),
    ar_stored_kpa=round(buffer_gas_results["ar_stored_kpa"], 4),
    )

    return new_state, co2_removed_kpa


