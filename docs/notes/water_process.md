# Assembly Processors (UPA / WPA / BPA)
### General Notes:
    ♡ three core water recovery assemblies that form closed loop system
    
    ♡ all three share the same control pattern
    
    ♡ units only run when the relevant tank exceeds the hysteresis threshold
    
    ♡ recovery rates are intentionally non-perfect
    
    ♡ power and capacity numbers are intentionally conservative for V1

### ----------------------------------------

## Assembly Processors Plan:
### Shared Control Logic:
    ♡ modes:
        - offline: 
            ♡ unit off

        - idle:
            ♡ unit is ready to run, but there isn't enough water in the source tank yet

            ♡ uses a small fixed fraction of base power

        - running:
            ♡ processes available mass up to its processing capacity

            ♡ power scales with the fraction of available processing capacity being used
    
    ♡ hysteresis prevents processors from repeatedly switching between idle and running when tank inventory is close to the operating threshold

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
        maximum available this step: 
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
    
    ♡ running power consists of a fixed baseline amount plus a load dependent amount
    
    ♡ the load dependent amont increases to the amount of the processor's available capacity being used
    
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
    ♡ BPA capacity changed from 0.25 kg/h to 0.5 kg/h

### ----------------------------------------

## Future Considerations:
    ♡ 

### ----------------------------------------

## Design Decisions:
### 

### ----------------------------------------

### Dev Log Notes:
#####