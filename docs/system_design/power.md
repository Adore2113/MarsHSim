# Power System
### General Notes:
    ♡ preliminary estimates

    ♡ solar generation powers the habitat and charges the primary battery

    ♡ excess energy is stored in a secondary long term battery bank

    ♡ available power decides which systems can operate normally or enter low power modes

### ----------------------------------------
 
## Habitat Power System Plan (updated 08/03/2026):
#### Primary Battery:
    ♡ current capacity: 25,000 kWh
    ♡ powers the habitat directly:
        -receives all generated solar energy first

        -when almost full, excess energy is sent to the secondary battery bank

        -enters low and critical power modes as charge decreases
    
    ♡ to do:
        - battery chemistry
        - figure out area for battery
        - mass
        - volume
        - charge/discharge limits
        - calculation showing how capacity was chosen

#### Secondary Battery Bank:
    ♡ current capacity: 1,500,000 kWh (1.5 GWh)
    ♡ long-term energy storage

    ♡ for long term habitat life with no resupply

    ♡ charges only after the primary battery reaches the charging threshold

    ♡ supplies energy back to the primary battery during shortages

    ♡ maintains a reserve except during emergency situations

    ♡ may increase to 2.0 GWh after longer testing

#### Battery Transfer:
    ♡ primary battery always has charging priority

    ♡ energy transfers between batteries are limited by a maximum transfer rate: 5000.0 kW

    ♡ charging and usage thresholds determine when transfers happen

    ♡ the secondary battery maintains a reserve during normal operation

    ♡ emergency conditions allow deeper use of the secondary battery

### ----------------------------------------

#### Subsystem Priority:
    ♡ priority 0:
        - oxygen generation
        - CO₂ scrubbing

    ♡ priority 1:
        - thermal control
        - water systems

    ♡ priority 2:
        - greenhouse
        - greenhouse lighting

    ♡ priority 3:
        - comfort systems
        - wellness lighting

    ♡ to do:
        - revisit this later

        - calculate kWh/sol budget for each priority

        - define exactly how each tier behaves mechanically

#### Power Modes:
    ♡ normal

    ♡ low:
        - dim habitat lighting (see lights.md)
        - disable wellness lights
        - maintain priority 0 and 1 systems

    ♡ critical/emergency:
        - reduce lighting to the minimum
        - prioritize oxygen generation and CO₂ scrubbing
        - reduce non essential systems (planned for future implementation)
    
     ♡ to do:
        - finalize battery thresholds

### ----------------------------------------

#### Deployable Equipment Power Interactions:
    ♡ to do: 
        - add heated pipe deploy/retract power draw and behavior during low power mode

        - open question (from 07/21/2026 dev log): if low power mode hits while pipes are 
        deployed, retracting doesn't currently cost power in V1, but leaving them deployed risks freezing or high heater draw 

        - decide if lower power should force retraction before entering low power, or accept the risk

### ----------------------------------------

#### Future Considerations:
    ♡ how much room/space the primary and backup banks will use
    
    ♡ finalize subsystem power priority calculations (kWh/sol per tier)

    ♡ finalize power mode transition thresholds (battery % or kWh)

    ♡ decide on heated pipe behavior during low power mode

    ♡ go over crew psychology / morale considerations with power availability (mentioned 07/22/2026 dev log)

    ♡ consider whether battery capacity needs to scale with the 50 acre solar plan's seasonal changes


### ----------------------------------------

### Design Evolution
#### Early Power System:
    ♡ battery capacity: 4000.0 kWh

    ♡ habitat lighting originally lived inside the power system

    ♡ later separated into its own subsystem

#### Early Lighting Assumptions:
    ♡ light level range:
        0.0 – 1.0

    ♡ minimum lighting:
        0.20

    ♡ daylight support:
        0.30

    ♡ emergency lighting:
        0.10

### ----------------------------------------

### Design Decisions:
#### Why use two battery systems?
    ♡ the solar field generates a ton of power that shouldn't be wasted

    ♡ I needed to consider long term energy storage

    ♡ it helps during prolonged dust storms, solar array regen and sols with low solar production

#### Why charge the primary battery first?
     ♡ the habitat should always maintain a highly available working battery

    ♡ excess energy can be safely stored once immediate operational needs are met

    ♡ reduces unnecessary cycling of the larger battery bank


#### Why use power modes?
    ♡ to follow the *future implemented* system priority tier system 

    ♡ allows the habitat to gradually reduce power consumption

    ♡ protects life support systems before reducing comfort systems

    ♡ avoids sudden complete shutdowns whenever possible

    ♡ allows future expansion for more advanced power management

#### Why increase the primary battery?
    ♡ the original battery became too small after the 50 acre solar field redesign

    ♡ again, the solar field generates a ton of power that shouldn't go to waste

    ♡ the habitat needs enough working storage to handle normal daily operation plus extra

    ♡ the larger secondary battery is intended for long term storage

### ----------------------------------------

### Dev Log notes:
###### 03/29/2026:
    ♡ battery capacity 4000.0 kWh

    ♡ started power_system.py

###### 04/10/2026:
    ♡ solar power will recharge habitat batteries

###### 05/25/2026:
    ♡ updating systems to include low power mode

###### 07/21/2026:
    ♡ considering whether heated pipes should retract automatically when low power begins, since leaving them deployed could require significant heating

###### 07/22/2026:
    ♡ started thinking more about long term power reserves and how power shortages affect crew psychology

###### 07/23/2026:
    ♡ average simulation before implementing the 50-acre solar field:
        - solar Generated: 559.26 kWh
        - total Energy Used: 649.12 kWh
        - net Energy: 89.86 kWh
    
###### 08/03/2026:
    ♡ increased the temporary primary battery capacity to 25,000 kWh

    ♡ set the secondary battery bank to 1,500,000 kWh (1.5 GWh) for long term habitat survival

    ♡ considering increasing the secondary battery bank to 2.0 GWh after longer testing

    ♡ added charging and usage thresholds for transfers between the primary battery and the secondary battery bank

    ♡ renamed battery_max_capacity_kwh to primary_battery_max_capacity_kwh

    ♡ separated habitat lighting into its own subsystem

    ♡ considering whether subsystem constants should remain together or be split into dedicated constants files