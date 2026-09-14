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
        - receives condensate from habitat CHX and greenhouse CHX

    ♡ located for short routes between gray / black / brine tanks and clean water storage

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
    ♡ it is sized for 30-crew brine with hysteresis, not continuous full UPA
    ♡ the large brine tank is the burst buffer

#### Wastewater Storage Room:
    ♡ floor area: ~ 90 m²
    ♡ width: ~ 10.0 m
    ♡ height: ~ 4.5 m
    ♡ volume: ~ 405 m³
    ♡ calculation: ~ 10.0 m × 9.0 m × 4.5 m = 405 m³

    ♡ access / placement:
        - next to the Water Processing Room
        - away from living rooms and the greenhouse grow floor

    ♡ includes:
        - gray water storage
        - black water storage
        - brine storage
        - service space around the tanks

    ♡ used for:
        - holding wastewater before processing
        - giving UPA / WPA / BPA a buffer so they do not have to run flat-out

    ♡ earlier size range was 80-100 m²
    ♡ 90 m² is the V1 size used in the 340 m² total

#### ISRU Water Room:
    ♡ floor area: ~ 50 m²
    ♡ width: ~ 8.0 m
    ♡ height: ~ 4.5 m
    ♡ volume: ~ 225 m³
    ♡ calculation: ~ 8.0 m × 6.25 m × 4.5 m = 225 m³

    ♡ access / placement:
        - in the utility hub
        - connects to the Water Processing Room
        - not on the living side

    ♡ includes:
        - raw ISRU water storage
        - service space around the tanks
        - transfer toward water processing

    ♡ used for:
        - holding incoming ISRU water before it is cleaned

    ♡ raw ISRU water at ~ 4,000 kg fits in this room
    ♡ earlier size range was 40-60 m²
    ♡ 50 m² is the V1 size used in the 340 m² total

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
            ~ washing-machine sized, ~ 0.4 m³/rack
        - CO₂ feed and small buffer
        - condenser and water separator
        - Sabatier water line towards Water Processing Room
        - 8 amine beds
        - amine bed thermal and vent connections
        - amine bed bay: ~ 40-50 m² within the room
        - controlled Sabatier methane vent line
        - methane sensors and automatic isolation valve
        - controls, valves and sensors
        - MCA interface
        - minimum maintenance aisle width: ~ 1.2 m

    ♡ used for:
        - oxygen generation
        - CO₂ removal and temporary storage
        - Sabatier water recovery
        - atmosphere monitoring and recovery
        - keeping connected life-support equipment together

    ♡ this room is not part of the 340 m² / 1,530 m³ water room total

     ♡ methane produced by the Sabatier is vented outside through a controlled line for V1and is never intentionally released into the habitat

    ♡ dedicated methane storage is not included in V1

    ♡ V1 room size remains ~ 120-140 m² until equipment placement and maintenance clearances are finalized

 **#### Atmosphere / Resource Recovery Room:**

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

        - 3 Sabatier racks

        - each Sabatier rack is approximately washing-machine sized (~ 0.4 m³)

        - CO₂ feed and small buffer

        - condenser and water separator

        - Sabatier water line toward the Water Processing Room

        - 8 amine beds

        - amine-bed thermal and vent connections

        - amine-bed bay: ~ 40-50 m² within the room

        - controlled Sabatier methane vent line

        - methane sensors and automatic isolation valve

        - controls, valves and sensors

        - MCA interface

        - minimum maintenance aisle width: ~ 1.2 m

    ♡ used for:

        - oxygen generation

        - CO₂ removal and temporary storage

        - Sabatier water recovery

        - atmosphere monitoring and recovery

        - keeping connected life-support equipment together

    ♡ methane produced by the Sabatier is vented outside through a controlled line for V1

    ♡ methane is never intentionally released into the habitat atmosphere

    ♡ dedicated methane storage is not included in V1

    ♡ this room is not part of the 340 m² / 1,530 m³ water-room subtotal

    ♡ V1 room size remains ~ 120-140 m² until equipment placement and maintenance clearances are finalized
### ----------------------------------------
