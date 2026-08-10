# Habitat Lighting:
### General Notes:
    ♡ preliminary estimates

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
    ♡ light level scales power and heat proportionally

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

#### Wellness Lights:
    ♡ activated after prolonged periods of low natural sunlight to support crew wellness

    ♡ full wellness light level: 1.0
    ♡ inactive wellness light level: 0.0
    ♡ full wellness lighting power: 0.5 kW
    ♡ full wellness lighting heat output: 0.1 kW
    ♡ calculation:
        - power:
            0.5 kW × wellness light level
        - heat:
            0.1 kW × wellness light level


### ----------------------------------------

#### Main Light Schedule:
    ♡ crew awake hours: 6:00–21:30 LMST
    ♡ full light period: 15.5 hours/sol
    ♡ dim light period: 8.5 hours/sol
    ♡ daytime base light level: 1.0
    ♡ nighttime base light level: 0.2
    ♡ calculation:
        - 21.5 hours - 6.0 hours = 15.5 hours full light period
        - 24.0 hours - 15.5 hours = 8.5 hours dim light period

#### Sunlight Dimming:
    ♡ sunlight amount range: 0.0–1.0
    ♡ maximum sunlight dimming: 0.6
    ♡ minimum normal light level: 0.2
    ♡ calculation:
        - sunlight dimming:
            sunlight amount × 0.6

        - adjusted light level:
            base light level - sunlight dimming

        - final light level:
            max(0.2, adjusted light level)


### ----------------------------------------

#### Wellness Light Operation:
    ♡ activation trigger: 3 consecutive low sunlight sols 
    
    ♡ deactivation trigger: 1 or fewer consecutive low sunlight sols
    
    ♡ previous state maintained at: 2 consecutive low sunlight sols

    ♡ follows the current habitat power mode

    ♡ disabled during low and critical power modes
    
    ♡ calculation (when active):
        - active power:
            0.5 kW × 1.0 = 0.5 kW
        - active heat:
            0.1 kW × 1.0 = 0.1 kW

        - maximum energy if active for 24 hours:
            0.5 kW × 24 hours = 12.0 kWh/sol

        - maximum heat energy if active for 24 hours:
            0.1 kW × 24 hours = 2.4 kWh/sol


### ----------------------------------------


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

#### Low Power Operation:
    ♡ main habitat lighting is reduced during low and critical power modes

    ♡ wellness lighting is disabled during low and critical power modes

#### Low Power Mode:
    ♡ main habitat light multiplier: 0.5
    ♡ wellness light level: 0.0
    ♡ calculation:
        - main lights:
                adjusted light level × 0.5
        - wellness lights:
                1.0 × 0.0 = 0.0

#### Critical Power Mode:
    ♡ main habitat light multiplier: 0.3
    ♡ wellness light level: 0.0
    ♡ calculation:
        - main lights:
            adjusted light level × 0.3
        - wellness lights:
            1.0 × 0.0 = 0.0


### ----------------------------------------

#### Future Considerations:
    ♡ calculate the total habitat floor area

    ♡ separate habitat lighting into physical zones

    ♡ replace preliminary lighting capacity values with area based calculations

    ♡ consider separate lighting levels for:
        -crew living areas
        -work areas
        -corridors
        -maintenance areas
        -sleeping areas

    ♡ give wellness lights a nighttime shutoff schedule


### ----------------------------------------

### Design Evolution
#### Early Lighting System:
    ♡ habitat lighting originally lived inside power.py

    ♡ later moved into its own file lights.py

    ♡ greenhouse lighting is still with the greenhouse subsystem


### ----------------------------------------

### Design Decisions:
#### Why wellness lights?
    ♡ I considered seasonal changes on Earth and how people can be affected by long periods without enough natural sunlight

    ♡ for morale/wellness reasons I wanted to incorporate a sort of SAD lighting idea but for the whole habitat
    
    ♡ mock sunlight is better than no sunlight during
      prolonged dark periods

#### Why separate habitat lighting and wellness lighting?
    ♡ habitat lighting powers the whole habitat

    ♡ wellness lighting only exists to support crew health during prolonged low sunlight

    ♡ separating them allows wellness lighting to be disabled during low power without affecting normal habitat operation


### ----------------------------------------

### Dev Log notes:
###### 04/05/2026:
        ♡ the lighting function will react and adjust to the level of daylight

###### 05/08/2026:
    ♡ started light for the greenhouse

###### 05/10/2026:
    ♡ I was able to go over the lighting function I had made in greenhouse.py and decided to add zones for each type of container the plants are in, I'm going to use the averages of that crop types in the containers

###### 06/23/2026:
    ♡ I set up to be running with daylight, but now I'm thinking about having the lights on a 12 hour cycle, but also turn off if not needed

###### 07/23/2026:
        ♡ I isolated the subsystems and the greenhouse power is taking up a high percentage of the power, I have it set up to be running w. daylight, but now I'm thinking about having the lights on a 12 hour cycle

        ♡ finished updating the greenhouse lights, at 16 base hours for the greenhouse lights I've manaed to get the Greenhouse energy usage to : 260.46 kwh, instead of 325.55kwh

###### 07/26/2026:
    ♡ greenhouse habitat lighting will sync with the rest of the habitat when plant lighting is not producing light


###### 08/03/2026:
    ♡ separated habitat lighting into its own subsystem

    ♡ greenhouse lighting remains with the greenhouse subsystem