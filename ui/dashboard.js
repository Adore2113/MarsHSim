const update_sec = 3000;    // update panels every 3 seconds

function decFmt(val, decimals = 2) {
  return typeof val === "number" ? val.toFixed(decimals) : "-";
} 

function posNeg(val) {
  return val >= 0 ? "+" : "";
}

function pct(val, total) {
  if (total == null || total === 0) return "-";
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

  if (cls) {
    elId.classList.add(cls);
  }
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
  const sab = data.sabatier;
  const water = data.water;
  const power = data.power;
  const thermal = data.thermal;
  const isru = data.isru;
  const gh = data.greenhouse;


//---------------------------------------------------♡

  //-----------status------------//
  const alerts = ss.alerts.length > 0
    ? ss.alerts.join("<br>")
    : "No alerts";

  set("status-p",
    `Status: ${ss.status}<br>` +
    `Sol ${ss.sol} | ${ss.lmst} LMST<br>` +
    `Habitat Temp: ${decFmt(ss.habitat_temp_c, 1)} °C<br>` +
    `Mars Temp: ${decFmt(ss.mars_temp_c, 1)} °C`
  );

  //---------atmosphere----------//
  set("atm-p",
    `Total Pressure: ${decFmt(atm.total_pressure_kpa)} kPa<br>` +
    `Oxygen: ${decFmt(atm.oxygen_kpa)} kPa<br>` +
    `Carbon Dioxide: ${decFmt(atm.carbon_dioxide_kpa)} kPa<br>` +
    `Nitrogen: ${decFmt(atm.nitrogen_kpa)} kPa<br>` +
    `Argon: ${decFmt(atm.argon_kpa)} kPa<br>` +
    `Methane: ${decFmt(atm.methane_kpa)} kPa<br>` +
    `<br>` +

    `Buffer Mode: ${atm.buffer_gas_mode ?? "-"}<br>` +
    `Pressure Gap: ${decFmt(atm.pressure_gap_kpa, 3)} kPa<br>` +
    `Gas Added: ${decFmt(atm.buffer_gas_added_kpa, 3)} kPa<br>` +
    `Gas Vented: ${decFmt(atm.buffer_gas_vented_kpa, 3)} kPa<br>` +
    `<br>` +   

    `O₂ Stored: ${decFmt(atm.o2_stored_kg)} kg<br>` +
    `CO₂ Stored: ${decFmt(atm.co2_stored_kg)} kg<br>` +
    `N₂ Stored: ${decFmt(atm.n2_stored_kg)} kg<br>` +
    `Ar Stored: ${decFmt(atm.ar_stored_kg)} kg<br>` +
    `H₂ Stored: ${decFmt(atm.h2_stored_kg, 3)} kg<br>` +
    `CH₄ Stored: ${decFmt(atm.ch4_stored_kg)} kg<br>` +
    `<br>` +   

    `Amine Beds: ${atm.amine_beds_online ?? 0}<br>` +
    `CO₂ Scrubbed: ${decFmt(atm.co2_scrubbed_kpa, 4)} kPa<br>` +
    `<br>` +   

    `OGA Mode: ${atm.oga_mode ?? "-"}<br>` +
    `O₂ Added: ${decFmt(atm.o2_added_kpa, 4)} kPa<br>` +
    `H₂ Added: ${decFmt(atm.h2_produced_kg, 4)} kg<br>` +
    `OGA Water Used: ${decFmt(atm.oga_water_used_kg, 3)} kg<br>` +
    `Water Limited: ${atm.oga_limited_by_water ? "YES" : "no"}`
  );

  //----------sabatier-----------//
set("sab-p",
  `Mode: ${sab.sabatier_mode ?? "-"}<br>` +
  `<br>` + 

 // `CO₂ Used: ${decFmt(sab.sabatier_co2_consumed_kpa, 4)} kPa<br>` + //
  `CO₂ Used: ${decFmt(sab.sabatier_co2_consumed_kg, 4)} kg<br>` +
  `H₂ Used: ${decFmt(sab.h2_used_kg, 4)} kg<br>` +
  `<br>` + 

  `CH₄ Added: ${decFmt(sab.ch4_added_kg, 4)} kg<br>` +
  `CH₄ Vented: ${decFmt(sab.ch4_vented_kg, 4)} kg<br>` +
  `Water Produced: ${decFmt(sab.sabatier_water_produced_kg, 4)} kg`
);

  //------------water------------//
set("water-p",
  `Humidity: ${pct(water.humidity_pct, 1)} %<br>` +
  `Vapor Added: ${decFmt(water.vapor_added_kg, 3)} kg<br>` +
  `Vapor Removed: ${decFmt(water.vapor_removed_kg, 3)} kg<br>` +
  `Potable Used: ${decFmt(water.potable_used_kg, 2)} kg<br>` +
  `<br>` +

  `UPA Processed: ${decFmt(water.upa_black_removed_kg, 3)} kg<br>` +
  `WPA Processed: ${decFmt(water.wpa_processed_kg, 3)} kg<br>` +
  `BPA Processed: ${decFmt(water.bpa_processed_kg, 3)} kg<br>` +
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
  `Raw Water Added: ${decFmt(water.raw_water_added_kg, 3)} kg<br>` +
  `<br>` +

  `Potable Stored: ${decFmt(water.potable_water_kg, 2)} kg<br>` +
  `Gray Stored: ${decFmt(water.gray_water_kg, 2)} kg<br>` +
  `Black Stored: ${decFmt(water.black_water_kg, 2)} kg<br>` +
  `Condensate Stored: ${decFmt(water.condensate_kg, 3)} kg<br>` +
  `Brine Stored: ${decFmt(water.brine_kg, 3)} kg<br>` +
  `Raw Water Stored: ${decFmt(water.raw_water_kg, 2)} kg`

);
  //------------power------------//

  //----------thermal------------//

  //------------isru-------------//

  //---------greenhouse----------//

}

loadDashboard();