# Utility / Resource Hub Layout Plans
### General Notes:
    ♡ preliminary estimates

    ♡ floor areas below are the rooms themselves and are net room areas unless marked otherwise

    ♡ every room is assumed to have sensors

    ♡ this is the industrial process hub and stays separated from living areas and greenhouse

    ♡ atmosphere / resource recovery is in this hub

    ♡ equipment volume is included within its room and isn't added separately

    ♡ the Power / Energy Hub is adjacent to this hub but is calculated separately (see energy_hub.md)

### ----------------------------------------

## Arcadia Utility / Resource Hub (updated 09/13/2026):

#### Total Utility Water Rooms:
    ♡ current combined floor area: ~ 340 m²
    ♡ current combined volume: ~ 1,530 m³
    ♡ height used for V1: ~ 4.5 m

    ♡ Water Processing Room:
        - floor area: ~ 90 m²
        - volume: ~ 405 m³

    ♡ Wastewater Storage Room:
        - floor area: ~ 90 m²
        - volume: ~ 405 m³

    ♡ ISRU Water Room:
        - floor area: ~ 50 m²
        - volume: ~ 225 m³

    ♡ Potable Water Storage Room:
        - floor area: ~ 110 m²
        - volume: ~ 495 m³

    ♡ calculation:
        - 90 + 90 + 50 + 110
          = 340 m²

        - 405 + 405 + 225 + 495
          = 1,530 m³

        - 340 m² × 4.5 m
          = 1,530 m³

    ♡ access / placement:
        - industrial zone
        - reachable for maintenance and emergencies without passing the main living spaces
        - more than one way in and out

    ♡ contains:
        - Water Processing Room
        - Wastewater Storage Room
        - ISRU Water Room
        - Potable Water Storage Room
        - Atmosphere / Resource Recovery Room
        - Methane Storage Bay

### ----------------------------------------

#### Water Processing Room:
    ♡ shape: rectangle
    ♡ floor area: ~ 90 m²
    ♡ width: ~ 10.0 m
    ♡ height: ~ 4.5 m
    ♡ volume: ~ 405 m³
    ♡ calculation:
        - ~ 10.0 m × 9.0 m = 90 m²
        - ~ 90 m² × 4.5 m = 405 m³

    ♡ minimum maintenance aisle width: ~ 1.2 m

    ♡ access / placement:
        - connects to wastewater storage
        - connects to potable storage
        - connects to the ISRU water room
        - connects to the utility hallway

    ♡ short routes between gray / black / brine tanks and clean water storage

    ♡ includes:
        - UPA and pretreatment
        - WPA
        - BPA
        - pumps, filters, catalytic reactors
        - sampling hardware
        - control cabinets
        - consumables storage
        - maintenance aisles

    ♡ used for:
        - all recovery and treatment work
        - turning wastewater and condensate into usable water
        - handling brine in bursts, not as a continuous full-load process

    ♡ BPA is kept at 0.5 kg/h
    ♡ the large brine tank is the burst buffer
    ♡ it is sized for 30-crew brine with hysteresis, not continuous full UPA

#### Wastewater Storage Room:
    ♡ floor area: ~ 90 m²
    ♡ width: ~ 10.0 m
    ♡ height: ~ 4.5 m
    ♡ volume: ~ 405 m³
    ♡ calculation: ~ 10.0 m × 9.0 m × 4.5 m = 405 m³

    ♡ access / placement:
        - next to the Water Processing Room
        - away from living rooms and greenhouse 

    ♡ includes:
        - gray water storage
        - black water storage
        - brine storage
        - service space around the tanks

    ♡ used for:
        - holding wastewater before processing
        - giving UPA / WPA / BPA a buffer

#### ISRU Water Room:
    ♡ floor area: ~ 50 m²
    ♡ width: ~ 8.0 m
    ♡ height: ~ 4.5 m
    ♡ volume: ~ 225 m³
    ♡ calculation: ~ 8.0 m × 6.25 m × 4.5 m = 225 m³

    ♡ access / placement:
        - in the utility hub
        - connects to the Water Processing Room
        - not on the living area side

    ♡ includes:
        - raw ISRU water storage
        - service space around the tanks
        - transfer toward water processing

    ♡ used for:
        - holding incoming ISRU water before it is cleaned

    ♡ raw ISRU water at ~ 4,000 kg fits in this room

#### Potable Water Storage Room:
    ♡ floor area: ~ 110 m²
    ♡ width: ~ 11.0 m
    ♡ height: ~ 4.5 m
    ♡ volume: ~ 495 m³
    ♡ calculation: ~ 11.0 m × 10.0 m × 4.5 m = 495 m³

    ♡ access / placement:
        - next to the Water Processing Room
        - clean side of the water rooms

    ♡ includes:
        - potable tanks
        - access around the tanks
        - transfer toward habitat use

    ♡ used for:
        - holding clean water after processing

    ♡ potable water itself is only about 10 m³
    ♡ the extra floor area is for tanks, structure and walking space

### ----------------------------------------

#### Atmosphere / Resource Recovery Room:
    ♡ shape: rectangle
    ♡ floor area: ~ 120-140 m²
    ♡ height: ~ 4.5 m
    ♡ volume: ~ 540-630 m³
    ♡ calculation:
        - 120 m² × 4.5 m = 540 m³
        - 140 m² × 4.5 m = 630 m³
    
    ♡ minimum maintenance aisle width: ~ 1.2 m

    ♡ access / placement:
        - in the Utility / Resource Hub
        - near the Habitat CHX / Air-Handling Room
        - near the ISRU Atmosphere Room
        - short water line to the Water Processing Room
        - connects to the utility hallway
        - controlled methane vent line leads outside the habitat

    ♡ includes:
        - OGA
        - oxygen distribution connection
        - hydrogen buffer and transfer line to Sabatier
        - 3 Sabatier racks:
            ~ washing-machine sized (~ 0.4 m³/rack)
        - CO₂ feed and small buffer
        - condenser and water separator
        - Sabatier water line to Water Processing Room
        - 8 amine beds
        - amine bed thermal and vent connections
        - amine bed bay: ~ 40-50 m² within the room
        - controlled Sabatier methane vent line
        - methane sensors and automatic isolation valve
        - controls, valves and sensors
        - MCA interface

    ♡ used for:
        - oxygen generation
        - CO₂ removal and temporary storage
        - Sabatier water recovery
        - atmosphere monitoring and recovery
        - keeping connected life-support equipment together

     ♡ methane produced by the Sabatier is vented outside through a controlled line for V1 and is never intentionally released into the habitat

    ♡ dedicated methane storage is not included in V1

    ♡ V1 room size is ~ 120-140 m² until equipment placement and maintenance clearances are finalized

#### ISRU Atmosphere Room:
    ♡ shape: rectangle
    ♡ floor area: ~ 80 m²
    ♡ width: ~ 10.0 m
    ♡ height: ~ 4.5 m
    ♡ volume: ~ 360 m³
    ♡ calculation:
        - ~ 10.0 m × 8.0 m = 80 m²
        - ~ 80 m² × 4.5 m = 360 m³

    ♡ minimum maintenance aisle width: ~ 1.2 m

    ♡ real world size reference:
        - ~ a large industrial workshop room

    ♡ access / placement:
        - at the exterior edge of the Utility / Resource Hub
        - near the Atmosphere / Resource Recovery Room
        - connects to the utility hallway
        - exterior connection to Mars atmosphere
        - reachable without passing through living areas

    ♡ includes:
        - exterior atmosphere intake
        - intake isolation valve
        - dust filtration and dust collection
        - compressor equipment
        - sorbent beds
        - separated gas transfer lines
        - controls, valves and sensors

    ♡ used for:
        - drawing in Mars atmosphere
        - removing dust before compression
        - compressing the intake gas
        - separating useful atmospheric gases
        - transferring recovered gases
    
    ♡ exterior intake equipment is not included in the pressurized room volume
    
    ♡ the room can be isolated from the rest of the Utility Hub during issues or maintenance

### ----------------------------------------

### Combined Area:
    ♡ Water Processing Room:
        - floor area: ~ 90 m²
        - height: ~ 4.5 m
        - volume: ~ 405 m³

    ♡ Wastewater Storage Room:
        - floor area: ~ 90 m²
        - height: ~ 4.5 m
        - volume: ~ 405 m³

    ♡ ISRU Water Room:
        - floor area: ~ 50 m²
        - height: ~ 4.5 m
        - volume: ~ 225 m³

    ♡ Potable Water Storage Room:
        - floor area: ~ 110 m²
        - height: ~ 4.5 m
        - volume: ~ 495 m³

    ♡ combined water-room totals:
        - floor area: ~ 340 m²
        - volume: ~ 1,530 m³
        - calculation:
            ~ 90 + 90 + 50 + 110
            = ~ 340 m²

            ~ 405 + 405 + 225 + 495
            = ~ 1,530 m³

    ♡ Atmosphere / Resource Recovery Room:
        - floor area: ~ 120-140 m²
        - volume: ~ 540-630 m³
        - not included in the 340 m² water total

    ♡ Methane Storage Bay:
        - not sized yet
        - not included in the 340 m² water total

### ----------------------------------------

### Design Decisions:
#### Why keep the utility rooms out of living and greenhouse space?
    ♡ dirty / noisy process areas should stay away from where people eat, sleep and grow food

    ♡ maintenance and emergencies should not have to go through the main living rooms

#### Why keep atmosphere systems in this hub?
    ♡ they connect with the water systems and storage

    ♡ it keeps the major life-support process equipment together

    ♡ it avoids scattering industrial systems into living or greenhouse space

#### Why are the water rooms small next to the power rooms?
    ♡ potable water itself is only about 10 m³
    ♡ 110 m² is already generous for that tank, access and structure

    ♡ gray, black and brine tanks are smaller than the battery corridor
    ♡ 4,000 kg of raw ISRU water fits in 40-60 m²
    ♡ UPA, WPA and BPA with aisles fit in about 90 m² for 30 crew

    ♡ the utility hub gets bigger when atmosphere recovery and methane storage are counted with the water rooms

#### Why is the greenhouse CHX bay not in this file?
    ♡ it sits on the greenhouse ground floor so it can take plant air there

    ♡ only the condensate line comes here

### ----------------------------------------

## Design Evolution:
    ♡ wastewater storage started as an 80-100 m² range

    ♡ ISRU water started as a 40-60 m² range

    ♡ those ranges were locked to 90 m² and 50 m² so the four rooms add to 340 m²

    ♡ atmosphere recovery started as a 120-140 m² range
    ♡ that range is still open

### ----------------------------------------

## Future Considerations:
    ♡ lock one floor size for the Atmosphere / Resource Recovery Room

    ♡ size the methane storage bay

    ♡ exact corridor widths and emergency routing around this hub

    ♡ height variations between living and utility spaces

    ♡ workshop space for fumes, dust and fire-risk work stays out of the hobby studio

### ----------------------------------------

## Dev Log Notes:
###### 08/23/2026
    ♡ finalize Wastewater Storage Room (currently 80-100 m² range)

    ♡ finalize ISRU Water Room (currently 40-60 m² range)

    ♡ Sabatier racks are located in the Atmosphere / Resource Recovery Room
    ♡ 3 Sabatier racks planned for redundancy
    ♡ each rack is approximately washing-machine sized (~ 0.4 m³)

###### 08/24/2026
    ♡ after entering the total floor area and volume for the utility / resource area, the water rooms seem small compared to the power rooms, but potable holds ~ 10 m³ of water itself, so ~ 110 m² room gives generous tank space, access, and structure, the other gray, black and brine water are smaller, so that space makes sense as well, the raw ISRU water at 4,000kg fits in 40–60 m² and the UPA, WPA and BPA equipment fits in ~ 90 m² with aisles sounds good for a 30 crew plan.. power just seems massive in comparison b/c the secondary battery corridor I made is bigger than my original habitat plan b/c of the amount of space they need.. when I add more rooms to the resource recovery area it will be bigger for sure

###### 09/13/2026
    ♡ although NASA investigated methane post-processing for deeper oxygen loop closures, it would be another subsystem, which I will be something to be implemented in the future