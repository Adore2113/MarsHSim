# ISRU Atm. and Water
### General Notes:
    ♡ In-Situ Resource Utilization (ISRU) collects local Marts resources to reduce dependence on Earth resupply

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

    ♡ water sytem modes:
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
