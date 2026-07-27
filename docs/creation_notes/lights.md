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
    ♡ current values are preliminary
    ♡ maximum light level: 1.0
    ♡ minimum normal light level: 0.2
    ♡ full lighting power: 2.0 kW
    ♡ full lighting heat output: 0.5 kW
    ♡ current values are preliminary
    ♡ calculation:
        - power:
            2.0 kW × adjusted light level

        - heat:
            0.5 kW × adjusted light level

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
#### Lighting Schedule:
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