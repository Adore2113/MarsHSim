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
