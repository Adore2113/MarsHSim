# Power System
### General Notes:
    ♡ preliminary estimates

    ♡ to do: 
        - summary of how battery, solar, and subsystem loads interact (after battery sizing and priority tiers are finalized)

    ♡ solar generation charges the habitat battery

### ----------------------------------------
 
## Habitat Power System Plan (date TBD):
#### Battery Storage:
    ♡ current battery capacity: 4000.0 kWh (03/29/2026)
    ♡ to do: chemistry/type, mass, volume, charge/discharge rate limits
    ♡ to do: calculation for how capacity of 4000.0 kWh was chosen
    ♡ to do: calculations for expected days of autonomy at average vs. worst-case (dust storm) solar input


### ----------------------------------------

#### Subsystem Power Priority:
    ♡ figure out a subsystem power priority system:
        - priority 0:
            -oxygen generation
            -CO₂ scrubbing
        - priority 1:
            -thermal control
            -water systems
        - priority 2:
            -greenhouse
            -lighting support
        - priority 3:
            -comfort systems
            -wellness lighting
    ♡ to do: calculation for kWh/sol budget per priority tier
    ♡ to do: define what a tier actually does mechanically (hard cutoff vs. gradual reduction)

#### Power Modes:
    ♡ Treat the multiplier versions in lights.md as current values
    ♡ normal
    ♡ low:
        - dim habitat lighting (see lights.md low power multiplier: 0.5x)
        - disable wellness lights
        - maintain life support and other priority 0/1 systems
        - to do: calculation for battery % or kWh threshold that triggers low power mode
    ♡ critical/emergency:
        - reduce lighting to the minimum (see lights.md critical multiplier: 0.3x)
        - prioritize the OGA and CO₂ scrubbers above all else
        - reduce non essential systems (planned for future implementation)
        - to do: calculations for battery % or kWh threshold that triggers critical mode


### ----------------------------------------

#### Deployable Equipment Power Interactions:
    ♡ to do: 
        - add heated pipe deploy/retract power draw and behavior during low power mode
        - open question (from 07/21/2026 dev log): if low power mode hits while pipes are deployed, retracting doesn't currently cost power in V1, but leaving them deployed risks freezing or high heater draw 
        - decide: force retraction before entering low power, or accept the risk



### ----------------------------------------
#### Future Considerations:
    ♡ start looking into realistic battery reserves and how much space they take up
    
    ♡ finalize subsystem power priority calculations (kWh/sol per tier)

    ♡ finalize power mode transition thresholds (battery % or kWh)

    ♡ decide on heated pipe behavior during low power mode

    ♡ go over crew psychology / morale considerations with power availability (mentioned 07/22/2026 dev log)

    ♡ consider whether battery capacity needs to scale with the 50 acre solar plan's seasonal changes


### ----------------------------------------
### Early Power System Ideas:
    ♡ light level range: 0–1
    ♡ minimum light levels:
        - daytime support: 0.30 (when enough sunlight is available)
        - minimum lighting: 0.20
        - emergency lighting: 0.10 (severe power shortages, if enough sunlight is available)

    ♡ battery capacity: 4000.0 kWh

### ----------------------------------------
### Power System Notes:
###### 03/29/2026:
    ♡ battery capacity 4000.0 kWh

###### 04/10/2026:
    ♡ solar power will recharge habitat batteries

###### 05/25/2026:
    ♡ updating systems to include low power mode

###### 07/21/2026:
    ♡ considering if all of a sudden the pipes are deploying and the low power mode hits or I lose power if the pipes don't retract, they will freeze or use a lot of power w. the heated pipes, but retracting doesn't use power in v1, which I'm questioning now

###### 07/22/2026:
        ♡ today I was thinking about my power reserves and power set up, I am really starting to consider what can ruin my simulation and I need to consider more of a crew psycholoy as well

###### 07/23/2026:
        ♡ my sim is running on average:  Solar Generated = 559.26 kwh, Total Power Used = 649.12 kWh, Net Energy = -89.86 kWh (BEFORE IMPLEMENTING 50 ACRE SOLAR PLAN)
