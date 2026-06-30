const update_sec = 3000;    // update panels every 3 seconds

function decimalFmt(val, decimals = 2) {
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

  const atm = data.atmosphere;
  const sab = data.sabatier;
  const water = data.water;
  const power = data.power;
  const thermal = data.thermal;
  const isru = data.isru;
  const gh = data.greenhouse;


//---------------------------------------------------♡

  //-----------status------------//
  const alerts = data.system_status.alerts.length > 0
    ? data.system_status.alerts.join("<br>")
    : "No alerts";

  document.getElementById("status-p").innerHTML =
    `Status: ${data.system_status.status}<br>` +
    `Alerts: ${alerts}<br>` +
    `Sol ${env.sol} | ${env.lmst} LMST<br>` +
    `Mars Temp: ${env.mars_temp_c.toFixed(1)} °C`;

  //---------atmosphere----------//

  //----------sabatier-----------//

  //------------water------------//

  //------------power------------//

  //----------thermal------------//

  //------------isru-------------//

  //---------greenhouse----------//

  document.getElementById("o2").textContent =
    `O₂: ${data.atmosphere.oxygen_kpa.toFixed(2)} kPa`;

  document.getElementById("co2").textContent =
    `CO₂: ${data.atmosphere.carbon_dioxide_kpa.toFixed(2)} kPa`;

  document.getElementById("pressure").textContent =
    `Pressure: ${data.atmosphere.total_pressure_kpa.toFixed(2)} kPa`;

  document.getElementById("temp").textContent =
    `Hab Temp: ${env.habitat_temp_c.toFixed(2)} °C`;
}

loadDashboard();