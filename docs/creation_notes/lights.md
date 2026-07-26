# Habitat Lighting:
### General Notes:
    ♡ preliminary estimates

    ♡ when the greenhouse lighting system is offline, the main lights will come on

    ♡ light power use and heat output change with the current light level

    ♡ individual lights and fixtures are not simulated for V1
    
    ♡ light level is represented from 0.0–1.0
    
    ♡ natural sunlight reduces the amount of artificial lighting required

    ♡ main habitat lighting and wellness lighting are modeled as separate loads
    
### ----------------------------------------

## Habitat Lighting Plan:
#### Area:
    ♡ habitat pressurized volume: 2,400 m³
    ♡ total floor area and room layout have not been finalized

    ♡ lighting is currently modeled as one combined habitat load

    ♡ power values will be recalculated once the habitat floor area and layout are designed

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

