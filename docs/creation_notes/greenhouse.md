# Greenhouse:
### General Notes:
    ♡ preliminary estimates
 
    ♡ this is a Mars habitat simulator, not a dedicated greenhouse simulator so I kept things intentionally simpler
 
    ♡ greenhouse is currently being treated as a separate building running on the same systems as the habitat; habitat size will be updated to include it later
 
    ♡ organized into 3 zones by container type (structural, container, rack), using zone averages instead of simulating individual crops
 
 ### ----------------------------------------
 
## Greenhouse Zones & Lighting Plan:
    ♡ best sunlight: 0.45 kW/m²
    ♡ minimum useful sunlight: 0.15 kW/m²
    ♡ LED power density: 0.12 kW/m²
    ♡ LED heat ratio: 0.68
    ♡ greenhouse light start hour: 5 (5:00 AM)
    ♡ greenhouse light duration: 16 hours
    ♡ default zone light target: 0.70 kW/m²
    ♡ default zone light absorption: 70%
    ♡ calculation:
        - start hour + light duration:
                5 hours + 16 hours = 21 hours
        - check for day-wrap:
                21 hours ÷ 24 hours/day = 0.875 days
        - whole days part of 0.875 days = 0 days (light doesn't roll into the next day)
        - convert whole days back to hours:
                0 days × 24 hours/day = 0 hours
        - get the final hour:
                21 hours − 0 hours = 21 hours
        - light end hour = 21:00 LMST