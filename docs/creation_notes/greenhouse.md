# Greenhouse:
### General Notes:
    ♡ this isn't a greenhouse simulator, so it's intentionally not as complex as it could be

    ♡ each zone uses averaged plant data instead of simulating individual crops

    ♡ actual light exposure depends on:
        - season / daylight fraction
        - zone light target
        - LED support level
        - power mode (normal/low/critical)

    ♡ running the greenhouse (LEDs, pumps, circulation) consumes power continuously while online, creating the same kind of engineering trade off as the solar field's maintenance draw

    ♡ grow area can be larger than the greenhouse floor area b/c of the vertical growing area

 ### ----------------------------------------
 
## Greenhouse Zones Plan (19/06/2026):
#### Greenhouse:
    ♡ pressurized volume: 1,007 m³
    ♡ floor area: 265 m²
    ♡ height: 3.8 m
    ♡ calculation:
        - volume:
            265 m² × 3.8 m = 1,007 m³

#### Grow area:
    ♡ 324 m² total effective grow area
    ♡ 3 zones
    ♡ calculation:
        - structural: 
            90 m²
        - container: 
            110 m²
        - rack: 
            124 m²
        - 90 + 110 + 124 = 324 m²

#### Zones:
    ♡ total model grow area: 324 m²
    ♡ separated by container type
    ♡ structural zone: 
        - 90 m²
        - 0.022 kPa/m²/sol O2/CO2 rate

    ♡ container zone: 
        - 110 m²
        - 0.020 kPa/m²/sol O2/CO2 rate

    ♡ rack zone: 
        - 124 m²
        - 0.015 kPa/m²/sol O2/CO2 rate

    ♡ calculation:
        - 90 m² + 110 m² + 124 m² = 324 m²
        - O2 produced/sol (same per m² rate for CO2 consumed):
            ♡ structural: 
                0.022 kPa/m²/sol × 90 m² = 1.98 kPa/sol

            ♡ container: 
                0.020 kPa/m²/sol × 110 m² = 2.20 kPa/sol

            ♡ rack: 
                0.015 kPa/m²/sol × 124 m² = 1.86 kPa/sol

            ♡ total ≈ 6.04 kPa/sol


#### Zone Subdivision (racks/containers per zone):
    ♡ I don't have racks per zone or containers per rack counts recorded yet

    ♡ moved to Future Considerations for now

### ----------------------------------------
 
#### Power Production:
    ♡ measured average, 16-hour base light schedule (current):
          ~ 260.5 kWh/sol

    ♡ measured average, before the 16-hour schedule:
          ~ 325.6 kWh/sol

    ♡ peak draw, full LED across all zones:
          ~ 71.3 kW

    ♡ calculation:
        - base (pumps, circulation, etc.): 
            0.10 kW/m² × 324 m² = 32.4 kW

        - LED, full support: 
            0.12 kW/m² × 324 m² = 38.88 kW

        - peak: 
            32.4 + 38.88 ≈ 71.3 kW
 
#### Heat Load:
    ♡ LED waste heat: ~ 26.4 kW
    ♡ structural heat: ~ 4.9 kW
    ♡ calculation (at full LED support):
        - LED heat: 
            38.88 kW × 0.68 (waste heat ratio) ≈ 26.4 kW
        - structural heat: 
            0.015 kW/m² × 324 m² ≈ 4.9 kW
 
### ----------------------------------------

#### Light Operation:
    ♡ LEDs offset lower natural light

    ♡ effective light per zone:
        natural_light_kw_per_m2 × light_absorption × day_length_bonus

    ♡ day_length_bonus:
        0.70 + (0.30 × daylight_fraction)

    ♡ calculation:
        - shortest daylight fraction:
            0.70 × natural light

        - longest daylight fraction:
            1.00 × natural light

        - LED support fills whatever gap is left below each zone's light target
 
### ----------------------------------------
