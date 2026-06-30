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

  set("status-p",
    `Status: ${data.system_status.status}<br>` +
    `Alerts: ${alerts}<br>` +
    `Sol ${data.system_status.sol} | ${data.system_status.lmst} LMST<br>` +
    `Mars Temp: ${decimalFmt(data.system_status.mars_temp_c, 1)} °C`
  );

  //---------atmosphere----------//

  //----------sabatier-----------//

  //------------water------------//

  //------------power------------//

  //----------thermal------------//

  //------------isru-------------//

  //---------greenhouse----------//

}

loadDashboard();