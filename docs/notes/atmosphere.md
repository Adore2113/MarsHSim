# Atmosphere
### General Notes:
    ♡ kg for storage, kpa for atmosphere

    ♡ V1 pressurized habitat volume: 30,176 m³

    ♡ methane storage bay is not in V1
    
    ♡ Sabatier methane vents outside and is never intentionally released into the habitat

### ----------------------------------------

## Arcadia Atmosphere Plan (updated 10/01/2026):
### Layout:
    ♡ Atmosphere / Resource Recovery Room: 
        ~ 140 m² / ~ 630 m³

    ♡ ISRU Atmosphere Room: ~ 80 m² / ~ 360 m³

    ♡ room measurements are kept in utility_hub.md

    ♡ atmosphere and recovery equipment is kept near connected water equipment and gas storage

### Cabin Atmosphere:
    ♡ total pressure target: 65.0 kPa
    ♡ total pressure safe range: 55.0-70.0 kPa

    ♡ target partial pressures:
        - O₂: 20.0 kPa
        - N₂: 22.0 kPa
        - Ar: 22.6 kPa
        - CO₂: 0.4 kPa
        - CH₄: 0.0 kPa
        - H₂: 0.0 kPa

    ♡ calculation:
        - total target pressure:
            20.0 + 22.0 + 22.6 + 0.4 + 0.0 + 0.0 = 65.0 kPa

    ♡ starting atmosphere matches the target partial pressures

### Gas Safety Ranges:
    ♡ O₂ safe range: 18.0-25.0 kPa
    ♡ CO₂ maximum: 1.0 kPa
    ♡ N₂ safe range: 10.0-30.0 kPa
    ♡ Ar safe range: 10.0-30.0 kPa
    ♡ H₂ maximum: 0.4 kPa
    ♡ CH₄ fire alert: 0.8 kPa
    ♡ H₂ and CH₄ have cabin targets of 0.0 kPa and are tracked as unwanted cabin gases

### Gas Mass per kPa:
    ♡ at 23 °C in the 30,176 m³ cabin, 1.0 kPa represents ~ 12,255 moles of gas

    ♡ ~ mass represented by 1.0 kPa:
        - O₂: 392 kg
        - N₂: 343 kg
        - Ar: 490 kg
        - CO₂: 539 kg
        - CH₄: 197 kg
        - H₂: 25 kg

    ♡ calculation:
        - habitat temperature in Kelvin:
            23 °C + 273.15 = 296.15 K

        - moles represented by 1.0 kPa:
            (1.0 kPa × 30,176 m³) ÷ (0.008314 kPa·m³/(mol·K) × 296.15 K)
            ≈ 12,255 mol

        - gas mass represented by 1.0 kPa:
            moles per kPa × gas molar mass × 0.001 kg/g

### Target Gas Inventory:
    ♡ O₂: ~ 7,843 kg
    ♡ N₂: ~ 7,553 kg
    ♡ Ar: ~ 11,064 kg
    ♡ CO₂: ~ 216 kg
    ♡ CH₄: 0 kg
    ♡ H₂: 0 kg
    ♡ total target atmosphere: ~ 26,700 kg
    ♡ calculation:
        - target mass for each gas:
            target partial pressure × kg represented by 1.0 kPa of that gas

        - total target atmosphere:
            O₂ mass + N₂ mass + Ar mass + CO₂ mass

### Gas Storage:
    ♡ O₂:
        - starting storage: 1,200 kg
        - capacity: 3,000 kg

    ♡ N₂:
        - starting storage: 1,500 kg
        - capacity: 4,000 kg

    ♡ Ar:
        - starting storage: 2,000 kg
        - capacity: 5,000 kg

    ♡ CO₂:
        - starting storage: 20 kg
        - capacity: 500 kg
        - storage is a resource buffer, not the cabin target

    ♡ H₂:
        - starting storage: 50 kg
        - capacity: 300 kg
        - used as Sabatier feed

    ♡ CH₄:
        - starting storage: 0 kg
        - capture-buffer capacity: 400 kg
        - no physical Methane Storage Bay in V1
        - Sabatier does not fill this buffer
        - a vent line is not treated as a storage tank

    ♡ the starting O₂, N₂ and Ar reserves each represent several kPa of cabin makeup gas

    ♡ calculation:
        - pressure equivalent of stored gas:
            stored gas in kg ÷ kg represented by 1.0 kPa of that gas

    ♡ the old 680 kg O₂ reserve represented ~ 22 kPa in the old habitat volume but only ~ 1.7 kPa in the current cabin

### ----------------------------------------

### CO₂ Scrubbing:
    ♡ total amine beds: 8
    ♡ CO₂ capacity per bed: 3 kg
    ♡ combined bed capacity: 24 kg CO₂

    ♡ 30 crew produce ~ 30 kg CO₂ per sol, so the beds must cycle and regenerate

    ♡ scrub rate per bed: 0.00028 kPa per scrub action

    ♡ calculation:
        - combined bed capacity:
            8 beds × 3 kg/bed = 24 kg CO₂

        - ~ CO₂ mass represented by one bed's scrub action:
            0.00028 kPa × 539 kg/kPa
            ≈ 0.15 kg CO₂

    ♡ the old 0.0035 kPa-per-bed value represented ~ 1.9 kg per bed action in the current cabin

    ♡ detailed adsorption, regeneration, power and heat behavior is kept in the Amine Beds / CO₂ Scrubbing file

### Buffer Gas:
    ♡ N₂ and Ar provide most of the target pressure that is not supplied by O₂:
        - N₂: ~ 2.7 %
        - Ar: ~ 1.6 %

    ♡ both gases are collected by ISRU atmosphere processing

    ♡ buffer-gas control is used for:
        - maintaining total cabin pressure
        - preventing O₂ from becoming the entire cabin atmosphere

    ♡ compressor, sorbent-bed and intake behavior is kept in the ISRU Atmosphere and Water file

### Gas Tracking:
    ♡ cabin partial pressures in kPa:
        - O₂
        - CO₂
        - N₂
        - Ar
        - H₂, monitored with a 0.0 kPa target
        - CH₄, monitored with a 0.0 kPa target

    ♡ stored resources in kg:
        - O₂
        - N₂
        - Ar
        - CO₂
        - H₂
        - CH₄ capture buffer variables

    ♡ the Sabatier reaction uses a stoichiometric ratio of 1 mole CO₂ to 4 moles H₂

    ♡ stored CO₂ and H₂ masses must be converted through their molar masses when determining reaction availability

    ♡ Sabatier product water is routed through the WPA instead of being added directly to potable storage

    ♡ Sabatier product methane is vented outside in V1

### Gas Leakage:
    ♡ each gas has its own base leak rate tracked in kPa/h

    ♡ controlled storage venting is separate from slow habitat leaks

    ♡ current leak rates:
        - general base reference: 0.00032 kPa/h
        - O₂: 0.00048 kPa/h
        - N₂: 0.00056 kPa/h
        - Ar: 0.00040 kPa/h
        - CO₂: 0.00040 kPa/h
        - H₂: 0.0020 kPa/h

        - CH₄: 0.0 kPa/h

    ♡ CH₄ leakage remains 0.0 until a future event places methane somewhere it can leak

    ♡ calculation:
        - gas pressure lost this step:
            gas leak rate in kPa/h × step duration in hours

        - ~ gas mass lost:
            gas pressure lost × kg represented by 1.0 kPa of that gas
            
### ----------------------------------------

### Atmosphere Subsystems:
    ♡ amine swing beds / CO₂ scrubbing:
        - amine_beds.md
        - co2_scrub.py

    ♡ Oxygen Generation Assembly:
        - oga.md
        - oxygen.py

    ♡ N₂ and Ar buffer-gas management:
        - buffer_gas.py

    ♡ Major Constituent Analyzer:
        - monitors the cabin gas mixture

    ♡ Sabatier system:
        - sabatier.md
        - racks are located in the Atmosphere / Resource Recovery Room

    ♡ ISRU atmosphere and sorbent beds:
        - isru.md
        - isru_atm.py

    ♡ habitat CHX:
        - Thermal / Humidity Control file

    ♡ greenhouse CHX:
        - Greenhouse file

### ----------------------------------------

## Design Evolution:
#### 
    ♡ moved from mixed units to consistent kPa for cabin, kg for storage

    ♡ added per gas leak rates instead of one

    ♡ the first model used one vague universal gas leak rate

    ♡ individual leak rates were added because different gases escape at different rates

    ♡ when cabin volume increased by ~ 12.6 times, leak rates in kPa/h were reduced so the physical leak didn't also become 12.6 times larger

   ♡ scrub pressure per bed was reduced because the same removed mass creates a smaller kPa change in the larger cabin

### ----------------------------------------

## Future Considerations:  
    ♡ include trace gases

    ♡ consider seasonal outside pressure changes from polar CO₂ freezing and sublimation

    ♡ look into and incorporate the ~ 25 % yearly external-pressure changes

    ♡ add more detailed outside-atmosphere effects to ISRU processing

    ♡ finalize the physical space and placement of ISRU atmosphere compressors and sorbent beds

    ♡ finalize amine bed and Major Constituent Analyzer placement

    ♡ decide whether the greenhouse atmosphere will remain completely separate from the 30,176 m³ habitat atmosphere

    ♡ model controlled greenhouse and habitat air exchange (if connecting the two volumes)

    ♡ consider methane post-processing after V1 if it gets kept and design an isolated Methane Storage Bay

    ♡ add CH₄ leak detection and fire control

    ♡ MAKE SURE: Sabatier reaction code uses the 1 CO₂ : 4 H₂ mole ratio instead of treating it as a 1 kg : 4 kg mass ratio

    ♡ document the exact time basis of scrub_per_bed_kpa

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

    ♡ stored H₂, CH₄, and buffered CO₂ are treated as resources and use mass ratios (especially Sabatier)

    ♡ consistency throughout the code

#### Why place atmosphere systems in the Utility / Resource Recovery Hub?
    ♡ a lot of systems  direct connections to the water equipment and storage
    
    ♡ keeps industrial process systems together and away from living and greenhouse areas
    
    ♡ shorter runs for H₂, CO₂ and product water

#### Why N₂ and Ar together as buffer gases?
    ♡ both gases are available in the Martian atmosphere and are relatively nonreactive under normal cabin conditions
    
    ♡ ISRU systems can collect both
    
    ♡ they keep total pressure up without making the cabin all O₂

#### Why reduce leak and scrub rates in kPa?
    ♡ a fixed pressure change represents more gas in a larger volume

    ♡ keeping the old kPa/h leak rate would have a much larger leak

    ♡ amine-bed mass capacity didn't increase with habitat volume

    ♡ the kPa removed by the same bed action so I had to decrease

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
    ♡ I am going to keep h2 stored: in kg and also I'm going to make the methane(ch4) storage to be in kg b/c these are being treated as resources and I read that the Sabatier uses mass ratios, not pressure ratios

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

###### 10/01/2026
    ♡ oga is no longer capped at 0.004, max_oga_output_kpa_per_hour is now 0.0038 in oxygen.py, b/c of the massive size increase 