# Greenhouse Gases (CO₂ & O₂)
### General Notes:
    ♡ this isn't a greenhouse simulator, so it's intentionally not as complex as it could be
    
    ♡ calculations are per zone

    ♡ each zone uses averaged plant data instead of simulating individual crops
    
    ♡ driven by light exposure × plant health
    
    ♡ the greenhouse is only a minor contributor to habitat atmosphere (~ 2% of crew needs)

### ----------------------------------------

## Photosynthesis Model:
    ♡ calculations are performed separately for each zone

    ♡ calculation:
        - photosynthesis factor:
            light exposure × plant health

        - CO₂ consumed:
            CO₂ rate per m² per sol × effective grow area × sol fraction × photosynthesis factor

        - O₂ produced:
            O₂ rate per m² per sol × effective grow area × sol fraction × photosynthesis factor

### ----------------------------------------

## Gas Exchange Target:
##### note: the current rates are placeholders
    ♡ final numbers will be recalculated once the full habitat layout and free volume are locked
    
    ♡ crew count: 30

    ♡ crew O₂ demand:
        - 0.00011 kPa/hour/person
        - 0.0814 kPa/sol

    ♡ Mars sol length (for calculations): 
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

        - approximate average target rate across current total effective grow area (~1,350 m²):
            0.00163 kPa/sol ÷ 1,350 m²
            ≈ 0.00000121 kPa/m²/sol

    ♡ this average is only a preliminary target

    ♡ final zone rates still need to preserve differences between the structural, container and rack zones

### ----------------------------------------

#### Current Zone Rates (updated for ~2% target - 08/11/2026):
    ♡ structural:
        - rate: 0.00000140 kPa/m²/sol
        - area: 420 m²
        - calculation:
            0.00000140 × 420 ≈ 0.000588 kPa/sol

    ♡ container:
        - rate: 0.00000120 kPa/m²/sol
        - area: 480 m²
        - calculation:
            0.00000120 × 480 ≈ 0.000576 kPa/sol

    ♡ rack:
        - rate: 0.00000100 kPa/m²/sol
        - area: 450 m²
        - calculation:
            0.00000100 × 450 ≈ 0.000450 kPa/sol

    ♡ total:
        0.000588 + 0.000576 + 0.000450 ≈ 0.00161 kPa/sol
        (very close to the 0.00163 kPa/sol target)

### ----------------------------------------

## Design Evolution:
#### Early Gas Exchange Model:
    ♡ the original greenhouse gas-exchange values produced ~ 75 times the crew's O₂ requirement

    ♡ decided the greenhouse should be a minor contributor instead of a primary life support system
    
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
        = 6.04 kPa/sol


### ----------------------------------------

## Future Considerations:
    ♡ recalculate the actual zone O₂ and CO₂ rates so the total is ~ 2% of crew demand

    ♡ keep structural highest and rack lowest when setting the final rates

    ♡ figure out pump failure:
            ♡ NFT flow stops  
            ♡ DO/root water conditions deteriorate
            ♡ rack health falls
            ♡ growth falls

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
    
### ----------------------------------------

### Dev Log Notes:
###### 05/18/2026
    ♡ I want the greenhouse capable of raising the o2 in the habitat b/c with my hexagon/hive idea for the structure, everything is close together, without seperate buildings so it just makes sense to me that it would be a factor 

###### 06/19/2026
    ♡ I noticed my greenhouse is currently producting 75x MORE o2 than my crew of 30  mean and this is absolutely not right, it doesn't make any sense so I need to fix this

    ♡ calculation for zone info:
        structural: 0.022 kPa/m²/sol × 90 m²  = 1.98 kPa/sol
        container:  0.020 kPa/m²/sol × 110 m² = 2.20 kPa/sol
        rack:       0.015 kPa/m²/sol × 124 m² = 1.86 kPa/sol
        total ≈ 6.04 kPa/sol

    ♡ calculation for crew o2 demand:
    0.00011 kPa/hr × 30 crew × ~ 24.66 hr/sol ≈ 0.081 kPa/sol

    ♡ the greenhouse actually produce only 2% of the crew o2 and co2 needs

###### 08/12/2026
    ♡ updated a few values and calculations in gases.md, but I need to come back to this file after I finalize the layout to get the true calculations