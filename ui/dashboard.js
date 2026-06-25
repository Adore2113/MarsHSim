async function loadDashboard() {
  const response = await fetch("data/latest.json");
  const data = await response.json();

  document.getElementById("status").textContent =
    `Status: ${data.system_status.status}`;

  document.getElementById("time").textContent =
    `Sol ${data.environment.sol} | ${data.environment.lmst} LMST`;

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