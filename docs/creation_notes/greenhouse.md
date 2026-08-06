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

## Greenhouse Lighting Plan:
#### Light Operation:
    ♡ LEDs offset lower natural light
    ♡ full LED light level: 1.0
    ♡ LED power density: 0.12 kW/m²
    ♡ LED heat ratio: 0.68

    ♡ LED support fills whatever gap is left below each zone's light target
    
    ♡ effective light per zone:
        - default zone light target: 0.70 kW/m²
        - default zone light absorption: 70%

        - best sunlight: 0.45 kW/m²
        - minimum useful sunlight: 0.15 kW/m²

    ♡ day_length_bonus:
        - used to adjust effective natural light according to the current amount of daylight

        - minimum day length value: 0.70
        - daylight contribution: 0.30

    ♡ calculation:
        - effective light per zone:
            natural_light_kw_per_m2 × light_absorption × day_length_bonus

        - shortest daylight fraction:
            0.70 × natural light

        - longest daylight fraction:
            1.00 × natural light

        - day_length_bonus: 
            0.70 + (0.30 × daylight_fraction)
        
#### Plant Lighting Schedule:
    ♡ full plant light period: 16 hours/sol
    ♡ plant light start time: 5:00 LMST
    ♡ plant light end time: 21:00 LMST
    ♡ calculation: 
        - light end hour: 
            (5 + 16) % 24 = 21:00

        - lights on: 
            05:00–21:00

        - lights off: 
            21:00–05:00

#### Light Modes:
    ♡ Power Mode Dimming:
        - normal: 
            full led level (1.0)
        - low power mode:
            led level × 0.6
        - critical power mode:
            led level × 0.2

    ♡ dark cycle: 
        - dark cycle: 8 hours/sol
        - outside scheduled hours, LEDs off

    ♡ full led support: 
        - used when effective natural light is at or below 0.15 kW/m²

    ♡ led support:
        - effective light below the zone's target, LEDs scale to fill the gap

    ♡ sunlight only:
        - effective light ≥ the zone's target, LEDs off

    ♡ calculation (led support level):
        - (light_target − effective_light) ÷ light_target

### ----------------------------------------

## Power Usage:        
#### Plant Light Power:
    ♡ LED power density: 0.12 kW/m²

    ♡ plant lighting power depends on effective grow area and LED level

    ♡ natural sunlight and partial LED support reduce actual energy use

    ♡ measured average, 16-hour schedule (current):
        ~ 260.5 kWh/sol

    ♡ measured average, before the 16-hour schedule: 
        ~ 325.6 kWh/sol
    
    ♡ calculation:
        - full LED power: 
            324 m² × 0.12 kW/m² = 38.88 kW

        - maximum energy over the full 16 hour light period: 
            38.88 kW × 16 hours = 622.08 kWh/sol

#### Greenhouse Habitat Lighting:
    ♡ greenhouse habitat lighting is part of the main habitat lighting system
 
    ♡ while plant lights are producing light:
        - greenhouse habitat lights remain off
 
    ♡ when plant lights are off:
        - greenhouse habitat lighting follows the current habitat light level

        - greenhouse habitat lighting follows the current habitat power mode
 
    ♡ calculation:
        - plant lights producing light: 
            greenhouse habitat light level = 0.0
        
        - plant lights not producing light: 
            greenhouse habitat light level = adjusted habitat light level

### ----------------------------------------

## Heat Generated:
#### Plant Light Heat:
    ♡ LED waste heat: ~ 26.4 kW
    ♡ LED heat ratio: 0.68
    ♡ structural heat: ~ 4.9 kW

    ♡ calculation:
        - LED heat output: 
            plant LED power × 0.68

        - maximum heat output at 38.88 kW:
            38.88 kW × 0.68 = 26.44 kW

        - maximum heat energy over 16 hours:
            26.44 kW × 16 hours ≈ 423.01 kWh/sol

        - LED heat: 
            38.88 kW × 0.68 (waste heat ratio) ≈ 26.4 kW

        -structural heat:
            0.015 kW/m² × 324 m² ≈ 4.9 kW

### ----------------------------------------

## Low Power Operation:
#### Low Power Mode:
    ♡ greenhouse plant light multiplier: 0.6
    ♡ calculation:
        - adjusted LED level:
            normal LED level × 0.6
 
#### Critical Power Mode:
    ♡ greenhouse plant light multiplier: 0.2
    ♡ calculation:
        - adjusted LED level:
            normal LED level × 0.2

### ----------------------------------------

