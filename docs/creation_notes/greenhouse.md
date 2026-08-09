# Greenhouse:
### General Notes:
    ♡ this isn't a greenhouse simulator, so it's intentionally not as complex as it could be

    ♡ running the greenhouse (LEDs, pumps, circulation) consumes power continuously while online, creating the same kind of engineering trade off as the solar field's maintenance draw

 ### ----------------------------------------
 
## Greenhouse Zones Plan (19/06/2026):
#### Greenhouse:
    ♡ pressurized volume: 1,007 m³
    ♡ floor area: 265 m²
    ♡ height: 3.8 m
    ♡ calculation:
        - volume:
            265 m² × 3.8 m
            = 1,007 m³

#### Grow area:
    ♡ 324 m² total effective grow area
    ♡ 3 zones
    ♡ calculation:
        - structural: 
            90 m²
        - container: 
            110 m²
        - rack: 
            124 m²
        - total:
            90 + 110 + 124
            = 324 m²

#### Zones:
    ♡ total model grow area: 324 m²
    ♡ separated by container type
    ♡ structural zone: 
        - 90 m²
        - 0.022 kPa/m²/sol O2/CO2 rate

    ♡ container zone: 
        - 110 m²
        - 0.020 kPa/m²/sol O2/CO2 rate

    ♡ rack zone: 
        - 124 m²
        - 0.015 kPa/m²/sol O2/CO2 rate

    ♡ calculation:
        - total grow area:
            90 m² + 110 m² + 124 m²
            = 324 m²

        - O2 produced/sol (same as CO2 consumed/m²):
            ♡ structural: 
                0.022 kPa/m²/sol × 90 m²
                = 1.98 kPa/sol

            ♡ container: 
                0.020 kPa/m²/sol × 110 m²
                = 2.20 kPa/sol

            ♡ rack: 
                0.015 kPa/m²/sol × 124 m²
                = 1.86 kPa/sol

            ♡ total ≈ 6.04 kPa/sol

#### Zone Subdivision (racks/containers per zone):
    ♡ I don't have racks per zone or containers per rack counts recorded yet

    ♡ moved to Future Considerations for now

### ----------------------------------------

## Growth Model:
#### Growth:
    ♡ default starting health: 0.98
    ♡ default starting light exposure: 0.65
    ♡ default growth multiplier: 1.0

    ♡ growth is tracked by zone instead of by individual crop

    ♡ calculation:
        - growth increase:
            base growth rate × growth multiplier × light exposure × health × sol fraction

#### Harvest:
    ♡ triggers when growth progress reaches or exceeds: 1.0

    ♡ growth progress resets to 0.0 after harvest
    
    ♡ food is produced only when a harvest occurs

    ♡ calculation:
        - food produced:
            ♡ food yield per m² × growing area × yield multiplier

        - harvest condition:
            ♡ growth progress ≥ 1.0

### ----------------------------------------


        


### ----------------------------------------

## Power Usage:        
#### Plant Light Power:
    ♡ LED power density: 0.12 kW/m²

    ♡ plant lighting power depends on effective grow area and LED level

    ♡ natural sunlight and partial LED support reduce actual energy use

    ♡ measured average, 16-hour schedule (current):
        ~ 260.5 kWh/sol

    ♡ measured average, before the 16-hour schedule: 
        ~ 325.6 kWh/sol
    
    ♡ calculation:
        - full LED power: 
            324 m² × 0.12 kW/m² = 38.88 kW

        - maximum energy over the full 16 hour light period: 
            38.88 kW × 16 hours = 622.08 kWh/sol


### ----------------------------------------

## Heat Generated:
#### Plant Light Heat:
    ♡ LED waste heat: ~ 26.4 kW
    ♡ LED heat ratio: 0.68
    ♡ structural heat: ~ 4.9 kW

    ♡ calculation:
        - LED heat output: 
            plant LED power × 0.68

        - maximum heat output at 38.88 kW:
            38.88 kW × 0.68 = 26.44 kW

        - maximum heat energy over 16 hours:
            26.44 kW × 16 hours ≈ 423.01 kWh/sol

        - LED heat: 
            38.88 kW × 0.68 (waste heat ratio) ≈ 26.4 kW

        -structural heat:
            0.015 kW/m² × 324 m² ≈ 4.9 kW

#### Structural Heat:
    ♡ greenhouse structural heat: 0.015 kW/m²
    ♡ calculation:
        - structural heat:
            ♡ greenhouse structural heat per m² × greenhouse floor area

        - using the 265 m² greenhouse floor area:
            ♡ 0.015 kW/m² × 265 m²
            = 3.975 kW
            ≈ 3.98 kW

        - structural heat energy over 24 hours:
            3.975 kW × 24 hours
            = 95.4 kWh/sol


### ----------------------------------------

## Greenhouse Water Model:
#### Water Use:
    ♡ water requirements are calculated by zone

    ♡ structural:
        - multiplier: 1.15
        - base water: 3.4 kg/m²/sol
        - growing area: 90 m²

    ♡ container:
        - multiplier: 1.00
        - base water: 2.6 kg/m²/sol
        - growing area: 110 m²

    ♡ rack:
        - multiplier: 0.90
        - base water: 1.95 kg/m²/sol
        - growing area: 124 m²

    ♡ calculation:
        - water needed:
            base water needed per m² × growing area × water multiplier × sol fraction

        - structural:
            3.4 kg/m²/sol × 90 m² × 1.15
            = 351.90 kg/sol

        - container:
            2.6 kg/m²/sol × 110 m² × 1.00
            = 286.00 kg/sol

        - rack:
            1.95 kg/m²/sol × 124 m² × 0.90
            = 217.62 kg/sol

        - total:
            351.90 + 286.00 + 217.62
            = 855.52 kg/sol

### ----------------------------------------

#### Water Recirculation:
    ♡ default water recirculation efficiency: 93%
    ♡ each zone has its own recirculation efficiency

    ♡ structural:
        - recirculation efficiency: 82%
        - water recirculated: 288.56 kg/sol
        - water taken up by plants: 63.34 kg/sol

    ♡ container:
        - recirculation efficiency: 88%
        - water recirculated: 251.68 kg/sol
        - water taken up by plants: 34.32 kg/sol

    ♡ rack:
        - recirculation efficiency: 94%
        - water recirculated: 204.56 kg/sol
        - water taken up by plants: 13.06 kg/sol

    ♡ total:
        - water recirculated: 744.80 kg/sol
        - water taken up by plants: 110.72 kg/sol

    ♡ calculation:
        - water recirculated:
            water needed × recirculation efficiency

        - water taken up by plants:
            water needed × (1.0 - recirculation efficiency)

        - structural recirculated:
            351.90 kg/sol × 0.82
            = 288.56 kg/sol

        - structural plant uptake:
            351.90 kg/sol × 0.18
            = 63.34 kg/sol

        - container recirculated:
            286.00 kg/sol × 0.88
            = 251.68 kg/sol

        - container plant uptake:
            286.00 kg/sol × 0.12
            = 34.32 kg/sol

        - rack recirculated:
            217.62 kg/sol × 0.94
            = 204.56 kg/sol

        - rack plant uptake:
            217.62 kg/sol × 0.06
            = 13.06 kg/sol

        - total water recirculated:
            288.56 + 251.68 + 204.56
            = 744.80 kg/sol

        - total plant water uptake:
            63.34 + 34.32 + 13.06
            = 110.72 kg/sol

        - water balance:
            744.80 + 110.72
            = 855.52 kg/sol

### ----------------------------------------

#### Runoff:
    ♡ runoff represents nutrient solution draining from the plant containers

    ♡ this water is collected and returned to the greenhouse nutrient reservoirs

    ♡ runoff is included in the greenhouse recirculation values above

    ♡ to do:
        - determine whether runoff should eventually be modeled separately

### ----------------------------------------

#### Transpiration and Plant Mass:
    ♡ transpiration ratio: 85% of plant water uptake
    ♡ plant mass ratio: 15% of plant water uptake

    ♡ calculation:
        - transpiration:
            plant water uptake × 0.85

        - plant mass water:
            plant water uptake × 0.15

### ----------------------------------------

## CO₂ & O₂ Model:
#### Photosynthesis:
    ♡ greenhouse gas exchange depends on plant health and light exposure

    ♡ calculations are performed separately for each greenhouse zone

    ♡ calculation:
        - photosynthesis factor:
            light exposure × plant health

        - CO₂ consumed:
            CO₂ consumption rate per m² per sol × growing area × sol fraction × photosynthesis factor

        - O₂ produced:
            O₂ production rate per m² per sol × growing area × sol fraction × photosynthesis factor

#### Gas Exchange Target:
    ♡ crew count: 30

    ♡ current crew O₂ demand: 
        0.00011 kPa/hour/person

    ♡ Mars sol length: 
        ~ 24.66 hours

    ♡ target greenhouse contribution:
        ~ 2% of crew O₂ and CO₂ needs

    ♡ calculation:
        - crew O₂ demand:
            0.00011 kPa/hour/person × 30 people × 24.66 hours/sol
            ≈ 0.0814 kPa/sol

        - target greenhouse contribution:
            0.0814 kPa/sol × 0.02
            ≈ 0.00163 kPa/sol

        - approximate average target rate across 324 m²:
            0.00163 kPa/sol ÷ 324 m²
            ≈ 0.00000503 kPa/m²/sol

    ♡ this average is only a preliminary target

    ♡ final zone rates still need to preserve differences between the structural, container and rack zones

### ----------------------------------------


----------------------------------------

## Growing Medium:
#### Lightweight Clay Balls:
    ♡ considering lightweight clay balls similar to LECA instead of soil

    ♡ can pack tightly and securely during Starship transport

    ♡ intended to degrade slowly over years on Mars

    ♡ to do:
        - calculate mass required
        - calculate transport volume
        - estimate degradation rate
        - determine replacement schedule
        - determine whether the material can be cleaned and reused
----------------------------------------

## Crop Plan:


#### Crop Considerations:
    ♡ sweet potato:
        - high in calories
        - edible leaves
        - can grow vertically
        - germination: 1–14 days
        - vegetative growth: 2–8 weeks
        - flowering: 6–12 weeks
        - harvest: ~ 3 months

    ♡ quinoa:
        - protein
        - carbohydrates
        - resilient
        - low preparation after harvest
        - germination: 2–3 weeks
        - vegetative growth: 2–4 weeks
        - flowering: 4–6 weeks
        - harvest: 3–4 months

    ♡ corn:
        - multipurpose
        - starchy
        - germination: 5–10 days
        - vegetative growth: 10–50 days
        - flowering: 50–70 days
        - harvest: 90–140 days

    ♡ dwarf banana trees:
        - familiar morale fruit
        - germination: 2–3 weeks
        - vegetative growth: 3–6 months
        - flowering: 6–12 months
        - fruit development: 11–14 months

    ♡ peanuts:
        - high in fat, protein and calories
        - germination: 5–10 days
        - vegetative growth: 10–40 days
        - flowering: 40–50 days
        - harvest: 120–160 days

    ♡ sunflowers:
        - edible seeds
        - morale value
        - germination: 7–10 days
        - vegetative growth: 20–40 days
        - flowering: 30–50 days
        - harvest: 70–120 days

    ♡ peas:
        - fast growth
        - germination: 7–14 days
        - vegetative growth: 12–42 days
        - flowering: 28–45 days
        - harvest: 60–70 days

    ♡ spinach:
        - germination: 7–14 days
        - vegetative growth: 30–45 days
        - flowering: 42–56 days
        - harvest: 37–60 days

    ♡ dwarf passionfruit:
        - vitamins
        - morale value
        - pleasant smell
        - germination: 7–28 days
        - vegetative growth: 60–182 days
        - flowering: 182–547 days
        - harvest: 1–1.5 years

    ♡ removed:
        - plantain leaf
        - removed because the expected 1–2 year harvest period is too long for the current simulation plan

    ♡ lentils:
        - not currently planned as a fresh greenhouse crop
        - could be stored as part of the habitat's food reserves
        - freeze-dried protein and emergency rations can provide additional backup food

    ♡ herbs:
        - small amounts only
        - dual-purpose crops preferred
        - specific herbs still need research

    ♡ fleshy fruits:
        - high water content
        - examples include peaches and apples

    ♡ dry fruits:
        - may be better for seed storage and reproduction
        - fruit protects the seeds

### ----------------------------------------

## Future Considerations:
    ♡ finalize effective grow area for each zone

    ♡ connect vertical grow area to the physical greenhouse layout

    ♡ recalculate O₂ and CO₂ production rates so the greenhouse contributes ~ 2% of crew demand instead of the previous 75× value

    ♡ decide between a 12, 14 or 16-hour plant lighting schedule
        - current schedule: 16 hours

    ♡ calculate greenhouse habitat lighting area separately

    ♡ model the full crew-waste-to-greenhouse nutrient and water loop

    ♡ determine how nutrient imbalance will be represented

    ♡ determine how plant pathogens and disease will be represented

    ♡ calculate lightweight clay-ball degradation and replacement

    ♡ decide which herbs would provide more than one use

    ♡ factor in:
        - plant disease
        - labour hours
        - morale value
        - spoilage rate
        - crop water use
        - nutrient balance

    ♡ reflect the helix/hive layout in the simulation after the habitat layout is finalized

    ♡ research species that build efficient structures and systems

    ♡ confirm whether the 0.10 kW/m² greenhouse equipment load includes plant lighting

    ## Water/Waste Recycling Loop:
    ## Water/Waste Recycling Loop:
    ♡ concept only, not fully modeled in V1

    ♡ planned crew water loop:
        - crew waste
        - water treatment
        - UPA/WPA
        - potable water
        - greenhouse nutrient solution
        - plants
        - greenhouse humidity
        - CHX water capture
        - water system

    ♡ pros:
        - massive water recycling
        - reduces replacement water requirements

    ♡ challenges:
        - nutrient imbalance
        - pathogens
        - plant disease
        - treatment requirements

    ♡ currently only the greenhouse water recirculation is modeled

    ♡ the full crew waste to greenhouse nutrient solution loop has not been implemented


#### Greenhouse Equipment Power:
    ♡ preliminary base equipment power: 0.10 kW/m²

    ♡ intended to represent equipment such as:
        - pumps
        - circulation
        - greenhouse support equipment

    ♡ this load is not currently included in the simulation's total power use

    ♡ calculation:
        - using the 265 m² greenhouse floor area:
            0.10 kW/m² × 265 m²
            = 26.5 kW

        - maximum energy over one Mars sol:
            26.5 kW × 24.66 hours
            ≈ 653.5 kWh/sol

    ♡ to do:
        - decide whether 0.10 kW/m² is realistic
        - confirm exactly which equipment this value includes
        - avoid including LED power because greenhouse LED power is already calculated separately
        - add greenhouse equipment power and energy to greenhouse_outputs
        - add greenhouse equipment power and energy to power.py
        - separate pumps, circulation and other equipment loads later

### ----------------------------------------

### ----------------------------------------

## Design Evolution:
#### Early Greenhouse Model:
    ♡ considered simulating each individual crop type with its own growing conditions

    ♡ this would have made the greenhouse much more detailed than the other MarsHSim systems

    ♡ considered using one overall greenhouse setting

    ♡ one overall setting seemed too simple

    ♡ decided to use 3 separate zones based on container type

    ♡ each zone now uses averages from the plants grown within it
    

#### Early Gas Exchange Model:
    ♡ the original greenhouse gas-exchange values produced ~ 75 times the crew's O₂ requirement

    ♡ decided the greenhouse should be a minor contributor instead of a primary life-support system

    ♡ current target is ~ 2% of crew demand

#### Previous Zone Rates:
    ♡ structural zone:
        - rate: 0.022 kPa/m²/sol
        - area: 90 m²
        - calculation:
            0.022 kPa/m²/sol × 90 m²
            = 1.98 kPa/sol

    ♡ container zone:
        - rate: 0.020 kPa/m²/sol
        - area: 110 m²
        - calculation:
            0.020 kPa/m²/sol × 110 m²
            = 2.20 kPa/sol

    ♡ rack zone:
        - rate: 0.015 kPa/m²/sol
        - area: 124 m²
        - calculation:
            0.015 kPa/m²/sol × 124 m²
            = 1.86 kPa/sol

    ♡ total previous greenhouse output:
        - 1.98 + 2.20 + 1.86
        = 6.04 kPa/sol


### ----------------------------------------

## Design Decision:
#### Why hydroponics?
    ♡ uses less water than traditional soil-based growing when water is recirculated

    ♡ allows water and nutrients to be collected, treated and reused

    ♡ makes vertical racks and hanging containers easier to incorporate

    ♡ avoids transporting and managing large amounts of soil

    ♡ works with the planned closed greenhouse water loop


#### Why not centralize greenhouse constants?
    ♡ values differ between the structural, container and rack zones

    ♡ keeping relevant values with each zone makes the differences easier to understand

#### Why let the greenhouse contribute to habitat O₂?
    ♡ plants naturally consume CO₂ and produce O₂ while photosynthesizing

    ♡ including a small contribution connects the greenhouse to the habitat atmosphere system

    ♡ the greenhouse is not intended to replace the OGA or other life-support equipment

    ♡ greenhouse gas exchange is intended to provide approximately 2% of crew needs



#### Why use the 40/45/15 nutrition targets?


#### Why avoid heavily processed crops?
    ♡ reduces the equipment and labour required after harvest

    ♡ simpler to represent in the simulation

    ♡ more practical for early habitat operations

### ----------------------------------------
