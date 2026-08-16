# Greenhouse Water:
### General Notes:
    ♡ calculations are performed separately for each zone

    ♡ each zone uses averaged plant data instead of simulating individual crops

    ♡ V1 uses treated habitat water for greenhouse make up water and assumes greenhouse nutrients are supplied separately

    ♡ by uptake I'm refering to the actual volume of water consumed by the plants

### ----------------------------------------

## Greenhouse Water Model (08/15/2026):
## Plant Water Demand:
    ♡ preliminary estimates

    ♡ structural:
        - plant water uptake: ~ 2.5 kg/m²/sol
        - effective grow area: 420 m²
        - baseline plant uptake: ~ 1,050 kg/sol
        
        - calculation:
            2.5 kg/m²/sol × 420 m²
            = 1,050 kg water/sol

    ♡ container:
        - plant water uptake: ~ 2.2 kg/m²/sol
        - effective grow area: 480 m²
        - baseline plant uptake: ~ 1,056 kg/sol
        
        - calculation:
            2.2 kg/m²/sol × 480 m²
            = 1,056 kg/sol

    ♡ rack:
        - plant water uptake: ~ 1.8 kg/m²/sol
        - effective grow area: 450 m²
        - baseline plant uptake: ~ 810 kg/sol

        - calculation:
            1.8 kg/m²/sol × 450 m²
            = 810 kg/sol

    ♡ total greenhouse plant water uptake:
        - calculation:
            1,050 + 1,056 + 810
            = 2,916 kg/sol

        - total plant water uptake:
            ~ 2,916 kg/sol

#### Transpiration & Plant Biomass:
    ♡ most water used by the plants eventually leaves through transpiration

    ♡ a smaller amount remains with the plant

    ♡ transpiration: ~ 95%
    ♡ plant biomass: ~ 5% (v1 PLACEHOLDER)
    ♡ total plant water uptake: ~ 2,916 kg/sol

    ♡ calculation:
        - transpiration:
            2,916 × 0.95
            = 2,770.2 kg/sol

        - plant biomass water:
            2,916 × 0.05
            = 145.8 kg/sol

#### Transpiration Recovery:
    ♡ transpired plant water enters the greenhouse atmosphere and the CHX removes most of this water as condensate

    ♡ captured condensate is sent to the WPA for processing

    ♡ CHX transpiration capture efficiency: ~ 95%
    ♡ greenhouse transpiration: ~ 2,770.2 kg/sol
    ♡ CHX condensate captured: ~ 2,631.69 kg/sol

    ♡ calculation:
        - condensate captured:
            2,770.2 × 0.95
            = 2,631.69 kg/sol

        - uncaptured transpiration:
            2,770.2 × 0.05
            = 138.51 kg/sol
        
        - condensate recovered by WPA:
            2,631.69 × 0.95
            = 2,500.1055 kg/sol
            ≈ 2,500.11 kg/sol

        - WPA processing loss:
            2,631.69 × 0.05
            = 131.5845 kg/sol
            ≈ 131.58 kg/sol

    ♡ captured condensate is sent into the habitat water recovery system

### ----------------------------------------

#### Operational Water Losses:
    ♡ these are rough V1 estimates since individual equipment, specific leaks and other non-plant losses aren't modeled separately

    ♡ see hydroponics.md for the circulation system losses

    ♡ structural:
        - operational loss rate: ~ 4%
        - baseline plant water uptake: 1,050 kg/sol

        - calculation:
            1,050 × 0.04
            = 42.0 kg/sol

    ♡ container:
        - operational loss rate: ~ 3%
        - baseline plant water uptake: 1,056 kg/sol

        - calculation:
            1,056 × 0.03
            = 31.68 kg/sol

    ♡ rack:
        - operational loss rate: ~ 2%
        - baseline plant water uptake: 810 kg/sol

        - calculation:
            810 × 0.02
            = 16.2 kg/sol

    ♡ total operational water loss:
        42.0 + 31.68 + 16.2
        = 89.88 kg/sol
        ≈ 89.9 kg/sol

### ----------------------------------------

## Make-up Water System:
    ♡ make-up happens when a reservoir drops to 70%

    ♡ the greenhouse only draws the actual volume needed to return to normal level

    ♡ make-up water replaces water that doesn't return to the greenhouse/habitat water loop during normal operation

    ♡ baseline sources of make-up demand:
        - water retained in plant biomass
        - transpiration not captured by the CHX
        - operational hydroponic water losses

    ♡ all three reservoirs are topped up from a shared clean water supply

    ♡ WPA processing loss ~ 131.58 kg/sol

    ♡ loop:
        1. habitat potable / treated water
        2. greenhouse make-up water
        3. zone valves
        4. nutrient reservoir


    ♡ calculation:
        145.8 kg/sol (plant biomass)
        + 138.51 kg/sol
        + 89.88 kg/sol
        = 374.19 kg/sol

        - baseline greenhouse make-up water demand before WPA losses:
            ~ 374.19 kg/sol
        
        - total baseline reservoir make-up demand:
            374.19 + 131.58
            = 505.77 kg/sol
        
        - this is water that must be replaced in the greenhouse reservoirs, not permanent water loss from the entire habitat

### ----------------------------------------

## Full Water / Waste Loop (Future):
    ♡ concept only — not modeled in V1 yet

    ♡ planned loop:
        1. crew wastewater / other waste
        2. UPA / WPA and other treatment
        3. recovered clean water
        4. nutrient recovery / processing
        5. greenhouse nutrient solution
        6. plants
        7. plant transpiration
        8. greenhouse humidity
        9. CHX condensate capture
        10. WPA processing
        11. recovered water returns to habitat storage

    ♡ water and nutrients are treated as separate parts of the future loop

    ♡ treated habitat water can be reused as greenhouse make-up water

    ♡ nutrients recovered from waste need to be processed into forms that are safe and usable by the crops before entering the reservoirs

    ♡ untreated crew waste is not sent directly into the greenhouse nutrient solution

    ♡ V1:
        - greenhouse make-up water comes from treated habitat water

        - greenhouse nutrients are assumed to be supplied separately

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

    
    ♡ water taken up by plants:
        - 85% becomes transpiration (goes into the greenhouse air and then the CHX): 
            plant water uptake × 0.85

        - 15% stays in plant mass (permanent loss):
            plant water uptake × 0.15

    ♡ the biomass water will eventually be calculated from crop production, but not for v1, so in the meantime the placeholder is just going to be ~ 5%

### ----------------------------------------

## Future Considerations:
    ♡ implement: the full crew waste to water recovery to nutrient recovery to greenhouse loop
    
    ♡ future goal:
    - recover both water and useful nutrients from habitat waste streams
    - reduce imported fertilizer requirements
    - reduce long term replacement water demand
    - make the habitat more self-sustaining

    ♡ determine which crew waste streams can realistically contribute nutrients

    ♡ determine what nutrient recovery / treatment is required before reuse

    ♡ determine how nitrogen, phosphorus, potassium and micronutrients are balanced

    ♡ determine how salts or unwanted compounds are prevented from accumulating in the greenhouse reservoirs

    ♡ eventually connect recovered nutrient production to greenhouse nutrient demand

### ----------------------------------------

## Design Decision:
#### Why calculate plant water uptake separately from hydroponic circulation?
    ♡ the amount of nutrient solution moving through the hydroponic system is much larger than the amount of water actually being consumed by the plants

    ♡ calculating plant uptake separately prevents nutrient solution from being counted as greenhouse water consumption

    ♡ water that drains through the growing system normally returns to its zone reservoir and remains in the hydroponic loop

#### Why use zone-specific water demand?
    ♡ the structural, container and rack zones have different crops

    ♡ each zone has a different effective grow area

    ♡ using zone averages keeps V1 manageable without treating every individual crop as if it has the same water demand
    
### ----------------------------------------

### Dev Log Notes:
###### 08/12/2026
    ♡ included make up water system for hydroponic reservoirs

###### 08/15/2026
    ♡ with so many changes I'm pretty much starting over for the water plan for the greenhouse, using my old information as reference

    ♡ starting with plant water demand, the old value was 3.4 kg/m²/sol × 1.15 = ~ 3.91 kg/m²/sol, looking over the NASA study with potatoes I've been referencing the total system water was ~ 2 L/m²/day, since water is ~ 1 kg/L, ≈ 2 kg/m²/day, a Mars sol = ~ 1.0275 Earth days, 2.0 kg/m²/day × 1.0275 day/sol ≈ 2.06 kg/m²/sol

    ♡ b/c my strucutral zone isn't all potato, I need to increase the mixed zone average probably above that b/c the banana is also very water demanding.. so for structural prelminary value I'll use the plant water uptake rate of ~ 2.5 kg/m²/sol

    ♡ containers contain med/tall crops and the hydroponic recircle the water efficiently, so it doesn't need to include the solution in the containers, NASA emphasizes that in closed CEA (Chemical Equilibrium with Applications), the major crop water requirement is what plants transpire, with irrigation water recirculated

    ♡ ~ 2.2 kg/m²/sol for container as a V1 zone average b/c it stays close to the crop water scale used for structural while being under ~ 2.5 since that zone includes the larger and more water demanding crops

    ♡ this one can be low considering growing conditions and crop choices for the rack zone, so ~ 1.8 kg/m²/sol will work for now

    ♡ replacing the old percetages for transpiration and plant mass, or at least going over the calculations

    ♡ plant water uptake seems to be mainly transpiration.. in some hydroponic experiments, water disappearing from sealed nutrient containers is treated essentially as transpiration, because only the above ground plants are exposed to the air, the water retained is actually quite low compared to that

    ♡ NASA ECLSS systems treat condensate as a recoverable wastewater stream, and plant growth life support research looks into recovering and reusing transpired water vapor, so using ~ 95% capturing efficiency seems right so that the recovery isn't perfect, but still small amount goesn't get collected

    ♡ things like maintenance/flushing, minor leakage, evaporation from exposed solution or wet surfaces, and solution retained in equipment/LECA during servicing all add into the the water losses, but I think I'm just going to use a small recirculation loss, and make each zone have a different percentage, mostly b/c of the different growing conditions, considering the ~ 95% capturing efficiency 

    ♡ the biomass water will eventually be calculated from crop production, but not for v1, so in the meantime the placeholder is just going to be ~ 5%