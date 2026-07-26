# Power System
### General Notes:
    ♡ 

### ----------------------------------------
#### Battery Storage:
    ♡ 

### ----------------------------------------
# Lighting:
### General Notes:
    ♡ preliminary estimates
    ♡ habitat lighting is modeled as one combined electrical load
    ♡ individual lights and fixtures are not simulated for V1
    ♡ light level is represented from 0.0–1.0
    ♡ light power use and heat output change with the current light level
    ♡ natural sunlight reduces the amount of artificial lighting required
    ♡ main habitat lighting and wellness lighting are modeled as separate loads

### ----------------------------------------
### Habitat Lighting Plan (03/29/2026):
    ♡ 

### ----------------------------------------
#### Lighting System:
    ♡ 

    ♡ planned automatic lighting schedule:
            -brighten at 6:00 AM
            -dim at 9:30 PM (21:30)

    ♡ adaptive lighting based on available sunlight

    ♡ Low Power Lighting:
        -habitat lighting is automatically dimmed during low power modes
        -wellness lighting is disabled
        -habitat lighting stays on at reduced brightness

### ----------------------------------------
#### Wellness Lighting:
    ♡ wellness lighting is separate system from the main habitat lights
    ♡ intended to support crew comfort and moral during longer periods of low to no natural sunlight

    ♡ activation:
        - turns on after 3 consecutive low sunlight sols
        - turns off when the streak falls to 1 sol or less
        - at 2 low-sunlight sols, it keeps its previous on/off state

    ♡ light level while active:
          1.0

    ♡ light level while inactive:
          0.0

    ♡ power:
          base_w_light_power_kw × wellness_light_level

    ♡ heat added:
          base_w_light_heat_kw × wellness_light_level

    ♡ energy used per timestep:
          w_light_power_used_kw × timestep_hours


### ----------------------------------------
#### Future Considerations:
        ♡ start looking into realistic battery reserves and how much space they take up
        
        ♡ figure out a subsystem power priority system:
            -priority 0:
                -oxygen generation
                -CO₂ scrubbing

            -priority 1:
                -thermal control
                -water systems

            -priority 2:
                -greenhouse
                -lighting support

            -priority 3:
                -comfort systems
                -wellness lighting


### ----------------------------------------
### Early Power System Ideas:

#### Battery Plan:
        ♡ battery capacity: 4000.0 kWh

#### Low Power Mode:
        ♡ normal

        ♡ low:
            -dim habitat lighting
            -disable wellness lights
            -maintain life support and other essential systems

        ♡ critical/emergency:
            -reduce lighting to the minimum
            -prioritize the OGA and CO₂ scrubbers
            -reduce non-essential systems (planned for future implementation)

#### Lighting:
        ♡ light level goes from 0-1

        ♡ minimum light levels:
            -daytime support: 0.30 (when sufficient sunlight is available)
            -minimum lighting: 0.20
            -emergency lighting: 0.10 (during severe power shortages, if sufficient sunlight is available)


### ----------------------------------------
### Power System Notes:
###### 03/29/2026:
        ♡ battery capacity 4000.0 kWh

###### 04/05/2026:
        ♡ the lighting function will react and adjust to the level of daylight

###### 04/10/2026:
        ♡ solar power will recharge habitat batteries

###### 05/25/2026:
        ♡ updating systems to include low power mode

###### 07/21/2026:
        ♡ considering if all of a sudden the pipes are deploying and the low power mode hits or I lose power if the pipes don't retract, they will freeze or use a lot of power w. the heated pipes, but retracting doesn't use power in v1, which I'm questioning now

###### 07/22/2026:
        ♡ today I was thinking about my power reserves and power set up, I am really starting to consider what can ruin my simulation and I need to consider more of a crew psycholoy as well

###### 07/23/2026:
        ♡ my sim is running on average:  Solar Generated = 559.26 kwh, Total Power Used = 649.12 kWh, Net Energy = -89.86 kWh

        ♡ I isolated the subsystems and the greenhouse power is taking up a high percentage of the power, I have it set up to be running w. daylight, but now I'm thinking about having the lights on a 12 hour cycle

        ♡ finished updating the greenhouse lights, at 16 base hours for the greenhouse lights I've manaed to get the Greenhouse energy usage to : 260.46 kwh, instead of 325.55kwh
