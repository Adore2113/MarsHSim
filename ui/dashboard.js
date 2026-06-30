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
    `Total Pressure: ${(atm.total_pressure_kpa)} kPa<br>` +
    `Oxygen: ${(atm.oxygen_kpa)} kPa<br>` +
    `Carbon Dioxide: ${(atm.carbon_dioxide_kpa)} kPa<br>` +
    `Nitrogen: ${(atm.nitrogen_kpa)} kPa<br>` +
    `Argon: ${(atm.argon_kpa)} kPa<br>` +
    `Methane: ${(atm.methane_kpa)} kPa<br>` +
    `<br>` +
    `Buffer Mode: ${(atm.buffer_gas_mode)} kPa<br>` +
    `Pressure Gap: ${(atm.pressure_gap_kpa)} kPa<br>` +
    `Gas Added: ${(atm.buffer_gas_added_kpa)} kPa<br>` +
    `Gas Vented: ${(atm.buffer_gas_vented_kpa)} kPa<br>` +
    `<br>` +   

  );

  //----------sabatier-----------//

  //------------water------------//

  //------------power------------//

  //----------thermal------------//

  //------------isru-------------//

  //---------greenhouse----------//

}

loadDashboard();