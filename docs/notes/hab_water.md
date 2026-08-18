# Habitat Water System
### General Notes:
    ♡ water demands are slightly over estimated becuase I would rather overestimate than under when it comes to values of usage/demand

    ♡

    ♡

### ----------------------------------------

## Arcadia Water System Plan (08/18/2026):
#### Layout
##### Water Recovery/Processing Room:
    ♡ shape: octagon (regular)
    ♡ floor area: 90 m²
    ♡ total height: 4.5 m
    ♡ width: 
        ~ 10.4 m across opposite walls

    ♡ wall length:
        ~ 4.3 m for each outside wall

    ♡ center distance:
        ~ 5.2 m from the center to each wall

    ♡ corner distance:
        ~ 5.6 m from the center to each corner

    ♡ overall corner to corner width:
        ~ 11.3 m from one corner to the opposite corner

    ♡ roof: lightly angled

    ♡ entrances: 
        two (one from the direct hallway to social hub, one from the greenhouse connection)

    ♡ contains processors and working equipment for water recovery/proccessing:
        - UPA + pretreatment
        - WPA (including gray water and condensate)
        - BPA
        - pumps, filters, catalytic reactors, etc.
        - sampling / water quality hardware
        - control cabinets
        - consumables storage
        - maintenance aisles and extra space

##### Water Storage Room:
    ♡ shape: octagon (regular)
    ♡ floor area: 120 m²
    ♡ total height: 4.5 m
    ♡ width: 
        ~ 12.0 m across opposite walls

    ♡ wall length (if octagon):
        ~ 5.0 m for each outside wall

    ♡ roof: 
        flat or lightly angled

    ♡ entrances: recovery / Processing Room, one from the direct hallway / social hub side

    ♡ contains vertical cylindrical habitat water tanks

    ♡ notes:
        - tanks are fully inside the pressurized, heated volume (V1)

        - clear access for inspection, sensors, and maintenance

        - separated from equipment so the process flow stays clean

        - greenhouse keeps only its own local zone reservoirs

### ----------------------------------------

#### Tank Capacities
    ♡ potable water storage capacity: 10,000.0 kg
    ♡ gray water storage capacity: 3,500.0 kg
    ♡ black water storage capacity: 1,800.0 kg
    ♡ condensate storage capacity: 5,000.0 kg
    ♡ brine storage capacity:1000.0 kg
    ♡ raw ISRU water: 4,000 kg capacity
    ♡ greenhouse reservoirs (total): ~ 2,000 kg
        - see greenhouse\hydroponics.md
   
#### Crew Water Demands: 
    ♡ demand total: ≈ 1,450 kg/sol, 
        - ~ 2,660 kg/sol (as a max theoretical)

    ♡ shower system:
        - normal mode: 
            10 min recommended, 20 min cut off
        - conservation mode: 7–10 min
        - low water mode: 5 min
        - critical mode: timed preset buttons, enforcing a navy type shower (very short, low flow)
    
    ♡ breakdown (kg/person/sol):
        - drinking + food rehydration: 
            ♡ 2.5 kg/person/sol
            ♡ total ≈ 75.0 kg/sol

        - personal hygiene (sink, face, hands, oral)
            ♡ 1.2 kg/person/sol
            ♡ total ≈ 36 kg/sol

        - shower:
            ♡  40 kg/person/sol
            ♡ total ≈ 1,200 kg/sol

        - shared laundry:
            ♡  3.0 kg/person/sol
            ♡ total ≈ 90 kg/sol

        - toilet:
            ♡ 0.5 kg/person/sol
            ♡ total ≈ 15kg/sol
        
        - misc:
            ♡ 0.5 kg/person/sol
            ♡ total ≈ 15kg/sol

        - steam room (for future reference):
             0.8 kg/person/sol
            ♡  total ≈ 24 kg/sol

#### :
    ♡ 

### ----------------------------------------

#### :
    ♡ 

    ♡

    ♡
### ----------------------------------------

## Design Evolution:
    ♡ original  tank capacities:  
        - potable water storage capacity: 6500.0 kg
        - gray water storage capacity: 1200.0 kg
        - black water storage capacity: 800.0 kg
        - condensate storage capacity: 250.0 kg
        - brine storage capacity: 400.0 kg

    ♡

    ♡
### ----------------------------------------

## Future Considerations:
    ♡ electrostatic dust repulsion (EDS) b/c of the fact that it's passive

    ♡ scheduled cleaning (possibly automated)

    ♡ dust repellent coatings that need to be reapplied over time

    ♡

    ♡
### ----------------------------------------

## Design Decisions:
#### Why separate water processing from water storage?
    ♡  so the process flow stays clean

    ♡  maintenence access would be awkward and disturb the greenhouse

    ♡  the dirty part of the system won't be near the clean growing area

    ♡  to make sure there was enough room for everything

#### Why allow continuous-flow showers?
    ♡ there are only 30 crew members and all of them but there should be a max time amount, I'm thinking 15 minutes as a hard maximum, 10 minutes as standard, 5 minutes in low water mode, and a very short, low-flow shower mode; "Navy" shower mode 1. water on = wet yourself, 2. water off = soap/shampoo 3. water on = rinse 4.done ( maybe controlled with a push button?)

    ♡ making the shower cut off at 20 minutes instead of 15, some people like longer showers and if I will reduce it to 15 if need be

#### Why overestimate crew water demand?
    ♡ ideally the habitat has a safe buffer

    ♡ overassuming instead of under estimating is safer

    ♡ the crew can live comfortably and have things like non-timed showers

#### Why send captured greenhouse condensate through the WPA?
    ♡ greenhouse condensate is recoverable water but it needs treatment before storage

    ♡ routing it through the WPA keeps greenhouse recovery connected to the same central habitat water treatment loop as other recoverable water streams

    ♡ this allows WPA efficiency and processing losses to affect the final amount returned to storage

#### Why use treated habitat water for greenhouse make-up in V1?
    ♡ the greenhouse is part of the same closed habitat water inventory

    ♡ using treated habitat water keeps the greenhouse connected to the water recovery system

    ♡ raw wastewater is not sent directly into the greenhouse reservoirs

    ♡ nutrient recovery from crew waste is planned for the future, but nutrients are treated separately from water in V1 

### ----------------------------------------

### Dev Log Notes:
###### 03/13/2026
    ♡ figure out how much water(H2O) the OGA and water electrolysis uses every time it runs, I'm going to find the fixed reaction ratio instead of a fixed ratio b/c the amount of O₂ produced are going to change depending on habitat events

    ♡ going to use 1000kg of water to start as a placeholder to finish the OGA functions

    ♡ going to keep the OGA functions separate instead of one big function w. a comment to sort of group them together, I feel like that will be better for future readability

    ♡ finished OGA and water electrolysis for now, moving onto argon and nitrogen

###### 03/24/2026
    ♡ I chose the starting amounts for some power variables and made a separate file for the OGA and water electrolysis

###### 04/22/2026
    ♡ doing some research before starting water_system.py to know what kind of water system makes sense w. focus on reusability

    ♡ going w.:
        -Urine Processor Assembly (UPA)
        -Water Processor Assembly (WPA)
        -Brine Processor Assembly (BPA)

    ♡ worked on the water system file

    ♡ I read about In-Situ Resource Utilization (ISRU) to extract water locally but I'll worry about that later

###### 04/23/2026
    ♡ adding condensate/CHX to water_system and engine and made OGA use potable water

###### 04/27/2026
♡ started to add sabatier info/logic into my water system file

###### 05/22/2026
    ♡ I added in the Sabatier into water.py, b/c I forgot to add it in the storage update and run_water_system function 

    ♡ while testing the water outputs, I can see that the net loss/sol is way too high, so I'm going to go over some numbers

    ♡ 115.5kg/sol is just the cost of having a 30 person crew

    ♡ I was thinking about other way to recycle and actually get water and I thought about piercing through the surface w. two or three heated pipes that siphon up some frozen Mars water every so often? retractable pipes so they don't freeze and can be used at will, I'm going to do some research on this

    ♡ going back to In-Situ Resource Utilization (ISRU) to extract water locally, I'm thinking piercing through the surface w. two or three heated pipes that siphon up some frozen Mars water every so often w. retractable pipes so they don't freeze and can be used when wanted and needed to avoid environmental factors

###### 05/23/2026
    ♡ I created a file for handling water extraction and I'm going to make a list in state, similar to the lists I have for the other subsystems and add in each pipe, in case I want to add more later and of course to have a few as backup

    ♡ I realized that I didn't have water runoff from the greenhouse, so I implemented that today and also fixed and cleaned up water.py, after including the for now very basic isru system

###### 05/25/2026
    ♡ fixing isru and added modes and pipe retraction and extraction

    ♡ going over water file, adding hysteresis and updating power used logic to make it more similar to CO₂_scrub.py

    ♡ updated power usage in water.py

    ♡ updating systems to include low power mode

###### 06/30/2026
    ♡ I need to decide if I want to keep the water outputs in water, but that's 27 lines which is a lot for on panel, so I need to choose if I want to keep them in water, or put them in their corrosponding panels ( UI NOTES )

###### 08/15/2026
    ♡ NASA ECLSS systems treat condensate as a recoverable wastewater stream, and plant growth life support research looks into recovering and reusing transpired water vapor, so using ~ 95% capturing efficiency seems right so that the recovery isn't perfect, but still a small amount doesn't get collected

    ♡ things like maintenance/flushing, minor leakage, evaporation from exposed solution or wet surfaces, and solution retained in equipment/LECA during servicing all add into the the water losses, but I think I'm just going to use a small recirculation loss, and make each zone have a different percentage, mostly b/c of the different growing conditions, considering the ~ 95% capturing efficiency

###### 08/18/2026
    ♡ today I'll be going over my entire habitat's water system

    ♡ I need to remember to go back over my make-up water demand values so they don't dominate the water balance after I get the water system set up

    ♡ consider crew laundry and other misc. things

    ♡ I'm going to lower my UPA rate b/c reasaech shows that my previously decided system was a bit optimistic, so I will lower it from 0.94 to between 0.70 - 0.87. I'm also going to increase the recovery fraction from the BPA. I read that it usually recovered more, so I can move this to between 0.95-0.98

    ♡ I'm going to look at my storage tank capacities and then figure out how I want the layout to be, this is a simulator and only v1, so I'm not going to have incredibly detailed layout plans

    ♡ current tank capacities:  
        - potable_water_storage_capacity_kg = 6500.0,
        - gray_water_storage_capacity_kg = 1200.0,
        - black_water_storage_capacity_kg = 800.0,
        - condensate_storage_capacity_kg = 250.0,
        - brine_storage_capacity_kg = 400.0,

    ♡ increasing these tank capacities, b/c they were too small, the condensation alone can go up to 2,600 k/sol, and I need there to be a lot more water storage for long term survival

    ♡ adding an extra tank for the isru system

    ♡ ISS keeps a minimum reserve of ~ 800–1,600 kg of potable water in contingency after containers and MASA studies size water storage for only ~ 30 days of open-loop operation, and I read that you should plan for the largest expected daily usage plus unanticipated events

    ♡ sticking with my octagon/hive style layout, I can work on a water utility room for the water

    ♡ I want a water utility hub with clean, distinct corridors leading off to different rooms/octagons in the habitat, I think there should be an obvious split between the greenhouse/food area and the utilities that handle things like wastewater and things you don't really want to think about while wanting a clean area

    ♡ steam room can be a potential future version consideration ( pros: real benefits, high recovery rate and a small earth luxury.. cons: extra water demand (hardly b/c of recovery, extra head and humidity load, ventilation is important but maintenance and cleaning needs to be considered), I will add it in my notes though b/c I am undecided

    ♡ crew water demand are rough estimates for now, overassumed instead of under, and the drinking and food rehydration is based on NASA's baseline, the personal hygiene value is higher than the ISS minimum, and some other values are averaged

    ♡ I think that the crew should be able to have showers with constant water, there are only 30 of them but there should be a max time amount, I'm thinking 15 minutes as a hard maximum, 10 minutes as standard, 5 minutes in low water mode, and a very short, low-flow shower mode; "Navy" shower mode 1. water on = wet yourself, 2. water off = soap/shampoo 3. water on = rinse 4.done ( maybe controlled with a push button?)

    ♡ making the shower cut off at 20 minutes instead of 15, some people like longer showers and if I will reduce it to 15 if need be

    ♡ I am using misc to represent little things like eye washing stations, extra consumption, etc.

    ♡ the water utility area containing the water tanks, aren't going to be light-admitting, or if they are, it won't be a priority b/c I want to make sure enough true light gets in here to see well

    ♡ I did consider the tanks outside of the habitat, but that opens up a lot of other issues like maintenece issues, but I am thinking about partially burried tanks, where only about 30-40% of the large tanks only show in the warm water utility room so everything can stay in the heated room, but I will have to add extra heaters, insulation, leak detection, etc. and the freezing risk is massive, for v1 I'm sticking with keeping the tanks fully inside the water utility room

    ♡ I decided to size the water utility room around the water equipment

    ♡ I considered keeping water tanks in the storage under the ramps in the greenhouse but I decided to keep those seperate

    ♡ small permanent losses = uncaptured vapor, operational losses, biomass water, residual brine
