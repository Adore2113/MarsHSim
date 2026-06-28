const update_sec = 3000;    // update panels every 3 seconds

function decimal_fmt(val, decimals = 2) {
  return typeof val === "number" ? val.toFixed(decimals) : "-";
} 

async function loadDashboard() {
  const response = await fetch("data/latest.json");
  const data = await response.json();

const alerts = data.system_status.alerts.length > 0
    ? data.system_status.alerts.join("<br>")
    : "No alerts";

  document.getElementById("status-p").innerHTML =
    `Status: ${data.system_status.status}<br>` +
    `Alerts: ${alerts}<br>` +
    `Sol ${data.environment.sol} | ${data.environment.lmst} LMST<br>` +
    `Mars Temp: ${data.environment.mars_temp_c.toFixed(1)} °C`;

  document.getElementById("o2").textContent =
    `O₂: ${data.atmosphere.oxygen_kpa.toFixed(2)} kPa`;

  document.getElementById("co2").textContent =
    `CO₂: ${data.atmosphere.carbon_dioxide_kpa.toFixed(2)} kPa`;

  document.getElementById("pressure").textContent =
    `Pressure: ${data.atmosphere.total_pressure_kpa.toFixed(2)} kPa`;

  document.getElementById("temp").textContent =
    `Hab Temp: ${data.environment.habitat_temp_c.toFixed(2)} °C`;
}

loadDashboard();