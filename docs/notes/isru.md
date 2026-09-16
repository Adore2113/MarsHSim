# ISRU Atm. and Water
### General Notes:
    ♡ In-Situ Resource Utilization (ISRU) collects local Mars resources to reduce dependence on Earth resupply

    ♡ the water system extracts subsurface ice and stores it as raw ISRU water

    ♡ the atmosphere system processes Mars air to collect nitrogen (N₂), argon (Ar) and carbon dioxide (CO₂)

    ♡ both systems respond automatically to habitat storage levels and power mode

    ♡ dust reduces the extraction efficiency of both systems

    ♡ power and capacity numbers are preliminary V1 estimates

    ♡ extracted raw water passes through the Water Processing Assembly before becoming potable

    ♡ collected N₂ and Ar are stored for use by the habitat buffer-gas system

    ♡ CO₂ released during sorbent-bed regeneration is added to CO₂ storage
### ----------------------------------------

## Arcadia Extraction Plan (08/18/2026):
### ISRU Water:
    ♡ total heated pipes: 6
    ♡ maximum pipes online: 6
    ♡ extracted water is sent to the raw ISRU water tank
    ♡ raw ISRU water storage is separate from potable and other non-potable water storage

    ♡ water system modes:
        - offline:
            - ISRU water system is switched off
            - pipes that are deploying or extracting are commanded to retract

        - idle:
            - system is switched on, but no pipes are extracting or deploying

        - running:
            - at least one pipe is extracting or deploying

    ♡ pipe states:
        - offline:
            - pipe is fully retracted and not extracting

        - deploying:
            - pipe is moving into extraction position
            - deployment time: ~ 25 minutes

        - extracting:
            - pipe is heating and extracting subsurface ice

        - retracting:
            - pipe is returning to its protected position
            - retraction time: ~ 45 minutes

    ♡ automatic pipe staging:
        - potable water below 1,500 kg:
            - target pipes online: 6
            - treated as a water emergency

        - potable water from 1,500 kg - below 2,600 kg:
            - target pipes online: 4

        - potable water from 2,600 kg - below 3,900 kg:
            - target pipes online: 3

        - potable water from 3,900 kg - below 5,200 kg:
            - target pipes online: 2

        - potable water at or above 5,200 kg:
            - target pipes online: 0

        - low-power mode:
            - maximum target: 2 pipes

        - critical-power mode:
            - target pipes online: 0

        - during a water emergency, a retracting pipe can reverse its decision and begin deploying again

        - outside a water emergency, a retracting pipe finishes retracting before it can be selected again

#### Water Extraction:
    ♡ base extraction rate: 
        ~ 15.0 kg/h per extracting pipe

    ♡ pipe efficiency: ~ 0.82
    ♡ dust factor reduces usable extraction
    ♡ water added is limited by the remaining capacity of the raw ISRU water tank

    ♡ calculation:
        - step duration in hours:
            step duration in minutes ÷ 60

        - ice melted this step:
            15.0 kg/h × extracting pipes × step duration in hours

        - average dust effect:
            sum of active-pipe dust factors ÷ number of extracting pipes

        - usable raw water extracted:
            ice melted × 0.82 × average dust effect

        - raw-water storage space remaining:
            raw-water storage capacity - current raw-water storage

        - water added to storage:
            the smaller of usable raw water extracted or storage space remaining

#### Water Extraction Power and Heat:
    ♡ heated-pipe power: ~ 8.5 kW per active pipe
    ♡ heat output: ~ 85 % of electrical power
    ♡ currently counts extracting and deploying pipes as active for power

    ♡ calculation:
        - active pipes:
            extracting pipes + deploying pipes

        - electrical power:
            8.5 kW × active pipes

        - electrical energy used:
            electrical power × step duration in hours

        - heat output:
            electrical power × 0.85

        - heat energy added:
            heat output × step duration in hours

### ----------------------------------------

### ISRU Atmosphere:
    ♡ compressors:
        - maximum compressors online: 4
        - compressor efficiency: ~ 0.78
        - base intake rate: 
            ~ 20.0 kg/h of raw atmosphere per effective compressor

        - compressor power: 
            ~ 4.0 kW per extracting compressor

        - compressors have no deployment or mechanical delay state in V1

        - compressors switch between offline and extracting

    ♡ system modes:
        - offline:
            - ISRU atmosphere system is switched off
            - all compressors are set to offline

        - idle:
            - atmosphere system is switched on, but no compressors are extracting

        - running:
            - at least one compressor is extracting Mars atmosphere
    
    ♡ automatic compressor staging:
        - low-storage thresholds:
            - N₂: 600 kg
            - Ar: 400 kg

        - hysteresis multiplier: 1.5
        
        - if N₂ is below 600 kg or Ar is below 400 kg:
            - target compressors online: 4

        - if N₂ is below 900 kg or Ar is below 600 kg:
            - target compressors online: 2

        - if both gases are above their hysteresis thresholds:
            - target compressors online: 0

        - low-power mode:
            - maximum target: 1 compressor

        - critical-power mode:
            - target compressors online: 0

    ♡ calculation:
        - N₂ upper threshold:
            600 kg × 1.5 = 900 kg

        - Ar upper threshold:
            400 kg × 1.5 = 600 kg

#### Mars Atmosphere Ratios:
    ♡ CO₂ ratio: ~ 0.95
    ♡ N₂ ratio: ~ 0.027
    ♡ Ar ratio: ~ 0.016
    ♡ the remaining ~ 0.007 represents gases not collected by this V1 system

#### Sorbent Beds:
    ♡ total planned beds: 5
    ♡ primary beds: 3
    ♡ backup beds: 2
    ♡ maximum beds adsorbing at once: 2
    ♡ CO₂ capture efficiency: ~ 0.85
    ♡ regeneration time: ~ 60 minutes
    ♡ bed states:
        - standby
        - adsorbing
        - regenerating

    ♡ adsorbing beds capture CO₂ from the compressed Mars atmosphere before N₂ and Ar are added to storage

    ♡ when a bed reaches capacity, it enters regeneration

    ♡ regenerating beds release their stored CO₂ gradually over the regeneration period

    ♡ released CO₂ is transferred to CO₂ storage up to its remaining capacity

    ♡ fewer available adsorbing beds reduce the amount of raw atmosphere that can be processed

#### Atmosphere Intake and Separation:
    ♡ effective compressors are limited by both extracting compressors and beds available to adsorb CO₂

    ♡ calculation:
        - beds available this step:
            the smaller of 2 or current adsorbing beds + available primary standby beds

        - effective compressors:
            the smaller of extracting compressors or beds available this step

        - raw atmosphere intake:
            20.0 kg/h × effective compressors × step duration in hours

        - average dust effect:
            sum of extracting-compressor dust factors ÷ number of extracting compressors

        - usable atmosphere intake:
            raw atmosphere intake × 0.78 × average dust effect

        - N₂ extracted:
            usable atmosphere intake × 0.027

        - Ar extracted:
            usable atmosphere intake × 0.016

        - CO₂ entering sorbent processing:
            usable atmosphere intake × 0.95

#### CO₂ Adsorption and Regeneration
    ♡ incoming CO₂ is divided equally between adsorbing beds

    ♡ each bed captures only the amount allowed by its efficiency and remaining capacity

    ♡ CO₂ that is not captured is reported as bypassed CO₂

    ♡ calculation:
        - CO₂ offered to each bed:
            incoming CO₂ ÷ adsorbing beds

        - capturable CO₂ per bed:
            CO₂ offered to each bed × 0.85

        - CO₂ absorbed by each bed:
            the smaller of capturable CO₂ or remaining bed capacity

        - bypassed CO₂:
            incoming CO₂ - total CO₂ absorbed

        - regeneration release fraction this step:
            the smaller of 1.0 or step duration in minutes ÷ 60 minutes

        - CO₂ released from a regenerating bed:
            current bed gas load × regeneration release fraction

#### Gas Storage:
    ♡ N₂ and Ar are added directly to their storage tanks after separation

    ♡ the amount added is limited by the remaining capacity of each tank

    ♡ CO₂ is added to storage when it is released during sorbent-bed regeneration

    ♡ calculation:
        - storage space remaining:
            storage capacity - current stored mass

        - gas added to storage:
            the smaller of extracted or released gas and storage space remaining

#### Atmosphere Processing Power and Heat:
    ♡ compressor power: ~ 4.0 kW per extracting compressor

    ♡ heat output: ~ 60 % of compressor electrical power

    ♡ current V1 power and heat calculations include compressors but not separate sorbent-bed loads

    ♡ calculation:
        - electrical power:
            4.0 kW × extracting compressors

        - electrical energy used:
            electrical power × step duration in hours

        - heat output:
            electrical power × 0.60

        - heat energy added:
            heat output × step duration in hours

### ----------------------------------------
## Design Evolution:
    ♡ local water extraction was left for a later v.

    ♡ high daily water losses led to development of retractable heated extraction pipes

    ♡ the first concept used two or three pipes(now uses six with automatic staging)
    
    ♡ raw ISRU water went to general water system without its own dedicated tank, a separate raw ISRU water tank and storage area were added later

    ♡ atmosphere ISRU was added to provide N₂ and Ar without resupply

    ♡ compressors had only direct on / off control

    ♡ sorbent beds were added before connecting the atmosphere system to the rest of the habitat

    ♡ the system uses a swing-bed cycle similar to the habitat amine beds

    ♡ five beds were selected so some can remain available while others regenerate

    ♡ compressor processing capacity is reduced when fewer beds can adsorb CO₂

    ♡ ISRU water variables were renamed to include water after the atmosphere ISRU system was added

### ----------------------------------------

## Future Considerations:
    ♡ decide if deploying pipes should draw power even when no pipe is already extracting

    ♡ decide how much power retraction requires and what happens if power is lost while pipes are deployed

    ♡ decide if deployed pipes can freeze during low-power or critical-power events !!

    ♡ stop or idle extraction when the raw-water tank is full instead of continuing to operate without storing additional water !!

    ♡ recalculate pipe-status output counts after an offline command changes deploying and extracting pipes to retracting

    ♡ review pipe counter updates when a deployment finishes or a pipe changes direction during the same step

    ♡ decide how much extracted-pipe heat reaches the habitat instead of the subsurface or outside environment

    ♡ decide if four compressors should stay powered when only two can process atmosphere through available sorbent beds

    ♡ add sorbent-bed power and heat requirements

    ♡ allow backup sorbent beds to support processing when primary standby beds are unavailable

    ♡ continue regeneration timers even when compressors are idle or the atmosphere system is not processing new intake

    ♡ figure out where bypassed CO₂ goes instead of allowing it to leave the tracked mass balance

    ♡ figure out what happens to extracted N₂, Ar and regenerated CO₂ when their storage tanks are full

    ♡ confirm if the Mars atmosphere ratios should be treated as mass fractions or converted from molar / volume fractions

    ♡ research compressor and sorbent-bed regeneration timing in more detail

    ♡ electrostatic dust repulsion (EDS) b/c of the fact that it's passive

### ----------------------------------------

## Design Decisions:
#### Why extract water locally?
    ♡ a 30-person crew creates a large continuing water demand

    ♡ even with water recovery, local extraction reduces dependence on stored water

    ♡ Arcadia Planitia was selected partly because of accessible subsurface water ice

#### Why use retractable heated pipes?
    ♡ heating allows subsurface ice to be melted for collection

    ♡ retraction protects pipes when they are not needed and automatic deployment allows the system to respond to changing potable-water levels

#### Why give raw ISRU water its own storage area?
    ♡ extracted water has not yet passed through the Water Processing Assembly

    ♡ separating it from potable water protects water quality

    ♡ dedicated storage makes routing and maintenance easier to understand

#### Why extract N₂ and Ar from the Mars atmosphere?
    ♡ N₂ and Ar are required to maintain the selected habitat buffer-gas mixture

    ♡ local collection supports long-duration operation without regular gas resupply

#### Why remove CO₂ before storing N₂ and Ar?
    ♡ Mars atmosphere is mostly CO₂

    ♡ sorbent beds remove most of the CO₂ from the processed stream letting the smaller N₂ and Ar portions to be collected separately

#### Why use multiple sorbent beds?
    ♡ adsorption must continue while another bed regenerates

    ♡ multiple beds provide cycling capacity and redundancy

    ♡ backup beds reduce the risk of losing all atmospheric processing when a bed is unavailable

#### Why do compressors switch states immediately?
    ♡ unlike the physical travel time of the water pipes, V1 does not model a mechanical deployment delay for compressors

    ♡ immediate switching keeps the first atmosphere model manageable

### ----------------------------------------

### Dev Log Notes:
###### From v1_scope:
    ♡ I read about In-Situ Resource Utilization (ISRU) to extract water locally but I'll worry about that later

    ♡ while testing the water outputs, I can see that the net loss per sol is way too high, so I'm going to go over some numbers

    ♡ 115.5kg per sol is just the cost of having a 30 person crew

    ♡ I was thinking about other way to recycle and actually get water and I thought about piercing through the surface with two or three heated pipes that siphon up some frozen mars water every so often? retractable pipes so they don't freeze and can be used at will, I'm going to do some reasearch on this

    ♡ going back to In-Situ Resource Utilization (ISRU) to extract water locally, I'm thinking piercing through the surface with two or three heated pipes that siphon up some frozen mars water every so often with retractable pipes so they don't freeze and can be used when wanted and needed to avoid environmental factors


###### 05/22/2026
    ♡ I was thinking about other way to recycle and actually get water and I thought about piercing through the surface w. two or three heated pipes that siphon up some frozen Mars water every so often? retractable pipes so they don't freeze and can be used at will, I'm going to do some research on this

    ♡ going back to In-Situ Resource Utilization (ISRU) to extract water locally, I'm thinking piercing through the surface w. two or three heated pipes that siphon up some frozen Mars water every so often w. retractable pipes so they don't freeze and can be used when wanted and needed to avoid environmental factors

###### 05/25/2026
    ♡ fixing isru and added modes and pipe retraction and extraction

###### 06/20/2026
    ♡ setting up ISRU file for Ar and N₂, which is crucial for no resupply w. a con being power usage

    ♡ I am not going to have a timer for the compressors yet, but for future versions I am planning on adding a regen state and usig absorption/sorbent beds that need a regen cycle between intakes

###### 06/21/2026

    ♡ I decided I'm going to add the sorbent beds to the isru_atm file before continueing to connect it to the other files

    ♡ don't forget to add isru_water to dust file

    ♡ I'm going to use five sorbent beds in total, two as backups as I like to have, so there are enough to absorb while another bed regenerates

    ♡ sorbent beds trap CO₂ from compressed Mars air before N₂/Ar and gets added to storage. This is modeled as a swing bed cycle, like the amine beds in CO₂_scrub.py.

    ♡ regen stop processing taking that bed fully offline, fewer adsorbing beds online = less raw atmosphere gets processed, meaning less N₂ and Ar gets added to storage too

    ♡ unlike isru water pipes that have a real physical deploy/retract travel time, a compressor has no mechanical delay, so it just flips between "offline" and "extracting" based on target amount needed online for each step

###### 06/24/2026
    ♡ adding dust to irsu_water.py

###### 06/30/2026
    ♡ realized that I didn't rename my isru water variables to include the word water after adding isru_atm

###### 07/21/2026

    ♡ while going over my isru files, the pipes in my isru file are set up so that they can switch their decision to deploy or retract, in case of low water emergencies

    ♡ I am considering if all of a sudden the pipes are deploying and the low power mode hits or I lose power if the pipes don't retract, they will freeze or use a lot of power w. the heated pipes, but retracting doesn't use power in v1, which I'm questioning now

###### 08/18/2026
    ♡ adding an extra tank for the isru system

###### 08/22/2026
    ♡ I considered keeping all the non-potable water tanks together, but I'd like the seperation between the ISRU raw water to have it's own area

###### 09/13/2026
    ♡ added water ISRU room to handle drawing in Mars atmosphere, removing dust before compression, compressing the intake gas, separating useful atmospheric gases and transferring recovered gases toward habitat storage or use

###### 09/16/2026
    ♡ while going over oga.md and my code, I realized these things: 
        - the retract is still 0 kW
        - pipes can keep drawing heat if low power hits while they are out
        - full raw tank still “runs” with 0 kg added
        - bypassed CO₂ is not stored
        - sorbent beds have no power term