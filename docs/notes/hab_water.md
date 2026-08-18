# Habitat Water System
### General Notes:
    ♡ water demands are slightly over estimated becuase I would rather overestimate than under when it comes to values of usage/demand

    ♡

    ♡

### ----------------------------------------

## Arcadia Water System Plan (08/18/2026):
#### Layout
##### Water Recovery/Processing Room:
    ♡ shape: octagon (regular)
    ♡ floor area: 90 m²
    ♡ total height: 4.5 m
    ♡ width: 
        ~ 10.4 m across opposite walls

    ♡ wall length:
        ~ 4.3 m for each outside wall

    ♡ center distance:
        ~ 5.2 m from the center to each wall

    ♡ corner distance:
        ~ 5.6 m from the center to each corner

    ♡ overall corner to corner width:
        ~ 11.3 m from one corner to the opposite corner

    ♡ roof: lightly angled

    ♡ entrances: 
        two (one from the direct hallway to social hub, one from the greenhouse connection)

    ♡ contains processors and working equipment for water recovery/proccessing:
        - UPA + pretreatment
        - WPA (including gray water and condensate)
        - BPA
        - pumps, filters, catalytic reactors, etc.
        - sampling / water quality hardware
        - control cabinets
        - consumables storage
        - maintenance aisles and extra space

##### Water Storage Room:
    ♡ shape: octagon (regular)
    ♡ floor area: 120 m²
    ♡ total height: 4.5 m
    ♡ width: 
        ~ 12.0 m across opposite walls

    ♡ wall length (if octagon):
        ~ 5.0 m for each outside wall

    ♡ roof: 
        flat or lightly angled

    ♡ entrances: recovery / Processing Room, one from the direct hallway / social hub side

    ♡ contains vertical cylindrical habitat water tanks

    ♡ notes:
        - tanks are fully inside the pressurized, heated volume (V1)

        - clear access for inspection, sensors, and maintenance

        - separated from equipment so the process flow stays clean

        - greenhouse keeps only its own local zone reservoirs

### ----------------------------------------

#### Tank Capacities
    ♡ potable water storage capacity: 10,000.0 kg
    ♡ gray water storage capacity: 3,500.0 kg
    ♡ black water storage capacity: 1,800.0 kg
    ♡ condensate storage capacity: 5,000.0 kg
    ♡ brine storage capacity:1000.0 kg
    ♡ raw ISRU water: 4,000 kg capacity
    ♡ greenhouse reservoirs (total): ~ 2,000 kg
        - see greenhouse\hydroponics.md
   
#### Crew Water Demands: 
    ♡ demand total: ≈ 1,450 kg/sol, 
        - ~ 2,660 kg/sol (as a max theoretical)

    ♡ shower system:
        - normal mode: 
            10 min recommended, 20 min cut off
        - conservation mode: 7–10 min
        - low water mode: 5 min
        - critical mode: timed preset buttons, enforcing a navy type shower (very short, low flow)
    
    ♡ breakdown (kg/person/sol):
        - drinking + food rehydration: 
            ♡ 2.5 kg/person/sol
            ♡ total ≈ 75.0 kg/sol

        - personal hygiene (sink, face, hands, oral)
            ♡ 1.2 kg/person/sol
            ♡ total ≈ 36 kg/sol

        - shower:
            ♡  40 kg/person/sol
            ♡ total ≈ 1,200 kg/sol

        - shared laundry:
            ♡  3.0 kg/person/sol
            ♡ total ≈ 90 kg/sol

        - toilet:
            ♡ 0.5 kg/person/sol
            ♡ total ≈ 15kg/sol
        
        - misc:
            ♡ 0.5 kg/person/sol
            ♡ total ≈ 15kg/sol

        - steam room (for future reference):
             0.8 kg/person/sol
            ♡  total ≈ 24 kg/sol

#### 
    ♡ 

### ----------------------------------------

#### 
    ♡ 

    ♡

    ♡
### ----------------------------------------

## Design Evolution:
    ♡ original  tank capacities:  
        - potable water storage capacity: 6500.0 kg
        - gray water storage capacity: 1200.0 kg
        - black water storage capacity: 800.0 kg
        - condensate storage capacity: 250.0 kg
        - brine storage capacity: 400.0 kg

    ♡

    ♡
### ----------------------------------------

## Future Considerations:
    ♡ 
    
    ♡

    ♡

    ♡
### ----------------------------------------

## Design Decisions:
#### 
    ♡

    ♡

    ♡
### ----------------------------------------

### Dev Log Notes:
###### 03/13/2026
    ♡ figure out how much water(H2O) the OGA and water electrolysis uses every time it runs, I'm going to find the fixed reaction ratio instead of a fixed ratio b/c the amount of O₂ produced are going to change depending on habitat events

    ♡ going to use 1000kg of water to start as a placeholder to finish the OGA functions

    ♡ going to keep the OGA functions separate instead of one big function w. a comment to sort of group them together, I feel like that will be better for future readability

    ♡ finished OGA and water electrolysis for now, moving onto argon and nitrogen

##      03/24/2026
    ♡ I chose the starting amounts for some power variables and made a separate file for the OGA and water electrolysis

##      04/22/2026
    ♡ doing some research before starting water_system.py to know what kind of water system makes sense w. focus on reusability

    ♡ going w.:
        -Urine Processor Assembly (UPA)
        -Water Processor Assembly (WPA)
        -Brine Processor Assembly (BPA)

    ♡ worked on the water system file

    ♡ I read about In-Situ Resource Utilization (ISRU) to extract water locally but I'll worry about that later
