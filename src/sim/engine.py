from dataclasses import replace

from .state import Habitat_State

default_dt_min = 5

def sep(state: Habitat_State, dt_min: int = default_dt_min) -> Habitat_State:
    dt_s = int(dt_min * 60)
    return replace(state, mission_time_s=state.mission_time_s + dt_s)