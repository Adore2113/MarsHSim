# Habitat Lighting:
### General Notes:
    ♡ preliminary estimates

    ♡ when the greenhouse lighting system is offline, the main lights will come on

    ♡ light power use and heat output change with the current light level

    ♡ individual lights and fixtures are not simulated for V1
    
    ♡ light level is represented from 0.0–1.0
    
    ♡ natural sunlight reduces the amount of artificial lighting required

    ♡ main habitat lighting and wellness lighting are modeled as separate loads

    ♡ power values will be recalculated once the habitat floor area and layout are designed
    
### ----------------------------------------

## Habitat Lighting Plan:
#### Habitat:
    ♡ habitat pressurized volume: 2,400 m³
    ♡ floor area: not finalized
    ♡ room layout: not finalized

#### Main Lights:
    ♡ maximum light level: 1.0
    ♡ minimum normal light level: 0.2
    ♡ full lighting power: 2.0 kW
    ♡ full lighting heat output: 0.5 kW
    ♡ calculation:
        - power:
            2.0 kW × adjusted light level
        - heat:
            0.5 kW × adjusted light level
        - minimum normal power:
            2.0 kW × 0.2 = 0.4 kW
        - minimum normal heat:
            0.5 kW × 0.2 = 0.1 kW

#### Main Lighting Schedule:
    ♡ crew awake hours: 06:00–21:30 LMST
    ♡ full light period: 15.5 hours/sol
    ♡ dim light period: 8.5 hours/sol
    ♡ daytime base light level: 1.0
    ♡ nighttime base light level: 0.2
    ♡ calculation:
        - 21.5 hours - 6.0 hours = 15.5 hours full-light period
        - 24.0 hours - 15.5 hours = 8.5 hours dim-light period

#### Sunlight Dimming:
    ♡ sunlight amount range: 0.0–1.0
    ♡ maximum sunlight dimming: 0.6
    ♡ minimum normal light level: 0.2
    ♡ calculation:
        - sunlight dimming = sunlight amount × 0.6
        - adjusted light level = base light level - sunlight dimming
        - final light level = max(0.2, adjusted light level)


### ----------------------------------------
#### Wellness Lights:
    ♡ activated after prolonged periods of low natural sunlight
    ♡ full wellness lighting power: 0.5 kW
    ♡ full wellness lighting heat output: 0.1 kW
    ♡ calculation:
        - power:
            0.5 kW × wellness light level
        - heat:
            0.1 kW × wellness light level

### ----------------------------------------
#### Greenhouse Plant Lights:
    ♡ plant lights are separate from the main habitat lighting system
    ♡ plant lighting area: total effective grow area of all greenhouse zones
    ♡ LED power density: 0.12 kW/m²
    ♡ LED heat ratio: 0.68
    ♡ full LED light level: 1.0
    ♡ plant light start time: 05:00 LMST
    ♡ plant light end time: 21:00 LMST
    ♡ full plant light period: 16 hours/sol
    ♡ dark cycle: 8 hours/sol
    ♡ calculation:
        - plant light end:
            05:00 + 16 hours = 21:00 LMST
        - dark cycle:
            24 hours - 16 hours = 8 hours
        - full LED power:
            effective grow area × 0.12 kW/m²
        - LED heat output:
            full LED power × 0.68
        - full-cycle energy:
            full LED power × 16 hours

### ----------------------------------------
#### Low Power Operation:
    ♡ main habitat lighting is reduced during low-power modes
    ♡ wellness lighting is disabled during low and critical power modes
    ♡ calculation:
        - low mode:
            adjusted light level × 0.5
        - critical mode:
            adjusted light level × 0.3

### ----------------------------------------
#### Future Considerations:
    ♡ 

### ----------------------------------------
### Lighting Design Decisions:
#### Why wellness lights?
    ♡ I considered season changes on earth and how people are effected by the lack of sunlight so for moral reasons I wanted to incorporate a sort of SAD lighting idea but for the whole habitat
    
    ♡ mock sunlight is better than no sunlight

#### Why timed greenhouse lights?

### ----------------------------------------
### Dev Log notes:
###### :
    ♡ 