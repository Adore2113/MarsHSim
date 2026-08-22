# Sabatier 
### General Notes:
    ♡ converts CO₂ + H₂ into CH₄ + H₂O

    ♡ provides both methane and recovered water

    ♡ water produced is added directly to the potable water balance

    ♡ integrates with OGA: OGA produces hydrogen that can feed the Sabatier (or be vented)

    ♡ SpaceX approach: combines oxygen production (electrolysis / OGA) with methane rocket fuel production with Sabatier + electrolysis

    ♡ only runs when so many reactants are available and the system is on

    ♡ includes limited and venting modes for reactant shortages and methane storage limits

### ----------------------------------------

## Sabatier Plan:
### Reaction Chemistry:
    ♡ min H₂ for reaction: 0.012 kg
    ♡ min CO₂ for reaction: 0.012 kg
    ♡ hysteresis multiplier: 1.5
   
    ♡ methane venting hysteresis: 
        0.60 of storage capacity
   
    ♡ stoichiometric ratio: 
        1 CO₂ : 4 H₂

    ♡ produces: 
        1 CH₄ + 2 H₂O

    ♡ molar masses:
        - H₂ = 2.016 g/mol
        - CO₂ = 44.01 g/mol
        - CH₄ = 16.043 g/mol
        - H₂O = 18.015 g/mol

    ♡ base efficiency: 0.88

    ♡ reactions_available:
        - how many times the stoichiometric reaction can occur, limited by the lesser reactant and efficiency

    ♡ calculation:
        co2_moles:
             available_co2_kg / (44.01 × 0.001)

        h2_moles:
             available_h2_kg  / (2.016 × 0.001)

        reactions_available:
             min(co2_moles, h2_moles / 4) × 0.88

        water_produced_kg:
             reactions_available × 2 × 18.015 × 0.001
        
        ch4_produced_kg :
             reactions_available × 16.043 × 0.001
        
        h2_consumed_kg  :
             reactions_available × 4 × 2.016 × 0.001
        
        co2_consumed_kg :
             reactions_available × 44.01 × 0.001

### Operating Modes:
    ♡ offline:
        - system off
        - no power or reaction

    ♡ idle:
        - both reactants below minimum thresholds
        - very low standby power: ~ 0.1 kW

    ♡ limited_co2 / limited_h2:
        - one reactant is low/below hysteresis
        - runs at reduced power: ~ 75 % of base

    ♡ running:
        - both reactants above hysteresis
        - full power and reaction rate

    ♡ venting:
        - methane storage is near or over capacity
        - excess CH₄ is vented
        - power may increase slightly at × 1.25

    ♡ critical power mode:
        - reduced power: 0.3 kW
        - reduced  heat: ~ 0.2 kW

### Power & Heat:
    ♡ base power: 0.85 kW
    ♡ idle power: ~ 0.1 kW
    ♡ limited mode power: base × 0.75
    ♡ critical power mode: 0.3 kW
    
    ♡ exothermic heat fraction:
        0.65 of electrical pow

    ♡ calculation:
        heat:
            sabatier_power_used_kw × 0.65


### ----------------------------------------

## Design Evolution:
####

### ----------------------------------------

## Future Considerations:
    ♡ 

### ----------------------------------------

## Design Decisions:
#### 

### ----------------------------------------

### Dev Log Notes:
######