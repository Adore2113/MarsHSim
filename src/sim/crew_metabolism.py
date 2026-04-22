from dataclasses import replace
from .state import Habitat_State

#--------------------constants-----------------------♡
w_per_kw = 1000   # watts to kilowatts

base_o2_drop_kpa = 0.00011
base_co2_rise_kpa = 0.0000967

base_breath_vapor_per_day_kg = 1.0
base_skin_vapor_per_day_kg = 0.8

base_nourishment_per_day_kg = 2.35    # drinking and food prep
base_hygiene_water_per_day_kg = 1.5
base_black_water_per_day_kg = 1.8

# base_condensate_per_day_kg = ?
#----------------------------------------------------♡


#--------crew activites and metabolism rates---------♡
crew_activity_states = {
    "normal" : {"o2_drop_multiplier" : 1.0, "co2_rise_multiplier" : 1.0, "breath_vapor_multiplier" : 1.0, "skin_vapor_multiplier" : 1.0, "heat_per_person_w" : 120, "water_multiplier": 1.0},
    "sleep" : {"o2_drop_multiplier" : 0.8, "co2_rise_multiplier" : 0.8, "breath_vapor_multiplier" : 0.8, "skin_vapor_multiplier" : 0.4, "heat_per_person_w" : 83,  "water_multiplier": 0.6},
    "exercise" : {"o2_drop_multiplier" : 1.5, "co2_rise_multiplier" : 1.5, "breath_vapor_multiplier" : 1.4, "skin_vapor_multiplier" : 2.0, "heat_per_person_w" : 280,  "water_multiplier": 1.8},  
    "intense" : {"o2_drop_multiplier" : 2.0, "co2_rise_multiplier" : 2.0, "breath_vapor_multiplier" : 1.8, "skin_vapor_multiplier" : 3.0, "heat_per_person_w" : 350, "water_multiplier": 2.2},
    }


# -------crew metabolism per default timestep--------♡
def total_crew_metabolism(state, dt_min):
    hours_per_step = dt_min / 60
    crew_activity = crew_activity_states[state.crew_activity]

    #-------------atmosphere gas changes-------------♡
    o2_drop_kpa = base_o2_drop_kpa * state.crew_count * crew_activity["o2_drop_multiplier"]
    co2_rise_kpa = base_co2_rise_kpa * state.crew_count * crew_activity["co2_rise_multiplier"]

    #----------------humidity changes----------------♡
    breath_vapor_added_kg = (base_breath_vapor_per_day_kg * state.crew_count * crew_activity["breath_vapor_multiplier"] * hours_per_step) / 24
    skin_vapor_added_kg = (base_skin_vapor_per_day_kg * state.crew_count * crew_activity["skin_vapor_multiplier"] * hours_per_step) / 24

    #--------------temperature changes---------------♡
    crew_temp_rise_kw = (crew_activity["heat_per_person_w"] * state.crew_count) / w_per_kw
    crew_temp_rise_kwh = crew_temp_rise_kw * hours_per_step

    #------------------water usage-------------------♡
    nourishment_per_day_kg = (base_nourishment_per_day_kg * state.crew_count * crew_activity["water_multiplier"] * hours_per_step) / 24
    hygiene_water_per_day_kg = (base_hygiene_water_per_day_kg * state.crew_count * crew_activity["water_multiplier"] * hours_per_step) / 24
    black_water_per_day_kg = (base_black_water_per_day_kg * state.crew_count * crew_activity["water_multiplier"] * hours_per_step) / 24

    potable_water_used_kg = nourishment_per_day_kg + hygiene_water_per_day_kg

   # gray_water_added_kg = potable_water_used_kg * 0.6  # placeholder ratio


    return {
        "o2_drop_kpa" : o2_drop_kpa,
        "co2_rise_kpa" : co2_rise_kpa,
        "breath_vapor_added_kg" : breath_vapor_added_kg,
        "skin_vapor_added_kg" : skin_vapor_added_kg,
        "crew_temp_rise_kw" : crew_temp_rise_kw,
        "nourishment_per_day_kg" : nourishment_per_day_kg,
        "hygiene_water_per_day_kg" : hygiene_water_per_day_kg,
        "black_water_per_day_kg" : black_water_per_day_kg,
        "potable_water_used_kg" : potable_water_used_kg,
        }