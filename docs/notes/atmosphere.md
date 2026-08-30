# Atmosphere
### General Notes:
    ♡ kg for storage, kpa for atmosphere
    
### ----------------------------------------

## Atmosphere Plan ():
### Layout:

#### Resource Recovery Room:
    ♡ shape: rectangle
    ♡ floor area: ~ 120–140 m²
    ♡ height: 4.5 m
    ♡ volume: ~ 270–360 m³
    ♡ contains:
        - 3 Sabatier racks (each ~ 0.4 m³)
        - H₂ buffer from OGA
        - CO₂ feed / small buffer
        - condenser and water separator
        - controls, valves, sensors, MCA interface
        - maintenance space(~ 1.2 m)
        - amine bed bay for 8 beds in a row with thermal and vent connections, and a clear service isle (~ 40–50 m²)

    ♡ access:
        - near OGA and other atmosphere systems
        - short water line to water processing room
        - connected to the methane storage bay
        - connects to the utility hallway

#### Methane Storage Bay:
    ♡ isolated room / bay for CH₄ tanks
    ♡ independent ventilation and fire considerations
    ♡ next to the atmosphere / resource recovery room
    ♡ methane is never intentionally added to the cabin atmosphere

### Gas Tracking:
    ♡ cabin atmosphere:
        - tracked as partial pressures in kPa
        - O₂, CO₂, N₂, Ar

    ♡ stored resources: 
        - tracked as mass in kg
        - H₂ storage
        - CH₄ storage
        - CO₂ storage (when buffered)

    ♡ individual base leak rates per gas, storage venting is separate

### Atmosphere Subsystems:
    ♡ amine swing beds / CO₂ scrubbing: co2_scrub.py
    ♡ Oxygen Generation Assembly (OGA): oxygen.py
    ♡ buffer gas management (N₂ + Ar): buffer_gas.py
    ♡ Major Constituent Analyzer (MCA)
    ♡ Sabatier: sabatier.md (racks are in this room)
    ♡ ISRU atmosphere and sorbent beds: isru_atm.py

### ----------------------------------------

## Design Evolution:
#### 
    ♡ early target pressure accidentally set to 60 kPa, so corrected to 65 kPa

    ♡ moved from mixed units toward consistent rule: kPa in cabin, kg in storage

    ♡ added per gas leak rates instead of one

    ♡ Sabatier water path changed from direct potable addition to WPA treatment

    ♡ atmosphere physical location locked to utility / resource hub (08/24/2026)

### ----------------------------------------

## Future Considerations:
    ♡ track other trace gases

    ♡ exact sizing of Methane Storage Bay

    ♡ detailed amine bed and MCA placement for layout
    
    ♡ ISRU atmosphere compressor / sorbent bed footprint

    ♡ more refined leak and vent models

    ♡ seasonal / polar CO₂ pressure effects

### ----------------------------------------

## Design Decisions:
#### Why ~ 65 kPa total pressure?
    ♡ a leak would release less atmosphere

    ♡ I wanted it to be lower than Earth sea-level pressure

    ♡ pressure loss will be less catastrophic

    ♡ less gas woul be required to pressurize the habitat

    ♡ it can still support a safe Earth like oxygen partial pressure

#### Why kPa for atmosphere and kg for storage?
    ♡ cabin behaviour is pressure driven (Dalton's Law, crew effects, alerts)

    ♡ stored H₂,CH₄, buffered CO₂ are treated as resources and use mass ratios (especially Sabatier)

    ♡ consistency throughout the code

#### Why put atmosphere systems in the Utility / Resource Recovery Hub?
    ♡ a lot of systems have connections to the water equipment and storage
    
    ♡ keeps industrial process systems together and away from living and greenhouse areas
    
    ♡ short runs for H₂, CO₂ and product water

#### Why isolate methane storage?
    ♡ CH₄ is flammable

    ♡ independent ventilation and fire control are simpler in a dedicated bay

### ----------------------------------------

### Dev Log Notes:
###### From v1_scope:
    ♡ chose a lower target pressure of ~ 65 kPa so leaks would be less catastrophic

    ♡ 25% yearly atmosphere pressure changes from CO₂ freezing and sublimating at the poles

    ♡ going to be using Dalton's Law

    ♡ tracking partial pressure changes per timestep instead of mass

    ♡ using five-minute timesteps: 
        -288 intervals/day:
            ~ 0.0033 * 288 = 0.9504 kPa pp/day

        - 30 crew members:
            ~ 0.0033 * 30 = 0.099 kPa/5min

###### 03/04/2026
    ♡ starting w. atmosphere 

    ♡ going to be using Dalton's Law

###### 03/08/2026
    ♡ resuming atmosphere creation w. updated knowledge

    ♡ today I learned that I needed to get the skeleton figured out and that it's okay to refine the numbers afterwards

###### 03/09/2026
    ♡ continuing where I left off w. scrubbing

    ♡ NASA references: crew CO₂ production is ~ 1 kg pp/day


    ♡ making separate functions for managing and checking gases

###### 03/19/2026
    ♡ fixing the buffer gas control function so that it doesn't alter things from state directly and turning the return into a dictionary. I will probably end up using dictionaries for most of these as I go

###### 03/26/2026
    ♡ added some power consumption variables to oxygen_system.py

    ♡ for the mca function, I decided to not use state so I can manage/calculate both before and after control

    ♡ realizing that the file for the O₂ system has separate functions and the buffer gas file has one solid function, so I might end up breaking up that long function into a few smaller ones for readability and also b/c I will be adding more to this function

    ♡ broke up one long buffer gas system function into smaller ones for readability, organization and future handling

###### 04/28/2026
    ♡ changed the targets for N₂ and Ar and the target pressure to 65.0kpa (which it should have been this whole time, I accidentally had it at 60.0kpa)

###### 04/30/202
    ♡ I am going to keep h2 stored in kg and also I'm going to make the methane(ch4) storage to be in kg b/c these are being treated as resources and I read that the Sabatier uses mass ratios, not pressure ratios

    ♡ reactions_available is how many times stoichiometric reaction can happen w. a ratio of 1 CO₂ : 4 h2

    ♡ I thought adding a little bit of a leak while venting the ch4 was realistic, so I might add this to the other systems that vent

###### 05/03/2026
    ♡ I decided to track gases in the atmosphere in kpa and h2 and ch4 in kg for storage and I'm not 100% sure about the other ones yet

    ♡ going to keep things consistent: kg for storage, kpa for atmosphere

    ♡ adding variables for each gas to have a base leak rate, to use for venting and other things (using individual ones b/c some leak faster than others)

###### 05/14/2026
    ♡ going to add in the gas leak logic so the variables are actually getting used so I can delete the vague universal gas leak/hour variable

    ♡ adding gas_leak.py file to handle that ^

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

