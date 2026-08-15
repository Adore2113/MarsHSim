# Greenhouse Water:
### General Notes:
    ♡ water is calculated per zone

    ♡ the greenhouse uses recirculating hydroponics

    ♡ only the greenhouse recirculation and make-up water is fully modeled right now

    ♡ the full crew waste into nutrient solution loop is planned but not implemented yet

 ### ----------------------------------------

## Greenhouse Water Model:
#### Water Use:
    ♡ water requirements are calculated by zone

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

    ♡ calculation:
            base water × effective grow area × multiplier × sol fraction 
            = water needed

### ----------------------------------------

#### Water Recirculation:
    ♡ each zone has its own efficiency

    ♡ structural: 82%
    ♡ container: 88%
    ♡ rack: 94%

    ♡ calculation:
            - water needed × recirculation efficiency
            = water recirculated

            - water needed × (1.0 - recirculation efficiency)
            = water taken up by plants

    ♡ the water taken up by plants is what actually leaves the recirculating loop

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

## Reservoirs:
    ♡ each zone has its own reservoir

    ♡ sizing is based on effective grow area and hydroponic method

    ♡ see hydropnics.md

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
#### 

### ----------------------------------------

## Future Considerations:
    ♡ figure out runoff water and model separately

### ----------------------------------------

## Design Decision:
#### Why hydroponics?
    ♡ uses less water than traditional soil-based growing when water is recirculated

    ♡ allows water and nutrients to be collected, treated and reused

    ♡ makes vertical racks and hanging containers easier to incorporate

    ♡ avoids transporting and managing large amounts of soil

    ♡ works with the planned closed greenhouse water loop

#### Why refill at 70%?
    ♡ keeps the reservoirs from reaching the 50% low threshold under normal conditions

    ♡ gives a useful buffer in case of temporary water system problems

### ----------------------------------------

### Dev Log Notes:
###### 05/08/2026:
    ♡ going w. a hydroponic set up, I updated v1_scope to include all my notes about a greenhouse 

###### 05/13/2026
    ♡ adding in hydroponics to the greenhouse list and starting from greenhouse lighting to make the greenhouse file be how I want it to be


###### 05/16/2026
    ♡ considering looking at species that make their own structures and systems as inspiration for efficiency

###### 08/12/2026
    ♡ included make-up water system for hydroponic reservoirs