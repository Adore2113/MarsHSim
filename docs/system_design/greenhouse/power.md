# Greenhouse Power:
### General Notes:
    ♡ this file covers total greenhouse power draw and equipment load

    ♡ running the greenhouse (LEDs, pumps, circulation) consumes power continuously while online, creating the same kind of engineering trade off as the solar field's maintenance draw

 ### ----------------------------------------

## Greenhouse Power Usage (08/11/2026 update):
#### Plant Light Power:
    ♡ full mechanism in lighting.md, summarized here as part of total greenhouse draw

    ♡ using current Hive-8 total effective grow area: 1,350 m² (420 + 480 + 450, structural + container + rack)

    ♡ LED power density: 0.12 kW/m²

    ♡ plant lighting power depends on effective grow area and LED level

    ♡ natural sunlight and partial LED support reduce actual energy use

    ♡ theoretical max, full LED support, full 16 hour period: ~ 2,592 kWh/sol
    
    ♡ calculation:
        - full LED power: 1,350 m² × 0.12 kW/m² = 162 kW

        - max energy over 16 hours: 162 kW × 16 hours = 2,592 kWh/sol

    ♡ full support LED heat: ~ 110.2 kW, noted b/c it's part of the greenhouse's total thermal load alongside structural heat below

#### Greenhouse Equipment Power:
    ♡ preliminary base equipment power: 0.05 kW/m²

    ♡ intended to represent equipment such as:
        - pumps
        - circulation
        - greenhouse support equipment

    ♡ this load is not currently included in the simulation's total power use

    ♡ calculation (using ~1,326 m² greenhouse floor area):
        - 0.05 kW/m² × 1,326 m² ≈ 66.3 kW

        - maximum energy over one Mars sol:
            66.3 kW × 24.66 hours ≈ 1,635 kWh/sol

    ♡ to do:
        - add greenhouse equipment power and energy to greenhouse_outputs
        
        - add greenhouse equipment power and energy to power.py
        
        - separate pumps, circulation and other equipment loads later if needed

### ----------------------------------------

## Heat Generated:
#### Plant Light Heat:
    ♡ LED heat ratio: 0.68
    ♡ structural heat density: 0.015 kW/m²

    ♡ calculation (full LED):
        - LED heat output: 
            plant LED power × 0.68

        - maximum heat output at 162 kW:
            162 kW × 0.68 ≈ 110.2 kW

        - maximum heat energy over 16 hours:
            110.2 kW × 16 hours ≈ 1,763 kWh/sol

#### Structural Heat:
    ♡ structural heat: 0.015 kW/m²

    ♡ calculation:
        - structural heat:
            0.015 kW/m² × 1,350 m² ≈ 20.3 kW

        - heat energy over one sol(~24.66 h):
            20.3 kW × 24.66 hours ≈ 500 kWh/sol

### ----------------------------------------

#### Future Considerations:
    ♡ 

### ----------------------------------------

## Design Decisions:
#### Why an LED heat ratio of 0.68?
    ♡ I read that horticulture LED lights turn ~ 30-40 % of electricity into light, so about ~ 0.60 - 0.70 waste heat seemed right 

#### Why keep LED power/heat mechanics out of this file?
    ♡ both led power and heat are computed inside greenhouse_lighting()'s loop per zone, with other lighting info

    ♡  they're part of the lighting system, not a separate greenhouse subsystem
 
    ♡ keeping the mechanism in one place (lighting.md) avoids the same calculation being maintained in two files

### ----------------------------------------

### Dev Log Notes:
##      05/11/2026
     ♡ adding heat from the LED lights in my greenhouse_lighting function

##      07/23/2026
    ♡ my sim is running on average:  Solar Generated = 559.26 kwh, Total Power Used = 649.12 kWh, Net Energy = -89.86 kWh 

    ♡ I isolated the subsystems and the greenhouse light power is taking up a high percentage of the power, I have it set up to be running w. daylight, but now I'm thinking about having the lights on a 12 hour cycle

    ♡ finished updating the greenhouse lights, at 16 base hours for the greenhouse lights I've manaed to get the Greenhouse energy usage to 260.46 kwh, instead of 325.55kwh

##      08/11/2026
    ♡ I'm going over greenhouse power and waste heat, now that a lot of changes have been made to the greenhouse

    ♡ NASA style and long duration designs run moderate light levels instead of Earth's commercial maximums, so 100–160 W/m² electrical is common for efficient systems that mix sunlight + LEDs

    ♡ more modern LEDs deliver roughly 2.7–3.5 µmol/J, at 0.12 kW/m² (120 W/m²) electrical you can realistically expect about 320–400 µmol/m²/s at the canopy under decent mounting

    ♡ I read about crop needs:
        Spinach, peas, most leafy/herbs:
             150–300 µmol/m²/s (happy around 200–250)
        
        Quinoa, many medium crops:
             300–500
        
        Sweet potato, peanuts (higher light demand):
             400–600+ for strong yields

    ♡ so I'm changing my light targets per m2 to structural zone: 0.26, container zone: 0.23 and the rack zone: 0.19

    ♡ going over the values for greenhouse equipment power, I tried to look at NASA hydroponic set up studies for power draw, and found that in the Biomass Production Chamber(20 m² growing area) the light power used the most power, while air handling and chilling were next and then the nutrient solution pumps used a smaller amount

    ♡ student/NASA challenge greenhouse and MELiSSA-style studies show nutrient delivery / irrigation power as actually pretty low once the system is recirculating properly and efficient
    
    ♡ I'm going to drop the eqipment power draw to ~ 0.05 kW/m² 
