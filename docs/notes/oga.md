# Oxygen Generation Assembly
### General Notes:
    ♡ electrolyzes potable water into O₂ and H₂

    ♡ O₂ is added to the cabin atmosphere and tracked in kPa
    
    ♡ H₂ is stored for use by the Sabatier system
   
    ♡ excess O₂ is vented if O₂ storage is full
    
    ♡ water consumed by the OGA is subtracted from potable-water storage by the water system

    ♡ V1 models OGA output with gas law and electrolysis calculations instead a fixed mass of O₂ per step

## Arcadia OGA Plan (updated 08/30/2026):
### Shared Control Modes:
    ♡ offline:
        - OGA is switched off
        - no O₂ or H₂ is produced
        - no OGA power or heat

    ♡ idle:
        - OGA is available, but cabin O₂ is within 0.002 kPa of target
        - power: ~ 0.15 kW
        - heat: ~ 0.40 kW

    ♡ running:
        - OGA adds O₂ up to the amount needed or its step capacity
        - H₂ is produced from the same electrolysis reaction
        - running cap: 6.0 kPa O₂ per hour
        - power: ~ 2.5 kW
        - heat: ~ 1.2 kW

    ♡ handling limited_water:
        - potable water is too low to produce the calculated amount of O₂ while preserving the crew reserve and safety backup
    
        - no O₂ or H₂ is produced during the step
        
        - currently uses 55 % of normal running power and heat

    ♡ water used: 1.11 kg water / kg O₂
    ♡ H₂ made from the same split
    ♡ leaves 2.0 kg/crew + 30 kg before OGA can run

#### O₂ / OGA:
    ♡ hysteresis: ~ 0.002 kPa
    ♡ maximum O₂ output: ~ 6.0 kPa/h
    ♡ O₂ target is stored as target_o2_kpa
    ♡ current logic adds 0.001 kPa control margin to the calculated O₂ deficit

    ♡ calculation:
        - O₂ required:
            target O₂ kPa - O₂ kPa after crew metabolism

        - maximum O₂ this step:
            6.0 kPa/h × step duration in hours

        - O₂ added:
            the smaller of maximum O₂ this step or O₂ required + 0.001 kPa

    ♡ used for:
        - replacing O₂ consumed by the crew
        - maintaining cabin O₂ near target partial pressure


### ----------------------------------------

### ----------------------------------------

## Future Considerations:
    ♡ 

### ----------------------------------------

## Design Decisions:
#### 

### ----------------------------------------

### Dev Log Notes:
###### 03/09/2026
    ♡ researched O₂ regeneration and electrolysis w. focus on Oxygen Generation Assembly (OGA), MOXIE like Solid Oxide Electrolysis (SOXE) and Sabatier CO₂ reduction + electrolysis

    ♡ more research on 02 regen and electrolysis

    ♡ implementing very basic OGA O₂ generation function for now (handling power usage, total pressure updates, hydrogen(h2) production and handling/venting later)  

###### 03/10/2026

    ♡ renamed checking_gases function to gas_alerts, moved the CO₂ removal function to before o2_regen

    ♡ adding in the hydrogen that the OGA electrolysis makes and venting it FOR NOW and will do research on how I can use it later on (Sabatier?)

    ♡ adding OGA byproduct function in, first calculating 23C to Kelvin b/cI read the gas pressure depends on temp (pressure drops if it goes down) 

###### 03/13/2026

    ♡ figure out how much water(H2O) the OGA and water electrolysis uses every time it runs, I'm going to find the fixed reaction ratio instead of a fixed ratio b/c the amount of O₂ produced are going to change depending on habitat events

    ♡ going to use 1000kg of water to start as a placeholder to finish the OGA functions

    ♡ going to keep the OGA functions separate instead of one big function w. a comment to sort of group them together, I feel like that will be better for future readability

    ♡ finished OGA and water electrolysis for now, moving onto argon and nitrogen

###### 03/17/2026

    ♡ while adding the temp variables to run_oga, I decided to rename a few variables to make reading/going over my code later easier and I also decided to make these functions more efficient overall

    ♡ I'm not sure if I already stated this, but the OGA is capped at 0.004 (for now) so that the OGA has to take its time to catch backup so that it doesn't run a huge amount of power and it seems unrealistic

###### 04/27/2026

    ♡ added venting for OGA

###### 04/30/2026

    ♡ updated OGA logic, by removing the pa conversation at all and made r for the universal gas constant in kpa instead
