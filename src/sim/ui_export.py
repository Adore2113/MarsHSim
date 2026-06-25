#--------------------imports-------------------------♡
import json
from pathlib import Path
from .mars_time import get_sol_time
from .buffer_gas import mca
from .alerts import get_status
#----------------------------------------------------♡


UI_DATA_PATH = Path("src/ui/data/latest.json")


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
