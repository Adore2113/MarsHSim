# Sabatier 
### General Notes:
    ♡ converts CO₂ + H₂ into CH₄ + H₂O

    ♡ provides both methane and recovered water

    ♡ water produced is added directly to the potable water balance

    ♡ integrates with OGA: OGA produces hydrogen that can feed the Sabatier (or be vented)

    ♡ SpaceX approach: combines oxygen production (electrolysis / OGA) with methane rocket fuel production with Sabatier + electrolysis

    ♡ only runs when so many reactants are available and the system is on

    ♡ includes limited and venting modes for reactant shortages and methane storage limits

### ----------------------------------------

## Sabatier Plan:
### Reaction Chemistry:
    ♡ min H₂ for reaction: 0.012 kg
    ♡ min CO₂ for reaction: 0.012 kg
    ♡ hysteresis multiplier: 1.5
   
    ♡ methane venting hysteresis: 
        0.60 of storage capacity
   
    ♡ stoichiometric ratio: 
        1 CO₂ : 4 H₂

    ♡ produces: 
        1 CH₄ + 2 H₂O

    ♡ molar masses:
        - H₂ = 2.016 g/mol
        - CO₂ = 44.01 g/mol
        - CH₄ = 16.043 g/mol
        - H₂O = 18.015 g/mol

    ♡ base efficiency: 0.88

    ♡ reactions_available:
        - how many times the stoichiometric reaction can occur, limited by the lesser reactant and efficiency

    ♡ calculation:
        co2_moles:
             available_co2_kg / (44.01 × 0.001)

        h2_moles:
             available_h2_kg  / (2.016 × 0.001)

        reactions_available:
             min(co2_moles, h2_moles / 4) × 0.88

        water_produced_kg:
             reactions_available × 2 × 18.015 × 0.001
        
        ch4_produced_kg :
             reactions_available × 16.043 × 0.001
        
        h2_consumed_kg  :
             reactions_available × 4 × 2.016 × 0.001
        
        co2_consumed_kg :
             reactions_available × 44.01 × 0.001

### Operating Modes:
    ♡ offline:
        - system off
        - no power or reaction

    ♡ idle:
        - both reactants below minimum thresholds
        - very low standby power: ~ 0.1 kW

    ♡ limited_co2 / limited_h2:
        - one reactant is low/below hysteresis
        - runs at reduced power: ~ 75 % of base

    ♡ running:
        - both reactants above hysteresis
        - full power and reaction rate

    ♡ venting:
        - methane storage is near or over capacity
        - excess CH₄ is vented
        - power may increase slightly at × 1.25

    ♡ critical power mode:
        - reduced power: 0.3 kW
        - reduced  heat: ~ 0.2 kW

### Power & Heat:
    ♡ base power: 0.85 kW
    ♡ idle power: ~ 0.1 kW
    ♡ limited mode power: base × 0.75
    ♡ critical power mode: 0.3 kW
    
    ♡ exothermic heat fraction:
        0.65 of electrical pow

    ♡ calculation:
        heat:
            sabatier_power_used_kw × 0.65

### Water Production:
    ♡ water produced is added to the potable water storage veach step

    ♡ this is an important recovery source in the water balance

### Methane Handling:
    ♡ produced CH₄ is added to storage

    ♡ when storage exceeds venting hysteresis excess is vented/capped

    ♡ hard capacity limit forces venting if reached

    ♡ small continuous CH₄ leak from storage is also modelled

### Atmosphere Fallback:
    ♡ if stored CO₂ is almsot gone, a small limited amount can be drawn from cabin atmosphere

    ♡ capped so cabin CO₂ is not quickly depleated

### ----------------------------------------

## Design Evolution:
#### Early Integration:
    ♡ originally added late to the water balance

    ♡ water production was missing from the storage update

#### Modes:
    ♡ added limited_co2 / limited_h2 and venting modes

    ♡ added power saving mode for critical power conditions

### ----------------------------------------

## Future Considerations:
    ♡ go over OGA hydrogen production rates

    ♡ more detailed efficiency drop over time

    ♡ option to store vs vent methane based on mission phase (propellant or disposal)

### ----------------------------------------

## Design Decisions:
#### 

### ----------------------------------------

### Dev Log Notes:
###### 03/09/2026
    ♡ researched O₂ regeneration and electrolysis w. focus on Oxygen Generation Assembly (OGA), MOXIE like Solid Oxide Electrolysis (SOXE) and Sabatier CO₂ reduction + electrolysis


##      03/10/2026
    ♡ adding in the hydrogen that the OGA electrolysis makes and venting it FOR NOW and will do research on how I can use it later on (Sabatier?)

##      04/27/2026
    ♡ started to add sabatier info/logic into my water system file

##      04/28/2026
    ♡ created a new file for the Sabatier

##      04/30/2026
    ♡ I am going to keep h2 stored in kg and also I'm going to make the methane(ch4) storage to be in kg b/c these are being treated as resources and I read that the Sabatier uses mass ratios, not pressure ratios

    ♡ if I need to convert them at any time, I'll just use the conversion and put it up as a constant in the file

    ♡ resuming Sabatier file

    ♡ using a hysteresis to avoid jumpy on and off reactions

    ♡ reactions_available is how many times stoichiometric reaction can happen w. a ratio of 1 CO₂ : 4 h2

    ♡ I realize I actually put the mode decision in the main function for running the sabatier and also the OGA actually and I didn't in the other files. I've been changing things and upgrading how I'm doing things so eventually I will need to go through all of the files that I worked on first.

    ♡ waiting to do that though ^ b/c refactoring and editing has taken up enough time for the time being and I want to focus on getting some main systemsfigured out. 

    ♡ I thought adding a little bit of a leak while venting the ch4 was realistic, so I might add this to the other systems that vent

##      05/01/2026
    ♡ added sabatier outputs and updates into engine.py and fixed variables for ch4 where I accidentally put kpa insted or kg

    ♡ code is running again

##      05/03/2026
    ♡ updating print to show sabatier information

    ♡ I decided to track gases in the atmosphere in kpa and h2 and ch4 in kg for storage and I'm not 100% sure about the other ones yet

    ♡ going to keep things consistent: kg for storage, kpa for atmosphere

    ♡ adding variables for each gas to have a base leak rate, to use for venting and other things (using individual ones b/c some leak faster than others)

##      05/20/2026
    ♡ while going over the results from each subsystem, I'm realizing that CO₂ is not being handled right.. I need to fix where the Sabatier is getting it's CO₂ amount from

    ♡ I made some changes to the Sabatier file and ran a few test for four sols, getting an update every 5 hours while only getting the sol, time and atmosphere info.. CO₂ is much better, but there are still issues w. the buffer gas, as well as a few other things, that I will be working towards 


##      05/22/2026
    ♡ I added in the Sabatier into water.py, b/c I forgot to add it in the storage update and run_water_system function 

##      06/19/2026
    ♡ fixing my sabatier file, made the methane go aove the safe limit, so I'm going to see what I can do w. the methane storage and venting 

    ♡ I decided to make sure all ch4 is either vented immediately or sent to storage, it's not goin to be added into the cabin atmosphere

    ♡ I fixed the sabatier call in engine.py

    ♡ I noticed my greenhouse is currently producting 75x MORE O₂ than my crew of 30  mean and this is absolutely not right, it doesn't make any sense so I need to fix this


