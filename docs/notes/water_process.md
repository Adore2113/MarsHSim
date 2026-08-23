# Assembly Processors (UPA / WPA / BPA)
### General Notes:
    ♡ three core water recovery assemblies that form closed loop system
    
    ♡ all three share the same control pattern
    
    ♡ units only run when the relevant tank exceeds the hysteresis threshold
    
    ♡ recovery rates are intentionally non-perfect
    
    ♡ power and capacity numbers are intentionally conservative for V1

### ----------------------------------------

## Assembly Processors Plan (updated 08/22/2026):
### Layout:
    ♡ shape: rectangle
    ♡ floor area: ~ 90 m²
    ♡ height: 4.5 m
    ♡ volume: ~ 405 m³
    ♡ minimum maintenance aisle width: ~ 1.2 m
    ♡ approximate dimensions: 
        ~ 10 m × 9 m × 4.5 m

    ♡ processing layout:
        - UPA and pretreatment equipment are together
        - BPA is near the UPA and brine connections
        - WPA is on the cleaner side of the room
        - sampling hardware is near the WPA output
        
        - pumps, filters and control cabinets are around the processing systems

        - central maintenance area provides access to all systems

    ♡ access:
        - connects to the water storage room
        - connects to the utility hallway

    ♡ contains:
        - UPA and pretreatment equipment
        - WPA
        - BPA
        - pumps
        - filters
        - catalytic reactors
        - sampling hardware
        - control cabinets
        - consumables
        - maintenance aisles

    ♡ calculation:
        10 m × 9 m
        = ~ 90 m² floor area
        
        90 m² × 4.5 m
        = ~ 405 m³ volume


### Shared Control Modes:
    ♡ offline: 
        - system off

    ♡ idle:
        - unit is ready, but there isn't enough water in the source tank yet

        - uses a small fixed fraction of base power

    ♡ running:
        - processes available mass up to its processing capacity

        - power scales with the fraction of available processing capacity being used

### WPA Processing Priority:
    ♡ 1. condensate
    ♡ 2. gray water
    ♡ 3. raw ISRU water

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
    
    ♡ capacity is converted to the amount that can be processed during the current simulation step

    ♡ calculation: 
        - maximum available this step: 
            handling capacity × step duration in hours
        
        - daily processing capacity:
            88,775.244 s/sol ÷ 3,600 s/h
            ≈ 24.66 h/sol
            
            0.5 kg/h × 24.66 h/sol
            ≈ 12.33 kg/sol

### Power:
    ♡ base power
        - UPA: 0.45 kW
        - WPA: 0.80 kW
        - BPA: 0.25 kW

    ♡ power fraction:
        - UPA: 0.45
        - WPA: 0.50
        - BPA: 0.40
    
    ♡ running power consists of a fixed baseline amount plus a load dependent amount
    
    ♡ the load dependent amount increases with the amount of the processor's available capacity being used
    
    ♡ idle power is a small fixed fraction of base power

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
    ♡ heat added to the habitat thermal balance is modeled as ~ 85% of processor electrical power
    
    ♡ heat output changes with processor power use
    
    ♡ calculation:
        processor heat: 
            electrical power × 0.85

### ----------------------------------------

## Design Evolution:
#### Early Recovery Rates:
    ♡ original UPA recovery was higher at ~ 0.94
    ♡ lowered to 0.87 after researching more

#### Power Logic:
    ♡ early versions used fixed power
    ♡ updated to load proportional power (baseline + variable portion)

#### BPA Capacity:
    ♡ original capacity was 0.25 kg/h

    ♡ raised to 0.5 kg/h so the unit can keep up with brine from 30 crew without long term accumulation

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

###### 05/25/2026:
    ♡ added hysteresis and load proportional power logic

###### 08/18/2026:
    ♡ locked in recovery rates (UPA 0.87, WPA 0.95, BPA 0.90)

###### 08/20/2026:
    ♡ raised BPA handling capacity from 0.25 kg/h to 0.5 kg/h and added daily capacity calculations for water recovery