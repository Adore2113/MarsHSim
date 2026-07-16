const update_sec = 3000;    // update panels every 3 seconds

//----------------------helpers----------------------♡
function decFmt(val, decimals = 2) {
  return typeof val === "number" ? val.toFixed(decimals) : "-";
} 

function posNeg(val) {
  return typeof val === "number" && val >= 0 ? "+" : "";
}

function pct(val, total) {
  if (!total) return "-";
  return ((val / total) * 100).toFixed(0) + "%";
}

function set(id, html) {
  const elId = document.getElementById(id);
  if (elId) elId.innerHTML = html;
}

function setClass(id, cls) {
  const elId = document.getElementById(id);
  if (!elId) return;
  elId.classList.remove("nominal", "warning", "critical");
  if (cls) elId.classList.add(cls);
}


//---------------------------------------------------♡
async function loadDashboard() {
  let data;
  try {
      const res = await fetch("data/latest.json?" + Date.now());
      data = await res.json();
  } catch (error) {
      console.warn("Could not load latest.json:", error);
      return;
  }

  const ss = data.system_status;
  const atm = data.atmosphere;
  const oga = data.oga;
  const sab = data.sabatier;
  const water = data.water;
  const power = data.power;
  const thermal = data.thermal;
  const isru_w = data.isru_water;
  const isru_a = data.isru_atm;
  const gh = data.greenhouse;
//---------------------------------------------------♡


  //-----------status------------//
  set("status-p",
    `Sol ${ss.sol} | ${ss.lmst} LMST<br>` +
    `Season: 123456<br>` +
    `Crew Count: 30 <br>` +
    `Crew Activity: placeholder <br>`
  );


  //-----------alerts------------//
  const alerts = ss.alerts.length > 0

    ? ss.alerts.join(",")
    : "No alerts";

  set("alerts-p",
    `Status: ${ss.status}<br>` +
    `Alerts:${alerts}<br>`
  );

  //--------Surface Conditions---------//
  set("surface-p",
    `Peak Sun Today: ${decFmt(power.peak_sun_today, 3)} / 1.0<br>` +
    `Sunlight per m²: ${decFmt(power.sunlight_per_m2_kw, 3)} kW<br>` +
    `Low Sun Streak: ${power.low_sun_streak_sols ?? 0} sols<br>`+
    `Dust Storm Risk: 00%<br>`
  ); //figure out what else goes here later//


  //---------atmosphere----------//
  set("atm-p",
    `Total Pressure: ${decFmt(atm.total_pressure_kpa)} kPa<br>` +
    `Oxygen: ${decFmt(atm.oxygen_kpa)} kPa<br>` +
    `Carbon Dioxide: ${decFmt(atm.carbon_dioxide_kpa)} kPa<br>` +
    `Nitrogen: ${decFmt(atm.nitrogen_kpa)} kPa<br>` +
    `<br>` +

    `Buffer Mode: ${atm.buffer_gas_mode ?? "-"}<br>` +
    `Argon: ${decFmt(atm.argon_kpa)} kPa<br>` +
    `Methane: ${decFmt(atm.methane_kpa)} kPa<br>` +
    `Pressure Gap: ${decFmt(atm.pressure_gap_kpa, 3)} kPa<br>` +
    `Gas Added: ${decFmt(atm.buffer_gas_added_kpa, 3)} kPa<br>` +
    `Gas Vented: ${decFmt(atm.buffer_gas_vented_kpa, 3)} kPa<br>` +
    `<br>` +

    `Amine Beds: ${atm.amine_beds_online ?? 0}<br>` +
    `Bed Switch: ${atm.bed_switch_this_step ? "YES" : "no"}<br>` +
    `CO₂ Scrubbed: ${decFmt(atm.co2_scrubbed_kpa, 4)} kPa<br>` +
    `CO₂ Scrubbed: ${decFmt(atm.co2_scrubbed_kg, 4)} kg<br>` +
    `<br>` +

    `O₂ Stored: ${decFmt(atm.o2_stored_kg)} kg<br>` +
    `CO₂ Stored: ${decFmt(atm.co2_stored_kg)} kg<br>` +
    `N₂ Stored: ${decFmt(atm.n2_stored_kg)} kg<br>` +
    `Ar Stored: ${decFmt(atm.ar_stored_kg)} kg<br>` +
    `H₂ Stored: ${decFmt(atm.h2_stored_kg, 3)} kg<br>` +
    `CH₄ Stored: ${decFmt(atm.ch4_stored_kg)} kg<br>`
  );


  //----------OGA-----------//
 set("oga-p",
    `OGA Mode: ${oga.oga_mode ?? "-"}<br>` +
    `O₂ Added: ${decFmt(oga.o2_added_kpa, 4)} kPa<br>` +
    `O₂ Vented: ${decFmt(oga.o2_vented_kg, 4)} kg<br>` +
    `H₂ Added: ${decFmt(oga.h2_added_kg, 4)} kg<br>` +
    `OGA Water Used: ${decFmt(oga.oga_water_used_kg, 3)} kg<br>` +
    `Water Limited: ${oga.oga_limited_by_water ? "YES" : "no"}`
 );

 
  //----------sabatier-----------//
set("sab-p",
  
  `Mode: ${sab.sabatier_mode ?? "-"}<br>` +

  `CO₂ Used: ${decFmt(sab.sabatier_co2_consumed_kg, 4)} kg<br>` +
  `H₂ Used: ${decFmt(sab.h2_used_kg, 4)} kg<br>` +

  `CH₄ Added: ${decFmt(sab.ch4_added_kg, 4)} kg<br>` +
  `CH₄ Vented: ${decFmt(sab.ch4_vented_kg, 4)} kg<br>` +
  `Water Added: ${decFmt(sab.sabatier_water_added_kg, 4)} kg`  );


  //------------water------------//
set("water-p",
  `Humidity: ${decFmt(water.humidity_pct, 1)} %<br>` +
  `Vapor Added: ${decFmt(water.vapor_added_kg, 3)} kg<br>` +
  `Vapor Removed: ${decFmt(water.vapor_removed_kg, 3)} kg<br>` +
  `<br>` +

  `UPA Processed: ${decFmt(water.upa_black_removed_kg, 3)} kg<br>` +
  `WPA Processed: ${decFmt(water.wpa_processed_kg, 3)} kg<br>` +
  `BPA Processed: ${decFmt(water.bpa_processed_kg, 3)} kg<br>` +
  `<br>` +

  `Potable Used: ${decFmt(water.potable_used_kg, 2)} kg<br>` +
  `<br>` +

  `Total Recovered: ${decFmt(water.total_recovered_kg, 3)} kg<br>` +
  `UPA Recovered: ${decFmt(water.upa_recovered_kg, 3)} kg<br>` +
  `WPA Recovered: ${decFmt(water.wpa_recovered_kg, 3)} kg<br>` +
  `BPA Recovered: ${decFmt(water.bpa_recovered_kg, 3)} kg<br>` +
  `<br>` +

  `Gray Added: ${decFmt(water.gray_added_kg, 3)} kg<br>` +
  `Black Added: ${decFmt(water.black_added_kg, 3)} kg<br>` +
  `Condensate Added: ${decFmt(water.condensate_added_kg, 3)} kg<br>` +
  `UPA Brine Added: ${decFmt(water.upa_brine_added_kg, 3)} kg<br>` +
  `<br>` +

  `Potable Stored: ${decFmt(water.potable_water_kg, 0)} kg<br>` +
  `Gray Stored: ${decFmt(water.gray_water_kg, 2)} kg<br>` +
  `Black Stored: ${decFmt(water.black_water_kg, 2)} kg<br>` +
  `Condensate Stored: ${decFmt(water.condensate_kg, 3)} kg<br>` +
  `Brine Stored: ${decFmt(water.brine_kg, 3)} kg<br>` +
  `Raw Water Stored: ${decFmt(water.raw_water_kg, 2)} kg`
  );


  //------------power------------//
set("power-p",
  `Net Energy: ${posNeg(power.net_energy_kwh)}${decFmt(power.net_energy_kwh)} kWh<br>` +
  `Battery: ${decFmt(power.battery_stored_kwh, 0)} kWh (${pct(power.battery_stored_kwh, power.battery_capacity_kwh)})<br>` +
  `<br>` +
  
  `Solar Arrays: ${power.solar_arrays_online ?? "-"} / 10<br>` +
  `Solar Generated: ${decFmt(power.solar_generated_kw)} kW<br>` +
  `Wellness Lights: ${power.wellness_lights ? "ON" : "off"}<br>` +
  `<br>` +

  `Total Power Used: ${decFmt(power.total_power_used_kw)} kW<br>` +
  `OGA: ${decFmt(power.oga_power_kw)} kW<br>` +
  `Sabatier: ${decFmt(power.sabatier_power_kw)} kW<br>` +
  `CO₂ Scrubber: ${decFmt(power.scrubber_power_kw)} kW<br>` +
  `Lights: ${decFmt(power.lights_power_kw)} kW<br>` +
  
  `CHX: ${decFmt(power.chx_power_kw)} kW<br>` +
  `Radiators: ${decFmt(power.radiator_power_kw)} kW<br>` +
  `Heaters: ${decFmt(power.heater_power_kw)} kW<br>` +
  `Greenhouse: ${decFmt(power.gh_power_kw)} kW<br>` +
  
  `ISRU water: ${decFmt(power.isru_water_power_kw)} kW<br>` +
  `ISRU atmosphere: ${decFmt(power.isru_atm_power_kw)} kW<br>` +
  `<br>` +
  
  `Total Energy: ${decFmt(power.total_energy_used_kwh, 3)} kWh`
);


  //----------thermal------------//
set("thermal-p",
  `Mode: ${thermal.mode ?? "—"}<br>` +
  `Hab Temp: ${decFmt(thermal.habitat_temp_c)} °C<br>` +
  `Mars Temp: ${decFmt(thermal.mars_temp_c, 1)} °C<br>` +
  `Temp Trend: ${posNeg(thermal.temp_trend_c_per_hr)}${decFmt(thermal.temp_trend_c_per_hr, 3)} °C/hr<br>` +
  `Heat Loss: ${decFmt(thermal.heat_loss_kw)} kW<br>` +
  `Net Heat: ${decFmt(thermal.net_heat_kw)} kW<br>` +
  `<br>` + 

  `Heaters Online: ${thermal.heaters_online ?? 0}<br>` +
  `Heater Heat: ${decFmt(thermal.heater_heat_kw)} kW<br>` +
  
  `OGA Heat: ${decFmt(thermal.oga_heat_kw)} kW<br>` +
  `Sabatier Heat: ${decFmt(thermal.sabatier_heat_kw)} kW<br>` +
  `Amine Bed Heat: ${decFmt(thermal.amine_bed_heat_kw)} kW<br>` +
  `Light Heat: ${decFmt(thermal.light_heat_kw)} kW<br>` +
  `CHX Heat: ${decFmt(thermal.chx_heat_kw)} kW<br>` +
  `GH Heat: ${decFmt(thermal.gh_heat_kw, 3)} kW<br>` +
  `ISRU Water Heat: ${decFmt(thermal.isru_water_heat_kw)} kW<br>` +
  `ISRU Atmosphere Heat: ${decFmt(thermal.isru_atm_heat_kw)} kW<br>` +
  `<br>` + 

  `Radiators: ${thermal.radiators_online ?? 0} / 7<br>` +
  `Radiator Cooling: ${decFmt(thermal.radiator_cooling_kw)} kW`
);


//---------isru water----------//
set("isru-water-p",
  `Water Mode: ${isru_w.isru_water_mode ?? "—"}<br>` +
  `Pipes Extracting: ${isru_w.pipes_extracting ?? 0}<br>` +
  `Pipes Deploying: ${isru_w.pipes_deploying ?? 0}<br>` +
  `Pipes Retracting: ${isru_w.pipes_retracting ?? 0}<br>` +
  `Raw Water Added: ${decFmt(isru_w.raw_water_added_kg, 3)} kg`
  );


  //----------isru atm-----------//
  set("isru-atm-p",
  `Atmosphere Mode: ${isru_a.isru_atm_mode ?? "—"}<br>` +
  `Compressors: ${isru_a.compressors ?? 0}<br>` +
    `<br>` + 
  `Sorbent Beds Absoring: ${isru_a.sorbent_beds_adsorbing ?? 0}<br>` +
  `Sorbent Beds on Regen: ${isru_a.sorbent_beds_regen ?? 0}<br>` +
  `Sorbent Beds on Standby: ${isru_a.sorbent_beds_standby ?? 0}<br>` +
  `<br>` + 

  `N₂ Added: ${decFmt(isru_a.n2_added_kg, 3)} kg<br>` +
  `Ar Added: ${decFmt(isru_a.ar_added_kg, 3)} kg<br>` +
  `CO₂ Added: ${decFmt(isru_a.co2_added_kg, 3)} kg<br>` +
  `CO₂ Absorbed: ${decFmt(isru_a.co2_absorbed_kg, 3)} kg<br>` +
  `CO₂ Released: ${decFmt(isru_a.co2_released_kg, 3)} kg<br>` +
  `CO₂ Bypassed: ${decFmt(isru_a.co2_bypassed_kg, 3)} kg<br>`
  );

  //---------greenhouse----------//
set("gh-p",
  `Mode: ${gh.greenhouse_mode ?? "—"}<br>` +
  `Food Produced: ${decFmt(gh.food_produced_kg, 3)} kg<br>`+

  `Transpiration: ${decFmt(gh.gh_transpiration_kg, 3)} kg<br>` +
  `Water Needed: ${decFmt(gh.gh_water_needed_kg, 3)} kg<br>` +
  `Water Used: ${decFmt(gh.gh_water_used_kg, 3)} kg<br>` +
  `Recirculated: ${decFmt(gh.gh_water_recirculated_kg, 3)} kg<br>` +
  `<br>` +

  `CO₂ Consumed: ${decFmt(gh.gh_co2_used_kpa, 7)} kPa<br>` +
  `O₂ Produced: ${decFmt(gh.gh_o2_added_kpa, 7)} kPa<br>` 
  );
}

loadDashboard();
setInterval(loadDashboard, update_sec);