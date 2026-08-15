# Greenhouse Water:
### General Notes:
    ♡ calculations are performed separately for each zone

    ♡ each zone uses averaged plant data instead of simulating individual crops

    ♡ V1 uses treated habitat water for greenhouse make up water and assumes greenhouse nutrients are supplied separately

### ----------------------------------------
## Greenhouse Water Model (08/15/2026):
## Plant Water Demand:

## Greenhouse Water Model:
#### Water Use:
    ♡

### ----------------------------------------

#### Water Recirculation:
    ♡

### ----------------------------------------

## Runoff:
    ♡ runoff ratio: 0.08 (8% of water needed)

    ♡ represents nutrient solution that drains from the plant containers
    
    ♡ this water is collected and returned to the greenhouse nutrient reservoirs
    
    ♡ currently included in the overall recirculation numbers

### ----------------------------------------

#### Transpiration and Plant Mass:
    ♡ water taken up by plants:
        - 85% becomes transpiration (goes into the greenhouse air and then the CHX)

        - 15% stays in plant mass (permanent loss)

    ♡ calculation:
        - transpiration: 
            plant water uptake × 0.85

        - plant mass water:
            plant water uptake × 0.15

### ----------------------------------------

## Make-up Water System:
    ♡ all three reservoirs are topped up from a shared clean water supply

    ♡ loop:
        1. habitat potable / treated water
        2. greenhouse make-up water
        3. zone valves
        4. nutrient reservoir

    ♡ make-up only happens when a reservoir drops to 70%

    ♡ the greenhouse only draws the actual volume needed to return to normal level

    ♡ this is the main ongoing water demand the greenhouse places on the habitat

### ----------------------------------------

## Full Water / Waste Loop (Future):
    ♡ concept only — not modeled in V1

    ♡ planned loop:
        - crew waste
        - water treatment (UPA / WPA)
        - potable water
        - greenhouse nutrient solution
        - plants
        - greenhouse humidity
        - CHX water capture
        - back into the water system

    ♡ pros:
        - massive water recycling
        - reduces the need for replacement water

### ----------------------------------------

## Design Evolution:
    ♡ each zone has its own efficiency:
        - structural: 82%
        - container: 88%
        - rack: 94%

    ♡ the water taken up by plants is what actually leaves the recirculating loop

    ♡ water requirements are calculated by zone:

        ♡ structural:
            - base water: 3.4 kg/m²/sol
            - multiplier: 1.15
            - effective rate ≈ 3.91 kg/m²/sol

        ♡ container:
            - base water: 2.6 kg/m²/sol
            - multiplier: 1.00
            - effective rate ≈ 2.6 kg/m²/sol

        ♡ rack:
            - base water: 1.95 kg/m²/sol
            - multiplier: 0.90
            - effective rate ≈ 1.76 kg/m²/sol

### ----------------------------------------

## Future Considerations:
    ♡ figure out runoff water and model separately

     ♡ implement: the full crew waste to water recovery to nutrient recovery to greenhouse loop

### ----------------------------------------

## Design Decision:
#### 
    ♡ 
    
### ----------------------------------------

### Dev Log Notes:
###### 08/12/2026
    ♡ included make-up water system for hydroponic reservoirs