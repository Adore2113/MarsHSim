# Assembly Processors (UPA / WPA / BPA)
### General Notes:
    ♡ three core water recovery assemblies that form closed loop system
    
    ♡ all three share the same control pattern
    
    ♡ units only run when the relevant tank exceeds the hysteresis threshold
    
    ♡ recovery rates are intentionally non-perfect
    
    ♡ power and capacity numbers are intentionally conservative for V1

### ----------------------------------------

## Assembly Processors Plan ():
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
    


### ----------------------------------------

## Design Evolution:
###

### ----------------------------------------

## Future Considerations:
    ♡ 

### ----------------------------------------

## Design Decisions:
### 

### ----------------------------------------

### Dev Log Notes:
#####