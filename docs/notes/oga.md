# Oxygen Generation Assembly
### General Notes:
    ♡ electrolyzes potable water into O₂ and H₂
    
    ♡ O₂ is added to the cabin atmosphere in kPa
    
    ♡ H₂ is stored and sent to the Sabatier
    
    ♡ extra O₂ above target is stored, vented if storage is full
    
    ♡ water used here is subtracted from potable storage by the water system

### ----------------------------------------

## Arcadia O₂ Regen Plan (updated 08/30/2026):
####

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
