# Greenhouse Water and Hydroponics:
### General Notes:
    ♡ this isn't a greenhouse simulator, so it's intentionally not as complex as it could be

    ♡ water is calculated per zone

    ♡ the greenhouse uses recirculating hydroponics

    ♡ only the greenhouse recirculation is fully modeled right now

    ♡ the full crew waste into nutrient solution loop is planned but not implemented yet

 ### ----------------------------------------

## Greenhouse Water Model:
#### Water Use:
    ♡ water requirements are calculated by zone

    ♡ structural:
        - base water: 3.4 kg/m²/sol
        - multiplier: 1.15
        - effective rate ≈ 3.91 kg/m²/sol

    ♡ container:
        - base water: 2.6 kg/m²/sol
        - multiplier: 1.00
        - effective rate ≈ 2.6 kg/m²/sol

    ♡ rack:
        - base water: 1.95 kg/m²/sol
        - multiplier: 0.90
        - effective rate ≈ 1.76 kg/m²/sol

    ♡ calculation:
        - water needed:
            base water × effective grow area × multiplier × sol fraction

### ----------------------------------------
