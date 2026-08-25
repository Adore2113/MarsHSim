# CO₂ Scrubbing (Amine Swing Beds) 
### General Notes:
    ♡ removes CO₂ from the cabin atmosphere

    ♡ uses amine swing beds to absorb, regenerate, and cycle

    ♡ multiple beds so some can adsorb while others regenerate

    ♡ includes primary beds and backups

### ----------------------------------------
## CO₂ Scrubbing Plan (updated 08/24/2026):

### Layout
    ♡ beds and support equipment are part of the atmosphere / resource area
    
    ♡ see atmosphere.md for room placement and connections

### Beds
    ♡ total beds: 8
    ♡ min beds online: 2
    
    ♡ stored as a list so individual beds can be "online" or "standby"
    
    ♡ number of beds online is calculated from CO₂ load

### Operating Modes / States (per bed or system)
    ♡ offline
    ♡ standby / idle
    ♡ adsorbing (removing CO₂)
    ♡ regenerating
    ♡ (optional) limited / emergency behaviour later

### Operating Logic
    ♡ CO₂ above target decides how many beds are needed:
        - ≤ 0.0 kPa above target: 0 beds
        - > 0.012 kPa: 1 bed
        - > 0.03 kPa: 2 beds
        - > 0.06 kPa: 3 beds
        - > 0.12 kPa: 4 beds
        - > 0.25 kPa: 5 beds
        - > 0.50 kPa: 6 beds

    ♡ hysteresis:
        - co2_hysteresis_for_on = 0.05
        - co2_hysteresis_for_off = 0.03
        - once any beds are online, at least 1 stays online until CO₂ drops below target minus the off hysteresis

    ♡ cannot remove more CO₂ than currently exists above target

    ♡ scrubbed CO₂ is converted to kg and added to CO₂ stored for Sabatier/storage

### ----------------------------------------

## Design Evolution:
####

### ----------------------------------------

## Future Considerations:
    ♡ 

### ----------------------------------------

## Design Decisions:
#### 

### ----------------------------------------

### Dev Log Notes:
######