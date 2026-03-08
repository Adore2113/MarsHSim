from dataclasses import replace
from .state import Habitat_State

default_dt_min = 5

crew_count = 30
hab_vol_m3 = 2000.0



def step(state: Habitat_State, dt_min: int = default_dt_min) -> Habitat_State:
    dt_s = int(dt_min * 60)

    o2_drop = 0.0033 * state.crew_count
    co2_rise = 0.0029 * state.crew_count

    return replace(
        state, 
        mission_time_s=state.mission_time_s + dt_s,
        o2_kpa=state.o2_kpa - o2_drop,
        co2_kpa=state.co2_kpa + co2_rise
        )


