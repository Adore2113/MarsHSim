#--------------------imports-------------------------♡
import json
from pathlib import Path
from .mars_time import get_sol_time
from .buffer_gas import mca
from .alerts import get_status
#----------------------------------------------------♡

base_dir = Path(__file__).resolve().parents[2]
ui_data_path = base_dir / "ui" / "data" / "latest.json"


#----------------just like print.py------------------♡
def write_dashboard_json(state, outputs, alerts):
    sol, hour, minutes = get_sol_time(state)

    data = {
        "system_status": {
            "status": get_status(alerts),
            "alerts": alerts,
        },

        "environment": {
            "sol": sol,
            "lmst": f"{hour:02d}:{minutes:02d}",
            "habitat_temp_c": state.hab_temp_c,
            "mars_temp_c": outputs.get("mars_temp_c", state.mars_temp_c),
            "food_produced_kg": outputs.get("greenhouse_food_produced_kg", 0),
            "temp_change_per_hour_c": outputs.get("temp_change_c", 0) * 12,
        },

        "atmosphere": {
            "total_pressure_kpa": mca(state),
            "oxygen_kpa": state.o2_kpa,
            "carbon_dioxide_kpa": state.co2_kpa,
            "nitrogen_kpa": state.n2_kpa,
            "argon_kpa": state.ar_kpa,
            "methane_kpa": state.ch4_kpa,

            "buffer_gas_mode": outputs.get("buffer_gas_mode"),
            "pressure_gap_kpa": outputs.get("pressure_gap_kpa", 0),
            "buffer_gas_added_kpa": outputs.get("total_buffer_gas_added_kpa", 0),
            "buffer_gas_vented_kpa": outputs.get("total_buffer_gas_vented_kpa", 0),

            "o2_stored_kg": state.o2_stored_kg,
            "co2_stored_kg": state.co2_stored_kg,
            "n2_stored_kg": state.n2_stored_kg,
            "ar_stored_kg": state.ar_stored_kg,
            "h2_stored_kg": state.h2_stored_kg,
            "ch4_stored_kg": state.ch4_stored_kg,

            "isru_atm_mode": outputs.get("isru_atm_mode", "offline"),
            "compressors": outputs.get("compressors_extracting", 0),
            "beds_adsorbing": outputs.get("sorbent_beds_adsorbing", 0),
            "beds_regen": outputs.get("sorbent_beds_regenerating", 0),
            "beds_standby": outputs.get("sorbent_beds_standby", 0),

            "n2_added_kg": outputs.get("isru_n2_added_kg", 0),
            "ar_added_kg": outputs.get("isru_ar_added_kg", 0),
            "co2_captured_kg": outputs.get("sorbent_co2_absorbed_kg", 0),

            "amine_beds_online": outputs.get("beds_online_count", 0),
            "gh_co2_used_kpa": outputs.get("greenhouse_co2_consumed_kpa", 0),
            "sabatier_co2_kpa": outputs.get("sabatier_co2_consumed_kpa", 0),
            "co2_scrubbed_kpa": outputs.get("co2_removed_kpa", 0),
            "o2_added_kpa": outputs.get("o2_added_kpa", 0),
            "ch4_added_kg": outputs.get("sabatier_ch4_produced_kg", 0),
            "ch4_vented_kg": outputs.get("sabatier_ch4_vented_kg", 0),
            "h2_used_kg": outputs.get("sabatier_h2_consumed_kg", 0),
            "gh_o2_added_kpa": outputs.get("greenhouse_o2_produced_kpa", 0),
        },

        "power": {
            "net_energy_kwh": outputs.get("net_energy_kwh", 0),
            "peak_sun_today": state.peak_sunlight_today,
            "sunlight_per_m2_kw": state.daylight_m2_kw,
            "low_sun_streak_sols": state.low_sunlight_streak_sols,
            "solar_arrays_online": outputs.get("solar_arrays_online_count", 0),
            "solar_generated_kw": outputs.get("total_solar_generated_kw", 0),
            "battery_stored_kwh": state.battery_stored_kwh,
            "wellness_lights": state.wellness_lights_on,
            "greenhouse_mode": outputs.get("greenhouse_mode", "offline"),

            "total_power_used_kw": outputs.get("total_power_used_kw", 0),
            "gh_power_kw": outputs.get("greenhouse_led_power_kw", 0),
            "sabatier_power_kw": outputs.get("sabatier_power_used_kw", 0),
            "scrubber_power_kw": outputs.get("amine_bed_power_used_kw", 0),
            "lights_power_kw": outputs.get("light_power_used_kw", 0),
            "chx_power_kw": outputs.get("chx_power_used_kw", 0),
            "radiator_power_kw": outputs.get("radiator_power_kw", 0),
            "heater_power_kw": outputs.get("heater_power_kw", 0),
            "isru_power_kw": outputs.get("isru_power_used_kw", 0),
            "total_energy_used_kwh": outputs.get("total_energy_used_kwh", 0),
        },

        "thermal": {
            "mode": outputs.get("hab_temp_mode"),
            "mars_temp_c": outputs.get("mars_temp_c", state.mars_temp_c),
            "habitat_temp_c": state.hab_temp_c,
            "heat_loss_kw": outputs.get("heat_loss_kw", 0),
            "temp_trend_c_per_hr": outputs.get("temp_change_c", 0) * 12,
            "net_heat_kw": outputs.get("net_heat_kw", 0),
            "heaters_online": outputs.get("heaters_online_count", 0),
            "heater_heat_kw": outputs.get("heater_heat_kw", 0),
            "isru_heat_kw": outputs.get("isru_heat_added_kw", 0),
            "gh_heat_kw": outputs.get("total_greenhouse_heat_kw", 0),
            "sabatier_heat_kw": outputs.get("sabatier_heat_added_kw", 0),
            "amine_bed_heat_kw": outputs.get("amine_bed_heat_added_kw", 0),
            "light_heat_kw": outputs.get("light_heat_kw", 0),
            "chx_heat_kw": outputs.get("chx_heat_added_kw", 0),
            "oga_heat_kw": outputs.get("oga_heat_kw", 0),
            "radiators_online": outputs.get("radiators_online_count", 0),
            "radiator_cooling_kw": outputs.get("radiator_heat_rejection_kw", 0),
        },

        "water": {
            "vapor_added_kg": outputs.get("vapor_added_kg", 0),
            "humidity_pct": outputs.get("new_humidity_pct", state.current_humidity_pct),
            "vapor_removed_kg": outputs.get("vapor_removed_kg", 0),
            "gh_transpiration_kg": outputs.get("greenhouse_transpiration_kg", 0),
            "gh_water_needed_kg": outputs.get("greenhouse_water_needed_kg", 0),
            "gh_water_used_kg": outputs.get("greenhouse_water_consumed_kg", 0),
            "gh_recirculated_kg": outputs.get("greenhouse_water_recirculated_kg", 0),

            "upa_black_removed_kg": outputs.get("upa_black_water_removed_kg", 0),
            "wpa_processed_kg": outputs.get("wpa_water_processed_kg", 0),
            "bpa_processed_kg": outputs.get("bpa_water_processed_kg", 0),

            "potable_used_kg": outputs.get("potable_water_used_kg", 0),
            "oga_water_used_kg": outputs.get("oga_water_used_kg", 0),

            "total_recovered_kg": outputs.get("total_recovered_water_kg", 0),
            "upa_recovered_kg": outputs.get("upa_recovered_water_kg", 0),
            "wpa_recovered_kg": outputs.get("wpa_recovered_water_kg", 0),
            "bpa_recovered_kg": outputs.get("bpa_recovered_water_kg", 0),

            "gray_added_kg": outputs.get("gray_water_added_kg", 0),
            "black_added_kg": outputs.get("black_water_added_kg", 0),
            "condensate_added_kg": outputs.get("vapor_removed_kg", 0),
            "upa_brine_added_kg": outputs.get("upa_brine_added_kg", 0),
            "sabatier_water_added_kg": outputs.get("sabatier_water_produced_kg", 0),
            "raw_water_added_kg": outputs.get("isru_raw_water_added_kg", 0),

            "potable_water_kg": state.potable_water_storage_kg,
            "gray_water_kg": state.gray_water_storage_kg,
            "black_water_kg": state.black_water_storage_kg,
            "condensate_kg": state.condensate_storage_kg,
            "brine_kg": state.brine_storage_kg,
            "raw_water_kg": state.raw_isru_water_storage_kg,
        },
    }

    ui_data_path.parent.mkdir(parents=True, exist_ok=True)

    with open(ui_data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)