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
    `Amine Beds: ${atm.oga_limited_by_water ?? "YES" : "no"}`
  );

  //----------sabatier-----------//

  //------------water------------//

  //------------power------------//

  //----------thermal------------//

  //------------isru-------------//

  //---------greenhouse----------//

}

loadDashboard();