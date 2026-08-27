# Assembly Processors (UPA / WPA / BPA)
### General Notes:
    ♡ three main water recovery assemblies that form closed loop system, sharing the same control pattern
    
    ♡ units only run when the relevant tank exceeds the hysteresis threshold
    
    ♡ recovery rates are intentionally not perfect
    
    ♡ power and capacity numbers are intentionally conservative for V1

### ----------------------------------------

## Assembly Processors Plan (updated 08/22/2026):
### Layout
#### Water Recovery/Processing Rooms:
    ♡ shape: rectangle
    ♡ floor area: ~ 90 m²
    ♡ height: 4.5 m
    ♡ volume: ~ 405 m³
    ♡ minimum maintenance aisle width: ~ 1.2 m
    ♡ approximate dimensions: 
        ~ 10 m × 9 m × 4.5 m
    
    ♡ purpose:
        - all recovery and treatment work happens here

    ♡ access:
        - connects to the water storage room
        - connects to the ISRU water bay
        - connects to the utility hallway
        - receives condensate from habitat CHX and greenhouse CHX

    ♡ contains:
        - UPA and pretreatment
        - WPA
        - BPA
        - pumps, filters, catalytic reactors
        - sampling hardware
        - control cabinets
        - consumables storage
        - maintenance aisles

    ♡ calculation:
        10 m × 9 m 
        = ~ 90 m² floor area

        90 m² × 4.5 m 
        = ~ 405 m³ volume

### Shared Control Modes:
    ♡ offline: system off

    ♡ idle: 
        - ready but not enough water in the source tank yet (small fixed power)

    ♡ running: 
        - processes available mass up to capacity (power scales with load)

### WPA Processing Priority:
    ♡ 1. condensate
        - habitat CHX condensate
        - greenhouse CHX condensate
    ♡ 2. Sabatier produced water
    ♡ 3. gray water
    ♡ 4. raw ISRU water

### Recovery Rates:
    ♡ UPA: 0.87
    ♡ WPA: 0.95
    ♡ BPA: 0.90
    ♡ calculation: 
        - recovered water: 
            mass processed × recovery rate 
        
        - remaining waste/brine: 
            mass processed - recovered water

### Processing Capacity:
    ♡ UPA: 6.0 kg/h
    ♡ WPA: 80.0 kg/h
    ♡ BPA: 0.5 kg/h
    
    ♡ calculation: 
        - maximum available this step: 
            handling capacity × step duration in hours

### Power:
    ♡ base power
        - UPA: 0.45 kW
        - WPA: 0.80 kW
        - BPA: 0.25 kW

    ♡ power fraction:
        - UPA: 0.45
        - WPA: 0.50
        - BPA: 0.40
    
    ♡ idle power is a small fixed fraction of base power

    ♡ running power consists of a fixed baseline amount plus a load dependent amount

    ♡ calculation:
        - amount factor: 
        mass processed ÷ maximum available this step
        
        - baseline power: 
        base power × (1 - power fraction) 
        
        - power increase: 
        base power × power fraction × amount factor 
        
        - total running power: 
        baseline power + power increase

### Heat Output:        
    ♡ heat added to habitat:
        ≈ 85 % of electrical power

    ♡ calculation:
        processor heat: 
            electrical power × 0.85

### ----------------------------------------

## Design Evolution:
#### Early Recovery Rates:
    ♡ original UPA recovery ~ 0.94 but was lowered to 0.87 after researching

#### Power Logic:
    ♡ early versions used fixed power, updated to load proportional power

#### BPA Capacity:
    ♡ original capacity was 0.25 kg/h, was raised to 0.5 kg/h to keep up with 30-crew brine

### ----------------------------------------

## Future Considerations:
    ♡ 

### ----------------------------------------

## Design Decisions:
#### Why shared control pattern for all three?
    ♡ keeps code and behaviour consistent

    ♡ makes hysteresis and power scaling easy to change

    ♡ simplifies future low power modes

#### Why that specific priority order on WPA?
    ♡ condensate is the cleanest recoverable water
    
    ♡ gray water is most common
    
    ♡ raw ISRU water is last so it does not displace higher priority sources

#### Why BPA capacity of 0.5 kg/h?
    ♡ brine volume is much smaller than gray or black water

    ♡ low power and thermal impact
    
    ♡ it's enough to keep up with brine production from 30 crew

#### Why model heat as ~ 85 % of electrical power?
    ♡ it seemed simple and conservative for V1 thermal balance
    
    ♡ still captures the main heat contribution without needing detailed efficiency curves

### ----------------------------------------

### Dev Log Notes:
###### 04/22/2026:
    ♡ chose UPA / WPA / BPA after doing research on reusability

###### 04/23/2026
    ♡ adding condensate/CHX to water_system and engine and made OGA use potable water

###### 05/25/2026:
    ♡ added hysteresis and load proportional power logic

###### 08/18/2026:
    ♡ locked in recovery rates (UPA 0.87, WPA 0.95, BPA 0.90)

###### 08/20/2026:
    ♡ raised BPA handling capacity from 0.25 kg/h to 0.5 kg/h and added daily capacity calculations for water recovery

###### 08/22/2026:
    ♡ while I consider where to keep the Sabatier I'm going to move to the water processing assembly rooms, I want to avoid contamination, and for everything to stay clean overall, and to make maintenence easier, the potable water will have it's own clean room and area

    ♡ I considered keeping all the non-potable water tanks together, but I'd like the seperation between the ISRU raw water to have it's own area

###### 08/23/2026
    ♡ making the changes to move the water processing systems to have rooms to serperate by water quality and function

    ♡ sabatier.py: ch4_leaked_kpa is adding storage leak into cabin ch4_kpa, it should vent to Mars exterior per sabatier.md, not cabin atmosphere

        - decide: implement Sabatier to WPA water routing in water.py

        - new sabatier_water_storage_kg holding tank (like condensate)

        - stop adding sabatier_water_produced_kg directly in update_water_storages_kg()

