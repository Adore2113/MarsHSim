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
            265 m² × 3.8 m
            = 1,007 m³

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
        - total:
            90 + 110 + 124
            = 324 m²

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
        - total grow area:
            90 m² + 110 m² + 124 m²
            = 324 m²

        - O2 produced/sol (same as CO2 consumed/m²):
            ♡ structural: 
                0.022 kPa/m²/sol × 90 m²
                = 1.98 kPa/sol

            ♡ container: 
                0.020 kPa/m²/sol × 110 m²
                = 2.20 kPa/sol

            ♡ rack: 
                0.015 kPa/m²/sol × 124 m²
                = 1.86 kPa/sol

            ♡ total ≈ 6.04 kPa/sol

#### Zone Subdivision (racks/containers per zone):
    ♡ I don't have racks per zone or containers per rack counts recorded yet

    ♡ moved to Future Considerations for now

### ----------------------------------------

## Growth Model:
#### Growth:
    ♡ default starting health: 0.98
    ♡ default starting light exposure: 0.65
    ♡ default growth multiplier: 1.0

    ♡ growth is tracked by zone instead of by individual crop

    ♡ calculation:
        - growth increase:
            base growth rate × growth multiplier × light exposure × health × sol fraction

#### Harvest:
    ♡ triggers when growth progress reaches or exceeds: 1.0

    ♡ growth progress resets to 0.0 after harvest
    
    ♡ food is produced only when a harvest occurs

    ♡ calculation:
        - food produced:
            ♡ food yield per m² × growing area × yield multiplier

        - harvest condition:
            ♡ growth progress ≥ 1.0

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
            (5 + 16) % 24
            = 21:00

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

## Greenhouse Water Model:
#### Water Use:
    ♡ water requirements are calculated by zone

    ♡ structural:
        - multiplier: 1.15
        - base water: 3.4 kg/m²/sol
        - growing area: 90 m²

    ♡ container:
        - multiplier: 1.00
        - base water: 2.6 kg/m²/sol
        - growing area: 110 m²

    ♡ rack:
        - multiplier: 0.90
        - base water: 1.95 kg/m²/sol
        - growing area: 124 m²

    ♡ calculation:
        - water needed:
            base water needed per m² × growing area × water multiplier × sol fraction

        - structural:
            3.4 kg/m²/sol × 90 m² × 1.15
            = 351.90 kg/sol

        - container:
            2.6 kg/m²/sol × 110 m² × 1.00
            = 286.00 kg/sol

        - rack:
            1.95 kg/m²/sol × 124 m² × 0.90
            = 217.62 kg/sol

        - total:
            351.90 + 286.00 + 217.62
            = 855.52 kg/sol

### ----------------------------------------

#### Water Recirculation:
    ♡ default water recirculation efficiency: 93%
    ♡ each zone has its own recirculation efficiency

    ♡ structural:
        - recirculation efficiency: 82%
        - water recirculated: 288.56 kg/sol
        - water taken up by plants: 63.34 kg/sol

    ♡ container:
        - recirculation efficiency: 88%
        - water recirculated: 251.68 kg/sol
        - water taken up by plants: 34.32 kg/sol

    ♡ rack:
        - recirculation efficiency: 94%
        - water recirculated: 204.56 kg/sol
        - water taken up by plants: 13.06 kg/sol

    ♡ total:
        - water recirculated: 744.80 kg/sol
        - water taken up by plants: 110.72 kg/sol

    ♡ calculation:
        - water recirculated:
            water needed × recirculation efficiency

        - water taken up by plants:
            water needed × (1.0 - recirculation efficiency)

        - structural recirculated:
            351.90 kg/sol × 0.82
            = 288.56 kg/sol

        - structural plant uptake:
            351.90 kg/sol × 0.18
            = 63.34 kg/sol

        - container recirculated:
            286.00 kg/sol × 0.88
            = 251.68 kg/sol

        - container plant uptake:
            286.00 kg/sol × 0.12
            = 34.32 kg/sol

        - rack recirculated:
            217.62 kg/sol × 0.94
            = 204.56 kg/sol

        - rack plant uptake:
            217.62 kg/sol × 0.06
            = 13.06 kg/sol

        - total water recirculated:
            288.56 + 251.68 + 204.56
            = 744.80 kg/sol

        - total plant water uptake:
            63.34 + 34.32 + 13.06
            = 110.72 kg/sol

        - water balance:
            744.80 + 110.72
            = 855.52 kg/sol

### ----------------------------------------

#### Runoff:
    ♡ runoff represents nutrient solution draining from the plant containers

    ♡ this water is collected and returned to the greenhouse nutrient reservoirs

    ♡ runoff is included in the greenhouse recirculation values above

    ♡ to do:
        - determine whether runoff should eventually be modeled separately

### ----------------------------------------

#### Transpiration and Plant Mass:
    ♡ transpiration ratio: 85% of plant water uptake
    ♡ plant mass ratio: 15% of plant water uptake

    ♡ calculation:
        - transpiration:
            plant water uptake × 0.85

        - plant mass water:
            plant water uptake × 0.15

### ----------------------------------------

## CO₂ & O₂ Model:
#### Photosynthesis:
    ♡ greenhouse gas exchange depends on plant health and light exposure

    ♡ calculations are performed separately for each greenhouse zone

    ♡ calculation:
        - photosynthesis factor:
            light exposure × plant health

        - CO₂ consumed:
            CO₂ consumption rate per m² per sol × growing area × sol fraction × photosynthesis factor

        - O₂ produced:
            O₂ production rate per m² per sol × growing area × sol fraction × photosynthesis factor


#### Gas Exchange Target:
    ♡ crew count: 30

    ♡ current crew O₂ demand: 
        0.00011 kPa/hour/person

    ♡ Mars sol length: 
        ~ 24.66 hours

    ♡ target greenhouse contribution:
        ~ 2% of crew O₂ and CO₂ needs

    ♡ calculation:
        - crew O₂ demand:
            0.00011 kPa/hour/person × 30 people × 24.66 hours/sol
            ≈ 0.0814 kPa/sol

        - target greenhouse contribution:
            0.0814 kPa/sol × 0.02
            ≈ 0.00163 kPa/sol

        - approximate average target rate across 324 m²:
            0.00163 kPa/sol ÷ 324 m²
            ≈ 0.00000503 kPa/m²/sol

    ♡ this average is only a preliminary target

    ♡ final zone rates still need to preserve differences between the structural, container and rack zones

### ----------------------------------------
