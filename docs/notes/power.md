# Power System
### General Notes:
    ♡ preliminary estimates

    ♡ solar generation powers the habitat and charges the primary battery

    ♡ excess energy is stored in a secondary long term battery bank

    ♡ available power decides which systems can operate normally or enter low power modes

### ----------------------------------------
 
## Habitat Power System Plan (updated 08/22/2026):
## Layout
#### Primary Battery Room:
    ♡ shape: rectangle
    ♡ floor area: ~ 110 m²
    ♡ height: 4.5 m
    ♡ volume: ~ 495 m³
    ♡ 4 seperate battery banks
    ♡ capacity per bank: ~ 6,250 kWh
    ♡ battery banks arranged symmetrically
    ♡ central maintenance and access area
    ♡ minimum maintenance aisle width: ~ 1.2 m
    ♡ approximate dimensions: 
        ~ 11 m × 10 m × 4.5 m

    ♡ access:
        - entrance into power distribution and transfer room

        - *to do*

#### Secondary Battery Corridor Layout:
    ♡ shape: rectangle
    ♡ total volume across all rooms: ~ 12,000 m³
    ♡ 12 isolated battery rooms
    ♡ each room: ~ 1,000 m³
    ♡ height: 5.5 m
    ♡ floor area per room: ~ 182 m²
    ♡ total floor area of all rooms: ~ 2,182 m²
    ♡ room dimensions: ~ 15.6 m × 11.7 m × 5.5 m
    ♡ complete area with hallway:  ~ 2,450 m²
    ♡ lower access priority
    
    ♡ central hallway with 6 battery rooms along each side

    ♡ each room can be isolated for maintenance or emergencies 

    ♡ access:
        - one end of the corridor connects to the power distribution and transfer room

        - the other end connects to a battery maintenance and service room with an emergency exit

        - the primary battery room connects through the power distribution and transfer room instead of directly into the corridor

#### Power Distribution and Transfer Room:
    ♡ shape: rectangle
    ♡ floor area: ~ 70 m²
    ♡ height: 4.5 m
    ♡ volume: ~ 315 m³
    ♡ approximate dimensions: 
        ~ 10 m × 7 m × 4.5 m

    ♡ access:
        - entrance into the secondary battery corridor
   
        - connects the primary battery room to the secondary battery corridor

    ♡ contains:
        - battery transfer equipment
        - power converters
        - monitoring and control equipment
        - main breakers
        - electrical isolation equipment
        - connections between the primary and secondary battery bank and habitat power distribution

#### Battery Maintenance and Service Room:
    ♡ shape: rectangle
    ♡ floor area: ~ 120 m²
    ♡ height: 5.5 m
    ♡ volume: ~ 660 m³
    ♡ approximate dimensions: ~ 12 m × 10 m × 5.5 m
    ♡ separate equipment access
    ♡ used for inspecting, testing and replacing battery-system components

    ♡ access:
        - far end of the secondary battery corridor
        - *to do*

    ♡ contains:
        - diagnostic equipment
        - insulated tools
        - replacement component things
        - lifting and handling equipment
        - temporary space for components removed from the battery rooms

### ----------------------------------------

#### Primary Battery:
    ♡ current capacity: 25,000 kWh
    ♡ powers the habitat directly:
        -receives all generated solar energy first

        -when almost full, excess energy is sent to the secondary battery bank

        -enters low and critical power modes as charge decreases
    
    ♡ to do:
        - battery chemistry
        - charge/discharge limits
        - calculation showing how capacity was chosen

#### Secondary Battery Bank:
    ♡ current capacity: 1,500,000 kWh (1.5 GWh)

    ♡ charges only after the primary battery reaches the charging threshold

    ♡ supplies energy back to the primary battery during shortages

    ♡ maintains reserve except during emergency situations

    ♡ final capacity will be reconsidered after longer simulation testing and completion of the habitat power system

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
        0.0-1.0

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

#### Why use power modes?
    ♡ to follow the *future implemented* system priority tier system 

    ♡ lets the habitat gradually reduce power

    ♡ protects life support systems before reducing comfort systems

    ♡ avoids sudden complete shutdowns whenever possible

    ♡ allows future expansion for more advanced power management

#### Why increase the primary battery?
    ♡ the original battery became too small after the 50 acre solar field redesign

    ♡ again, the solar field generates a ton of power that shouldn't go to waste

    ♡ the habitat needs enough working storage to handle normal daily operation plus extra

    ♡ the larger secondary battery is intended for long term storage

#### Why this Primary battery size and layout?
    ♡ 25,000 kWh leaves a comfortable buffer 

    ♡ I figured a room dedicatd to this didn't need to be massive

    ♡ four sections makes sense for easier maintenance and emergency containment

    ♡ short cable runs and easy access are priorities for the working battery

#### Why this seconadary battery size and layout?
    ♡ 1.5 GWh is sized for long term storage for times where a lot of power won't be generated from different situations like brutal dust storms, emergencies, etc.

    ♡ 12,000 m³ total volume at ~ 125 kWh/m³ seems realistic

    ♡ 12 isolated rooms of ~ 1,000 m³ each let individual sections taken offline at at time

    ♡ rooms along a hallway are easier to maintain and isolate than one large space and it seems neater and for easy access

    ♡ I figured the backup could be secondary when considering most convenient access as far as layout goes

    ♡ each room has independent fire isolation, thermal monitoring, electrical isolation, and suppression

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

    ♡ set the secondary battery bank to 1,500,000 kWh (1.5 GWh) store excess solar generation and for long term habitat survival

    ♡ considering increasing the secondary battery bank to 2.0 GWh after longer testing

    ♡ added charging and usage thresholds for transfers between the primary battery and the secondary battery bank

    ♡ renamed battery_max_capacity_kwh to primary_battery_max_capacity_kwh

    ♡ separated habitat lighting into its own subsystem

    ♡ considering whether subsystem constants should remain together or be split into dedicated constants files

###### 08/22/2026:
     ♡ not every room in the habitat is going to be an octagon shape, only the areas that would be better for effiency and space

    ♡ I'm now looking into the power storage rooms, if I get the size of the subsystems figured out I can get the net habitat volume and then make my calculations include real values instead of a placeholder

    ♡ breaking the secondary power storage into multiple smaller rooms or pod areas seems like it would be neater, less overwhelming in emergencies, easier to maintain and easier to isolate issues if they came up later

    ♡ for the secondary battery storage, I'm picturing a hallway with walls that act like partitioners, so you can walk down the hallway, and on the sides there would be like.. rooms/bays/pods with:
            - rows of tall metal battery cabinets or racks
            - smaller rectangular battery modules inserted into those racks
            - thick electrical cables, etc.
            - coolant pipes and manifolds
            - battery management electronics
            - breakers and electrical isolation equipment
            - fire detection and suppression equipment
            - narrow but not too narrow maintenance aisles between rack rows
    
    each area would have it's own fire resistant walls and doors, independent thermal monitoring, independent electrical isolation, controlled ventilation, its own suppression system and no unrestricted airflow into the central corridor
                
    ♡ I was thinking a backup battery can be allowed to be in a more inconvenient spot, meaning it can be a lesser priority for easiest access areas, I want this area to be quite compact, and not too high because I want this to be clean, easy and boring to walk through

    ♡ if I make each area about 1,000 m³, and the corridor about 4 m wide, with six rooms on each side, so 12 in total, that would be around the size of a medium size-ish grocery store

    ♡ I'm picturing a specific grocery store that I go to in town, considering the main floor space, not including employee only areas,  1.5 GWh battery capacity in 12 isolated battery ares, that would be around tree quarters of the shopping area, it should lead into another room, but not be the main door b/c it's small 
    
    ♡ by "system level energy density: ~ 125 kWh/m³" under the secondary batter bank physical layout, I am talking about much battery capacity fits in the complete installed battery system with supporting equipment and maintenance space

    ♡ for the main battery room doesn't need to be huge and can be a taller industrial room, though, I think that there should be seperate battery areas that can be seperated and isolated for maintentence and for emergency handling
