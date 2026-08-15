# Greenhouse Gases (CO₂ & O₂)
### General Notes:
    ♡ this isn't a greenhouse simulator, so it's intentionally not as complex as it could be
    
    ♡ calculations are performed separately for each zone

    ♡ each zone uses averaged plant data instead of simulating individual crops
    
    ♡ driven by light exposure × plant health
    
    ♡ the greenhouse is intended to remain a minor contributor to habitat atmosphere

    ♡ ~ 2% of crew gas needs is a design  target, not a value the greenhouse is forced to produce

    ♡ gas exchange rates will be based on the averaged crop mix in each zone, then compared against crew demand

### ----------------------------------------

## Photosynthesis Model:
    ♡ light period:
        - plants consume CO₂ and produce O₂
        - gas exchange depends on light exposure × plant health

    ♡ dark period:
        - photosynthesis stops
        - plants continue respiration
        - plants consume O₂ and release CO₂ (smaller amounts)

    ♡ calculation:
        - photosynthesis factor:
            light exposure × plant health

        - CO₂ consumed:
            CO₂ rate per m² per sol × effective grow area × sol fraction × photosynthesis factor

        - O₂ produced:
            O₂ rate per m² per sol × effective grow area × sol fraction × photosynthesis factor

### ----------------------------------------

## Gas Exchange Rates:
#### Units & Conversion:
    ♡ gas exchange is stored as an amount of gas instead of pressure change

    ♡ light period:
        - CO₂ consumed: ~832.90 mol/sol
        - O₂ produced: ~857.89 mol/sol

    ♡ dark period:
        - CO₂ released: ~89.43 mol/sol
        - O₂ consumed: ~99.36 mol/sol

    ♡ net over one sol:
        - CO₂ removed: ~743.47 mol/sol
        - O₂ produced: ~758.53 mol/sol

    ♡ zone rates use:
        - mol CO₂/m²/sol
        - mol O₂/m²/sol

    ♡ final atmospheric pressure change is calculated separately using atmospheric volume and temperature

    ♡ conversion:
        µmol/m²/s × 1 mol / 1,000,000 µmol
        × s of active gas exchange
        = mol/m²/sol

### ----------------------------------------

#### Light Period CO₂ Exchange:
    ♡ REMINDER: these rates already account for the 16-hour active light period so don't apply another 16/24 multiplier later

    ♡ structural:
        - average light period CO₂ removal rate: 
            10 µmol CO₂/m²/s

        - converted MarsHSim rate: 
            ~ 0.576 mol CO₂/m²/sol 

        - calculations:
            10 µmol CO₂/m²/s × 57,600 s
            = 576,000 µmol CO₂/m²/sol

            micromoles to moles:
                576,000 ÷ 1,000,000
                = 0.576 mol CO₂/m²/sol

            CO₂ consumed:
                0.576 mol/m²/sol × effective grow area × sol fraction × light exposure × plant health
            
    ♡ container:
        - average light period CO₂ removal rate: 
            12 µmol CO₂/m²/s

        - converted MarsHSim rate: 
            ~ 0.6912 mol CO₂/m²/sol

        - calculations:
            12 µmol CO₂/m²/s × 57,600 s
            = 691,200 µmol CO₂/m²/sol

            micromoles to moles:
                691,200 ÷ 1,000,000
                = 0.6912 mol CO₂/m²/sol

            CO₂ consumed:
                0.6912 mol/m²/sol × effective grow area × sol fraction × light exposure × plant health

    ♡ rack:
        - average light period CO₂ removal rate:  
            10 µmol CO₂/m²/s

        - converted MarsHSim rate: 
            ~ 0.576 mol CO₂/m²/sol

        - calculations:
            10 µmol CO₂/m²/s × 57,600 s
            = 576,000 µmol CO₂/m²/sol

            micromoles to moles:
                576,000 ÷ 1,000,000
                = 0.576 mol CO₂/m²/sol

            CO₂ consumed:
                0.576 mol/m²/sol × effective grow area × sol fraction × light exposure × plant health

    ♡ actual gas exchange still scales with:
        - effective grow area
        - light exposure
        - plant health
        - sol fraction

#### Dark Period CO₂ Exchange: 
    ♡ photosynthesis stops during the dark period
    ♡ modifiers: zone area × plant health × timestep
    ♡ plant respiration continues

    ♡ plants:
        - consume O₂
        - release CO₂
    
    ♡ structural:
        - average dark period CO₂ release rate:
            ~ 3.0 µmol CO₂/m²/s

        - converted MarsHSim rate:
            ~ 0.0864 mol CO₂/m²/sol

        - calculations:
            3.0 µmol CO₂/m²/s × 28,800 s
            = 86,400 µmol CO₂/m²/sol

            micromoles to moles:
                86,400 ÷ 1,000,000
                = 0.0864 mol CO₂/m²/sol

            CO₂ released:
                0.0864 mol/m²/sol × effective grow area × sol fraction × plant health

    ♡ container:
        - average dark period CO₂ release rate:
            ~ 1.5 µmol CO₂/m²/s

        - converted MarsHSim rate:
            ~ 0.0432 mol CO₂/m²/sol

        - calculations:
            1.5 µmol CO₂/m²/s × 28,800 s
            = 43,200 µmol CO₂/m²/sol

            micromoles to moles:
                43,200 ÷ 1,000,000
                = 0.0432 mol CO₂/m²/sol

            CO₂ released:
                0.0432 mol/m²/sol × effective grow area × sol fraction × plant health

    ♡ rack:
        - average dark period CO₂ release rate:
            ~ 2.5 µmol CO₂/m²/s

        - converted MarsHSim rate:
            ~ 0.072 mol CO₂/m²/sol

        - calculations:
            2.5 µmol CO₂/m²/s × 28,800 s
            = 72,000 µmol CO₂/m²/sol

            micromoles to moles:
                72,000 ÷ 1,000,000
                = 0.072 mol CO₂/m²/sol

            CO₂ released:
                0.072 mol/m²/sol × effective grow area × sol fraction × plant health

#### Total CO₂ Exchange:
    ♡ light period CO₂ uptake: ~ 832.90 mol/so
    ♡ dark period CO₂ release: ~ 89.43 mol/sol

    ♡ calculations:
        - light period:
            ♡ structural:
                - baseline CO₂ uptake:
                    0.576 mol/m²/sol × 420 m²
                    = 241.92 mol CO₂/sol

            ♡ container:
                - baseline CO₂ uptake:
                    0.6912 mol/m²/sol × 480 m²
                    = 331.776 mol CO₂/sol
                    ≈ 331.78 mol CO₂/sol

            ♡ rack:
                - baseline CO₂ uptake:
                    0.576 mol/m²/sol × 450 m²
                    = 259.20 mol CO₂/sol

            ♡ total light period CO₂ uptake:
                241.92 + 331.78 + 259.20
                = 832.90 mol CO₂/sol

        - dark period:
            ♡ structural:
                - dark period CO₂ release:
                    0.0864 mol/m²/sol × 420 m²
                    = 36.288 mol CO₂/sol
                    ≈ 36.29 mol CO₂/sol

            ♡ container:
                - dark period CO₂ release:
                    0.0432 mol/m²/sol × 480 m²
                    = 20.736 mol CO₂/sol
                    ≈ 20.74 mol CO₂/sol

            ♡ rack:
                - dark period CO₂ release:
                    0.072 mol/m²/sol × 450 m²
                    = 32.40 mol CO₂/sol

            ♡ total dark period CO₂ release:
                36.29 + 20.74 + 32.40
                = 89.43 mol CO₂/sol
    
        ♡ net CO₂ removal over one sol:
            832.90 mol consumed - 89.43 mol released
            = 743.47 mol CO₂/sol

### ----------------------------------------

#### Light Period O₂ Exchange:
    ♡ preliminary estimates
    ♡ V1 uses a single value for all zones

    ♡ crop differences are already handled by the different CO₂ uptake rates per zone
        
    ♡ PQ = photosynthetic quotient, for every 1 mole of CO₂ removed during photosynthesis, how many moles of O₂ do they release  

    ♡ PQ = 1.03 for all zones
    ♡ PQ = O₂ produced ÷ CO₂ consumed
    ♡ O₂ produced = CO₂ consumed × 1.03 (PQ)

    ♡ structural:
        - CO₂ uptake: 0.576 mol CO₂/m²/sol
        - effective grow area: 420 m²

        - calculations:
            ♡ O₂ production:
                0.576 × 1.03
                = 0.59328 mol O₂/m²/sol

            ♡ full zone baseline O₂ production:
                0.59328 × 420
                = 249.1776 mol O₂/sol
                ≈ 249.18 mol O₂/sol

    ♡ container:
        - CO₂ uptake: 0.6912 mol CO₂/m²/sol
        - effective grow area: 480 m²

        - calculations:
            ♡ O₂ production:
                0.6912 × 1.03
                = 0.711936 mol O₂/m²/sol

            ♡ full zone baseline O₂ production:
                0.711936 × 480
                = 341.72928 mol O₂/sol
                ≈ 341.73 mol O₂/sol

    ♡ rack:
        - CO₂ uptake: 0.576 mol CO₂/m²/sol
        - effective grow area: 450 m²

        - calculations:
            ♡ O₂ production:
                0.576 × 1.03
                = 0.59328 mol O₂/m²/sol

            ♡ full zone baseline O₂ production:
                0.59328 × 450
                = 266.976 mol O₂/sol
                ≈ 266.98 mol O₂/sol            
    
    ♡ total light period O₂ production:
        249.18 + 341.73 + 266.98
        = 857.89 mol O₂/sol


#### Dark Period O₂ Exchange:
    ♡ preliminary estimates
    ♡ V1 uses a single value for all zones

    ♡ crop differences are already handled by the different dark period CO₂ release rates per zone

    ♡ RQ = respiratory quotient, the relationship between CO₂ released and O₂ consumed during respiration

    ♡ RQ = 0.90 for all zones
    ♡ RQ = CO₂ released ÷ O₂ consumed
    ♡ O₂ consumed = CO₂ released ÷ 0.90

    ♡ structural:
        - CO₂ release: 0.0864 mol CO₂/m²/sol
        - effective grow area: 420 m²

        - calculations:
            ♡ O₂ consumption:
                0.0864 ÷ 0.90
                = 0.096 mol O₂/m²/sol

            ♡ full zone baseline O₂ consumption:
                0.096 × 420
                = 40.32 mol O₂/sol

    ♡ container:
        - CO₂ release: 0.0432 mol CO₂/m²/sol
        - effective grow area: 480 m²

        - calculations:
            ♡ O₂ consumption:
                0.0432 ÷ 0.90
                = 0.048 mol O₂/m²/sol

            ♡ full zone baseline O₂ consumption:
                0.048 × 480
                = 23.04 mol O₂/sol


    ♡ rack:
        - CO₂ release: 0.072 mol CO₂/m²/sol
        - effective grow area: 450 m²

        - calculations:
            ♡ O₂ consumption:
                0.072 ÷ 0.90
                = 0.080 mol O₂/m²/sol

            ♡ full zone baseline O₂ consumption:
                0.080 × 450
                = 36.00 mol O₂/sol


    ♡ total dark period baseline O₂ consumption:
        40.32 + 23.04 + 36.00
        = 99.36 mol O₂/sol


#### Total O₂ Exchange:
    ♡ light period O₂ production: ~ 857.89 mol O₂/sol
    ♡ dark period O₂ consumption: ~ 99.36 mol O₂/sol

    ♡ calculations:
        - light period:
            ♡ structural:
                - baseline O₂ production:
                    0.59328 mol/m²/sol × 420 m²
                    = 249.1776 mol O₂/sol
                    ≈ 249.18 mol O₂/sol

            ♡ container:
                - baseline O₂ production:
                    0.711936 mol/m²/sol × 480 m²
                    = 341.72928 mol O₂/sol
                    ≈ 341.73 mol O₂/sol

            ♡ rack:
                - baseline O₂ production:
                    0.59328 mol/m²/sol × 450 m²
                    = 266.976 mol O₂/sol
                    ≈ 266.98 mol O₂/sol

            ♡ total light period O₂ production:
                249.18 + 341.73 + 266.98
                = 857.89 mol O₂/sol

        - dark period:
            ♡ structural:
                - baseline O₂ consumption:
                    0.096 mol/m²/sol × 420 m²
                    = 40.32 mol O₂/sol

            ♡ container:
                - baseline O₂ consumption:
                    0.048 mol/m²/sol × 480 m²
                    = 23.04 mol O₂/sol

            ♡ rack:
                - baseline O₂ consumption:
                    0.080 mol/m²/sol × 450 m²
                    = 36.00 mol O₂/sol

            ♡ total dark period O₂ consumption:
                40.32 + 23.04 + 36.00
                = 99.36 mol O₂/sol

        ♡ net O₂ production over one sol:
            857.89 mol produced - 99.36 mol consumed
            = 758.53 mol O₂/sol

### ----------------------------------------

## Atmospheric Contribution Target (08/14/2026):
    ♡ preliminary estimates
    ♡ crew count: 30

    ♡ crew O₂ demand:
        - 0.00011 kPa/hour/person
        - 0.0814 kPa/sol

    ♡ Mars sol length (for calculations): 
        ~ 24.66 hours

    ♡ target greenhouse contribution: 
        ~ 2% of crew O₂ and CO₂ needs

    ♡ greenhouse rates are calculated independently

    ♡ after gas exchange is calculated, it's compared to crew metabolic gas exchange

    ♡ ~ 2% is used to check if the greenhouse remains a minor atmospheric contributor isntead of forcing rates to match it

    ♡ calculation:
        - crew O₂ demand:
            0.00011 kPa/hour/person × 30 people × 24.66 hours/sol
            ≈ 0.0814 kPa/sol

        - target greenhouse contribution:
            0.0814 kPa/sol × 0.02
            ≈ 0.00163 kPa/sol

    ♡ this average is only a preliminary target

    ♡ final zone rates still need to preserve differences between the structural, container and rack zones

### ----------------------------------------

## Design Evolution:
    ♡ the original greenhouse gas-exchange values produced ~ 75 times the crew's O₂ requirement

    ♡ decided the greenhouse should be a minor contributor instead of a primary life support system

    ♡ it was deliberately made to contribute 2% of crew gas needs (CO₂ rate chosen so greenhouse = 2% crew demand)

    ♡ origional zone rates:
        - structural zone:
           ♡ rate: 0.022 kPa/m²/sol
           ♡ area: 90 m²
           ♡ calculation:
                0.022 kPa/m²/sol × 90 m² 
                = 1.98 kPa/sol

        - container zone:
            ♡ rate: 0.020 kPa/m²/sol
            ♡ area: 110 m²
            ♡ calculation:
                0.020 kPa/m²/sol × 110 m² 
                = 2.20 kPa/sol

        - rack zone:
            ♡  rate: 0.015 kPa/m²/sol
            ♡  area: 124 m²
            ♡  calculation:
                0.015 kPa/m²/sol × 124 m² 
                = 1.86 kPa/sol

        - total previous greenhouse output: 
             6.04 kPa/sol

    - previous zone rates (for ~ 2% target):
        - structural:
            ♡ rate: 0.00000140 kPa/m²/sol
            ♡ area: 420 m²
            ♡ calculation:
                0.00000140 × 420 ≈ 0.000588 kPa/sol

        - container:
            ♡ rate: 0.00000120 kPa/m²/sol
            ♡ area: 480 m²
            ♡ calculation:
                0.00000120 × 480 ≈ 0.000576 kPa/sol

        - rack:
            ♡ rate: 0.00000100 kPa/m²/sol
            ♡ area: 450 m²
            ♡ calculation:
                0.00000100 × 450 ≈ 0.000450 kPa/sol

        - total: 0.000588 + 0.000576 + 0.000450 
                ≈ 0.00161 kPa/sol

    ♡ considered PQ values: 
        - structural: PQ ≈ 1.10, this zone has more storage root/seed/fat producing crops

        - container: PQ ≈ 1.08, this zone has very mixed crops

        - rack: PQ ≈ 1.05, this zone is dominated more by leafy vegetative crops like spinach and herbs, so I'll keep it simple with ~ 1.1 ratio

### ----------------------------------------

## Future Considerations:
    ♡ calculate biologically based zone O₂ and CO₂ rates, then compare the total against the ~ 2% design target

    ♡ replace preliminary kPa/m²/sol gas rates with biologically based zone average gas exchange rates

    ♡ convert plant gas exchange into atmospheric partial pressure changes using greenhouse/habitat air volume

    ♡ add simplified dark cycle plant respiration

    ♡ determine greenhouse to habitat loop atmospheric exchange

    ♡ implement independently sealed greenhouse zones

### ----------------------------------------

## Design Decisions:
#### Why let the greenhouse contribute to habitat O₂?
    ♡ plants naturally consume CO₂ and produce O₂ while photosynthesizing

    ♡ including a small contribution connects the greenhouse to the habitat atmosphere system

    ♡ the greenhouse is not intended to replace the OGA or other life-support equipment

    ♡ greenhouse gas exchange is intended to provide approximately 2% of crew needs

#### Why not centralize the gas rates?
    ♡ values between structural, container and rack zones are different

    ♡ keeping the rates with each zone makes the differences easier to understand

#### Why ~ 2% of crew O₂ and CO₂ needs?
    ♡ I read that NASA shows ~ 20–25 m² of well lit crops can supply the full O₂ needs of one person

    ♡ my greenhouse priorities are food production and morale first, minor atmosphere contributions, moderate light levels (sunlight + supplemental LEDs) and to be power-concious, so ~ 2% made sense to me

    ♡ 2% is low relative to what the area could theoretically do

#### Why use mol O₂/m²/sol?
    ♡ plant gas exchange represents an amount of O₂ produced or CO₂ consumed, instead of pressure change

    ♡ Nasa research showed rates in µmol/m²/s, but I wanted to convert them because my simulator already handles sol fractions
    
    ♡ the resulting is converted to kPa after using atmospheric volume and temperature

#### Why use 10/12/10 µmol/m²/s for preliminary light period rates?
    ♡ I reasearched NASA's potato and sweet potato  high light experiments as something to go off of because they are studied as space crops and they're included in the greenhouse

    ♡ my simulator uses more moderate lighting and I have mixed crops, different growing rates and crop that aren't all at the same density, so I decided to go for more conservative averages

    ♡ sweet corn can reach ~ 28–34 µmol/m²/s under ideal controlled conditions, while passionfruit commonly falls around ~ 10–30 µmol/m²/s, so 12 µmol/m²/s was chosen as a conservative mixed zone average

    ♡ hydroponic spinach can photosynthesize at much more than 10 µmol CO₂/m²/s under ideal controlled lighting, so 10 µmol/m²/s was chosen as a conservative rack zone average rather than assuming every rack is mature and perfectly lit
    
#### Why use photosynthetic quotient (PQ)?
    ♡ PQ = the relationship between O₂ produced and CO₂ consumed during photosynthesis

    ♡ real plant gas exchange is not always exactly 1 mol O₂ produced for every 1 mol CO₂ consumed, and I have a lot of different crops to consider in each zone

    ♡ it made sense to use a simplified zone average PQ instead of modeling the metabolism of individual crops

#### Why one PQ value for all zones for v1?
    ♡ it matches my overall rule: zone averages, not individual crop physiology

    ♡ the zones are already biologically different b/c of the day time CO₂ rates being 10 / 12 / 10 µmol CO₂/m²/s

    ♡ using the values mentioned in future considerations/dev log notes was more speculative and I don't love that

    ♡ one shared PQ is used for V1 because plant PQ is generally close to 1.0 and varies with metabolism/nutrient conditions more than the current zone crop averages can reliably represent

### ----------------------------------------

### Dev Log Notes:
###### 05/18/2026
    ♡ I want the greenhouse capable of raising the O₂ in the habitat b/c with my hexagon/hive idea for the structure, everything is close together, without separate buildings so it just makes sense to me that it would be a factor 

###### 06/19/2026
    ♡ I noticed my greenhouse is currently producing 75× more O₂ than my crew of 30 needs and this is absolutely not right, it doesn't make any sense so I need to fix this

    ♡ calculation for zone info:
        structural: 0.022 kPa/m²/sol × 90 m²  = 1.98 kPa/sol
        container:  0.020 kPa/m²/sol × 110 m² = 2.20 kPa/sol
        rack:       0.015 kPa/m²/sol × 124 m² = 1.86 kPa/sol
        total ≈ 6.04 kPa/sol

    ♡ calculation for crew O₂ demand:
    0.00011 kPa/hr × 30 crew × ~ 24.66 hr/sol ≈ 0.081 kPa/sol

    ♡ greenhouse should actually produce only 2% of the crew O₂ and CO₂ needs

###### 08/12/2026
    ♡ updated a few values and calculations in gases.md, but I need to come back to this file after I finalize the layout to get the true calculations


###### 08/14/2026
    ♡ removing the forced 2% result 

    ♡ implementing the photosynthesis behavior that changes during the 16 hour light and 8 hour dark period,starting with the light period

    ♡ I'm going to use mol/m²/sol for my sim b/c It alread uses sol fractions

    ♡ I'm using NASA's potato and sweet potato information b/c they are studied as space crops and I'm including those in the sim: 45 µmol CO₂/m²/s at peak photosynthesis, with night time respiration around 9 µmol CO₂/m²/s in those high light experiments

    ♡ my sim is using more moderate lighting, and my zones are mixed crops so I'll look into more conservative averages

    ♡ considering plants being at different growing phases and not all of them being so dense

    ♡ structual: for every m² of structural growing area, while photosynthesis is active, the zone average plants remove ~ 10 µmol/m²/s in this simplified model below the ~ 45 µmol/m²/s

    ♡ container: 
        - ~ 12 µmol/m²/s for V1 zone average
        
        - sweet corn can get to ~  28–34 µmol/m²/s under ideal controlled conditions, while passionfruit seems to commonly fall around 10–30 µmol/m²/s, also consindering different growth stages, again

    ♡ rack: 
        - ~ 10 µmol CO₂/m²/s for V1 zone average
        
        - hydroponic spinach studies say that photosynthetic rates can be much higher than 10 µmol CO₂/m²/s under ideal controlled lighting, using 10 is a conservative mixed zone average instead of than every rack is a mature and perfectly lit

###### 08/15/2026
♡ I've decided to zone averages again for each zone's light period CO2 uptake rate as the dark period's CO2 realease rate, b/c NASA controlled enviornments show that the exact fraction can be very different depending on crop and environment, but b/c of the fractions being so different this will be a pretty rough average

    ♡ structural zone will have the hgihest night time respiration average for my project at ~ 3.0 µmol CO₂/m²/s

    ♡ ~ 1.5 µmol CO₂/m²/s for container b/c the sunflower respiration speficialy seems to be measured as pretty low, especially compared to the crops in the structural and rack zone

    ♡ ~ 2.5 µmol CO₂/m²/s for the rack zone, b/c spinach specifically is measured at ~ 5 µmol CO₂/m²/s so I decided to use that as a half  the mixed zone average, just as something to go off of

    ♡ I had considered using the 1:1 simplified photosynthesis equation, but that doesn't seem realistic and NASA life support work treats CO₂/O₂ ratios as different

    ♡ PQ = photosynthetic quotient
    ♡ RQ = respiratory quotient

    ♡ I read that PQ depends on species, what kind of nitrogen the plants are taking in, what biomass they are building, and how nutritent conditions can even have an impact.. my simulator isn't going this far in depth for v1
    
    ♡ going with PQ = 1.03 for all zones, seems safter b/c the other rates I considered are more speculative and look at more indvidual crops instead of sticking with zone averages

    ♡ I read that RQ depends on what the plants are respiring, first they respire glucose/carbs, then fats, and then sometimes proteins

    ♡ carb respiration is around 1.0, whilemore lipid/proteins can lower it, so I'm going with 0.90 as a simplified value for all zones, it seems like a conservative mixed average
    
    ♡ pressure change: ΔP = nRT ÷ V
        n = gas exchanged (mol)
        R = 0.008314 kPa·m³/(mol·K)
        T = atmospheric temperature in Kelvin
        V = connected atmospheric free volume in m³