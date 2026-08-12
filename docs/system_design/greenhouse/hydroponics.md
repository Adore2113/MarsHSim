# Greenhouse Hydroponics
### General Notes:
    ♡ targets and calculations are handled by zone averages instead of individual crop requirements

    ♡ targets were chosen after considering the plants grown in each zone and what they require, I tried to use the averages or meet in the middle

    ♡ the greenhouse uses recirculating hydroponics

    ♡ the full crew waste into nutrient solution loop is planned but not implemented yet
### ----------------------------------------

## Hydroponic Plan (08/12/2026 update):
#### Zone Methods:
    ♡ each zone has it's own resevoir and pumps

    ♡ structural:
        - intermittent drip-fed LECA (lightweight expanded clay agrregate; lightweight clay balls) beds in a shared zone reservoir

        - resevoir pumps solution through a manifold to drop lines, the solution percolates through the LECA/rootzone, collects, drains and returns back into the resevoir
        
        - loop:
            1. reservoir
            2. pump
            3. drip irrigation
            4. LECA beds
            5. drainage
            6. return/loop
    
    ♡  container:
        - intermittent drip-fed LECA dutch bucket style set up in a shared zone reservoir
        
        - dutch bucket = a recirulating drip system where each plant or small group gets it's own bucket, all connected with sharing plumbing
        
        - the same system as structure except the manifold sending nutrients to differen't containers, with their own dip emitters and drainage connections before returning

        - loop:
            1. reservoir
            2. pump
            3. drip irrigation
            4. individual containers
            5. return/loop
    
    ♡ rack:
        - NFT (Nutrient Film Technique) where the plats get a constant flowing nutrient solution

         - resevoir pumps nutrient solution to the highest end of the NFT channels, the solution flows as a shallow film through the rootzone, and carries it to the lower zone and returns back into the plumbing and then the resevoir

        - loop:
            1. reservoir
            2. pump
            3. NFT channels
            5. return/loop

#### Nutrient Solution Management:
    ♡ one target range per zone

    ♡ EC (electrical conductivity) is measures in mS/cm, indicating how concentraed the solution is, not which nutrients are present or if the ratios are perfect, just the overall ionic concentration (so you can tell if the concentration has changed)

    ♡ structural:
        - pH target range: 5.5-6.2 (~ 5.8)
        - EC target range: 1.8–2.4 mS/cm (~ 2.1)

    ♡  container:
        - pH target range: 5.7-6.3 (~ 6.0)
        - EC target range: 1.7–2.3 mS/cm (~ 2.0)
        
    ♡ rack:
        - pH target range: 5.8–6.3 (~ 6.0)
        - EC target range: 1.5–2.1 mS/cm (~ 1.8)

### ----------------------------------------

## Design Evolution:
    ♡ I only started with three zones with a shared effective growth rate without going into detail

### ----------------------------------------

## Future Considerations:
    ♡ 

### ----------------------------------------

## Design Decisions:
#### Why lightweight clay balls (LECA style) instead of soil?
    ♡ packs tightly and securely for Starship transport

    ♡ it works well with hydroponics and it can be cleaned and reused

    ♡ I learned about these years ago from seeing the hydroponic set up that my friend Joe had created, including clay balls, fish tanks, hanging planters, structural planter area and the whole set up.. the plants were thriving and it looked incredible

#### What is a dutch bucket style system?
    ♡ it's a recirulating drip systems where each plant or small group gets it's own bucket, all connected, sharing plumbing

#### Why these chosen values for pH targets?
    ♡ the ranges overlap intentionally, providing a managable operating range to match a mixture of crops in that specific zone

    ♡ for the racks specifically, Virginia Tech says that most NFT plants perform well between 5.5-6.2, after doing a few trials with spinach, so I decided to go with 6.0

#### Why different EC targets?
    ♡ the bigger/longer cycle crops should have a stronger nutrient solution

    ♡ the rack system can have lower concentrations b/c of the smaller, leafier plants there

    ♡ this is a simplification for my simulator, instead of going into detail about specific  plant nutrients like potassium or magnesium
