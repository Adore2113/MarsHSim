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
        - 1.98 + 2.20 + 1.86
        = 6.04 kPa/sol

