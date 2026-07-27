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

#### Main Lighting Schedule:
    ♡ crew awake hours: 06:00–21:30 LMST
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
        - sunlight dimming = sunlight amount × 0.6
        - adjusted light level = base light level - sunlight dimming
        - final light level = max(0.2, adjusted light level)


### ----------------------------------------

#### Wellness Lighting Operation:
    ♡ activation trigger: 3 consecutive low sunlight sols
    ♡ deactivation trigger: 1 or fewer consecutive low sunlight sols
    ♡ previous state maintained at: 2 consecutive low sunlight sols
    ♡ power while active: 0.5 kW
    ♡ heat output while active: 0.1 kW
    ♡ calculation:
        - active power:
            0.5 kW × 1.0 = 0.5 kW
        - active heat:
            0.1 kW × 1.0 = 0.1 kW
        - maximum energy if active for 24 hours:
            0.5 kW × 24 hours = 12.0 kWh/sol
        - maximum heat energy if active for 24 hours:
            0.1 kW × 24 hours = 2.4 kWh/sol


### ----------------------------------------

#### Greenhouse Plant Lights:
    ♡ artificial grow lights
    ♡ plant lights are separate from main habitat lights
    ♡ total effective grow area: not finalized
    ♡ LED power density: 0.12 kW/m²
    ♡ LED heat ratio: 0.68
    ♡ full LED light level: 1.0
    ♡ calculation:
        - full LED power:
            effective grow area × 0.12 kW/m²
        - LED heat output:
            full LED power × 0.68
        - full cycle energy:
            full LED power × 16 hours

#### Greenhouse Plant Lighting Schedule:
    ♡ plant light start time: 05:00 LMST
    ♡ plant light end time: 21:00 LMST
    ♡ full plant light period: 16 hours/sol
    ♡ dark cycle: 8 hours/sol
    ♡ calculation:
        - plant light end:
            05:00 + 16 hours = 21:00 LMST
        - dark cycle:
            24 hours - 16 hours = 8 hours

#### Greenhouse Plant Lighting Modes:
    ♡ dark cycle:
        - plant LED level: 0.0

    ♡ full LED support:
        - used when effective sunlight is at or below 0.15 kW/m²
        - plant LED level: 1.0

    ♡ LED support:
        - used when sunlight is useful but below the plant light target
        - LED level changes according to the remaining light requirement

    ♡ sunlight only:
        - used when effective natural sunlight meets or exceeds the light target
        - plant LED level: 0.0

    ♡ calculation:
        - effective natural light:
            natural light per m² × light absorption × day-length bonus

        - partial LED support:
            (light target - effective natural light) ÷ light target


#### Greenhouse Habitat Lighting:
    ♡ greenhouse habitat lighting is currently part of the main habitat light system
    ♡ while greenhouse plant lights are producing light:
            - greenhouse habitat lights remain off
    ♡ when greenhouse plant lights are off:
            - follows the current habitat light level
            - follows the current habitat power mode
    ♡ calculation:
        - plant lights producing light:
                greenhouse habitat light level = 0.0

        - plant lights not producing light:
                greenhouse habitat light level = adjusted habitat light level


### ----------------------------------------

#### Low Power Operation:
    ♡ main habitat lighting is reduced during low and critical power modes
    ♡ wellness lighting is disabled during low and critical power modes
    ♡ greenhouse plant lighting is reduced separately by the greenhouse system

#### Low Power Mode:
    ♡ main habitat light multiplier: 0.5
    ♡ wellness light level: 0.0
    ♡ greenhouse plant light multiplier: 0.6
    ♡ calculation:
        - main lights:
                adjusted light level × 0.5
        - wellness lights:
                1.0 × 0.0 = 0.0
        - greenhouse plant lights:
                LED level × 0.6

#### Critical Power Mode:
    ♡ main habitat light multiplier: 0.3
    ♡ wellness light level: 0.0
    ♡ greenhouse plant light multiplier: 0.2
    ♡ calculation:
        - main lights:
            adjusted light level × 0.3
        - wellness lights:
            1.0 × 0.0 = 0.0
        - greenhouse plant lights:
            LED level × 0.2

### ----------------------------------------

#### Future Considerations:
    ♡ calculate the total habitat floor area

    ♡ separate habitat lighting into physical zones

    ♡ calculate the greenhouse habitat lighting area separately

    ♡ replace preliminary lighting capacity values with area based calculations

    ♡ consider separate lighting levels for:
        -crew living areas
        -work areas
        -corridors
        -maintenance areas
        -sleeping areas

    ♡ give wellness lights the same turn off schedule for night time

### ----------------------------------------

### Lighting Design Decisions:
#### Why wellness lights?
    ♡ I considered seasonal changes on Earth and how people can be affected by long periods without enough natural sunlight

    ♡ for morale/wellness reasons I wanted to incorporate a sort of SAD lighting idea but for the whole habitat
    
    ♡ mock sunlight is better than no sunlight during
      prolonged dark periods

#### Why timed greenhouse lights?
    ♡ constant lights were taking up too much power (this was before my upgraded 50acre solar plan)

    ♡ plants require a controlled photoperiod rather than continuous lighting

    ♡ timed lighting allows crops to receive consistent lighting even when natural daylight changes by season

    ♡ the dark cycle gives crops a regular period without plant lighting

    ♡ natural sunlight can reduce the amount of LED support required during the scheduled light period

#### Why sync greenhouse habitat lights?
    ♡ greenhouse plant lights already provide visibility while they are active

    ♡ keeping the habitat lights off during that time avoids unnecessary duplicate lighting

    ♡ when the plant lights are off, the greenhouse follows the same lighting conditions as the rest of the habitat


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