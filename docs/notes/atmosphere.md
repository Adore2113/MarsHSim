# Atmosphere
### General Notes:

### ----------------------------------------

## Atmosphere Plan ():
### Layout:

#### Sabatier + Atmosphere Recovery Room:
    ♡ shape: rectangle
    ♡ floor area: ~ 60-80 m²
    ♡ height: 4.5 m
    ♡ contains:
        - 3 Sabatier racks (each ~ 0.4 m³)
        -  H₂ buffer from OGA
        - CO₂ feed small buffer
        - condenser and water separator
        - controls, valves, sensors
        - maintenance space

    ♡ access:
        - near OGA and atmosphere systems
        - short water line to the water processing room
        - connected to the methane storage bay

#### Methane Storage Bay:
    ♡ isolated room for CH₄ tanks
    ♡ independent ventilation and fire considerations

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
###### Notes from May:

###### 03/04/2026
    ♡ starting w. atmosphere 
    
    ♡ going to be using Dalton's Law

###### 03/08/2026
    ♡ resuming atmosphere creation w. updated knowledge

    ♡ CO₂ was defaulting to zero, need to fix my scrubbing system

    ♡ today I learned that I needed to get the skeleton figured out and that it's okay to refine the numbers afterwards

###### 03/09/2026
    ♡ continuing where I left off w. scrubbing

    ♡ NASA references: crew CO₂ production is ~ 1 kg pp/day

    ♡ researched O₂ regeneration and electrolysis w. focus on Oxygen Generation Assembly (OGA), MOXIE like Solid Oxide Electrolysis (SOXE) and Sabatier CO₂ reduction + electrolysis

    ♡ making separate functions for managing and checking gases

    ♡ more research on 02 regen and electrolysis

    ♡ implementing very basic OGA O₂ generation function for now (handling power usage, total pressure updates, hydrogen(h2) production and handling/venting later)  

###### 03/10/2026
    ♡ renamed checking_gases function to gas_alerts, moved the CO₂ removal function to before o2_regen

    ♡ I know that chemistry ratios use moles, but I really wanted to stick to kPa and kilograms (kg) to avoid my code being more complex, so I'll figure out the conversions to avoid that

    ♡ made the scrubber unable to remove more CO₂ than exists and changed the kPa values to move 4 decimal places instead of two, updated target based CO₂ and O₂ control, added target gases as global variables in engine.py

    ♡ adding in the hydrogen that the OGA electrolysis makes and venting it FOR NOW and will do research on how I can use it later on (Sabatier?)

    ♡ adding OGA byproduct function in, first calculating 23C to Kelvin b/cI read the gas pressure depends on temp (pressure drops if it goes down) 

###### 03/13/2026
    ♡ figure out how much water(H2O) the OGA and water electrolysis uses every time it runs, I'm going to find the fixed reaction ratio instead of a fixed ratio b/c the amount of O₂ produced are going to change depending on habitat events

    ♡ going to use 1000kg of water to start as a placeholder to finish the OGA functions

    ♡ going to keep the OGA functions separate instead of one big function w. a comment to sort of group them together, I feel like that will be better for future readability

    ♡ arranged some comments to be beside the line of code, I find if it's short, it does look cleaner

    ♡ finished OGA and water electrolysis for now, moving onto argon and nitrogen


###### 03/14/2026

    ♡ I added the variable CO₂_stored_kpa to collect and temporarily store the CO₂ the amine bed scrubs until I use it later in my code

###### 03/17/2026

    ♡ while adding the temp variables to run_oga, I decided to rename a few variables to make reading/going over my code later easier and I also decided to make these functions more efficient overall

    ♡ I'm not sure if I already stated this, but the OGA is capped at 0.004 (for now) so that the OGA has to take its time to catch backup so that it doesn't run a huge amount of power and it seems unrealistic

###### 03/19/2026
    ♡ fixing the buffer gas control function so that it doesn't alter things from state directly and turning the return into a dictionary. I will probably end up using dictionaries for most of these as I go

###### 03/26/2026
    ♡ added some power consumption variables to oxygen_system.py

    ♡ for the mca function, I decided to not use state so I can manage/calculate both before and after control

    ♡ realizing that the file for the O₂ system has separate functions and the buffer gas file has one solid function, so I might end up breaking up that long function into a few smaller ones for readability and also b/c I will be adding more to this function

    ♡ broke up one long buffer gas system function into smaller ones for readability, organization and future handling

###### 03/28/2026
    ♡ breaking up the CO₂ scrubber system into different functions and adding heat, taking into consideration that I want there to be a baseline power/online bed like there is for heat, power usage used on actual CO₂ removed, emergency events and full power loss (these last two will be handled later though)

    ♡ added power usage to CO₂ scrubber, updated engine and quick_test to work w. the file properly

###### 03/29/2026
    ♡ while looking at the amine bed list, I'm not happy w. how it's running right now b/c of how I hardcoded and pre-assigned the roles, when I actually want this to be a living working system, so before starting the solar power functions, I'm going to go back and try to fix that

###### 04/21/2026
    ♡ going back to CO₂_scrubber_system and changing hardcoding to calculations

###### 04/25/2026
    ♡ updated amine beds to come online w. how much CO₂ is needed, I used two different hysteresis for that

###### 04/27/2026
    ♡ added venting for OGA

###### 04/28/2026

    ♡ changed the targets for N₂ and Ar and the target pressure to 65.0kpa (which it should have been this whole time, I accidentally had it at 60.0kpa)

###### 04/30/2026

    ♡ updated OGA logic, by removing the pa conversation at all and made r for the universal gas constant in kpa instead

    ♡ I am going to keep h2 stored in kg and also I'm going to make the methane(ch4) storage to be in kg b/c these are being treated as resources and I read that the Sabatier uses mass ratios, not pressure ratios

    ♡ reactions_available is how many times stoichiometric reaction can happen w. a ratio of 1 CO₂ : 4 h2

    ♡ I thought adding a little bit of a leak while venting the ch4 was realistic, so I might add this to the other systems that vent

###### 05/03/2026

    ♡ I decided to track gases in the atmosphere in kpa and h2 and ch4 in kg for storage and I'm not 100% sure about the other ones yet

    ♡ going to keep things consistent: kg for storage, kpa for atmosphere

    ♡ adding variables for each gas to have a base leak rate, to use for venting and other things (using individual ones b/c some leak faster than others)

###### 05/05/2026
    ♡ working on CO₂_scrubber_system.py making the logic closer to the sabatier and other systems logic

###### 05/14/2026
    ♡ going to add in the gas leak logic so the variables are actually getting used so I can delete the vague universal gas leak/hour variable

    ♡ adding gas_leak.py file to handle that ^

###### 05/20/2026
    ♡ I added handling excess O₂ to oxygen.py

    ♡ while going over the results from each subsystem, I'm realizing that CO₂ is not being handled right.. I need to fix where the Sabatier is getting it's CO₂ amount from

    ♡ I made some changes to buffer gas, double check them tomorrow

###### 05/25/2026
    ♡ fixed venting logic in oxygen.py

###### 05/27/2026
    ♡ adding vent leaks to buffer_gas.py

    ♡ I know that turning buffer_gas.py into one long code might be different to read, but I think it works w. my section headers keeping things organized and hopefully easy to read, I'm also hoping this keeps things a bit neater when it comes to ouputs and variables and such

###### 05/29/2026
    ♡ fixing  ch4 venting logic

    ♡ the methane leak is going to only be relevant in future events, maybe

###### 06/16/2026
    ♡ fixing buffer gas

###### 08/24/2026

    ♡ the atmosphere are will be with the utility/resource area b/c a lot of those sytems have certain connections to the water eqipment and storage so it makes sense that they are kept in closer proximity

