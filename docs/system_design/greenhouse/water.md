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
