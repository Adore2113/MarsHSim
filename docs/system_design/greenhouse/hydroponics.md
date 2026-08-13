# Greenhouse Hydroponics
### General Notes:
    ♡ targets and calculations are handled by zone averages instead of individual crop requirements

    ♡ targets were chosen after considering the plants grown in each zone and what they require, I tried to use the averages or meet in the middle

    ♡ the greenhouse uses recirculating hydroponics

    ♡ the full crew waste into nutrient solution loop is planned but not implemented yet
### ----------------------------------------

## Hydroponic Plan (08/12/2026 update):
#### Zone Methods:
    ♡ each zone has it's own reservoir and pumps

    ♡ structural:
        - intermittent drip-fed LECA (lightweight expanded clay agrregate; lightweight clay balls) beds in a shared zone reservoir

        - reservoir pumps solution through a manifold to drop lines, the solution percolates through the LECA/rootzone, collects, drains and returns back into the reservoir
        
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
        
        - the same system as structure except the manifold sending nutrients to differen't containers, with their own drip emitters and drainage connections before returning

        - loop:
            1. reservoir
            2. pump
            3. drip irrigation
            4. individual containers
            5. return/loop
    
    ♡ rack:
        - NFT (Nutrient Film Technique) where the plants get a constant flowing nutrient solution

         - reservoir pumps nutrient solution to the highest end of the NFT channels, the solution flows as a shallow film through the rootzone, and carries it to the lower zone and returns back into the plumbing and then the reservoir

        - loop:
            1. reservoir
            2. pump
            3. NFT channels
            4. return/loop

#### Nutrient Solution Management:
    ♡ one target range per zone

    ♡ the following information is not simulated in v1 :

    ♡ pH target is crucial for health and plant growth

    ♡ EC (Electrical Conductivity) is measures in mS/cm, letting you know how much the concentration of the solution has changed

    ♡ DO (Dissolved Oxygen)how much oxygen is dissolved in the solution for the roots to use
    
    ♡ structural:
        - pH target range: 5.5-6.2 (~ 5.8)
        - EC target range: 1.8-2.4 mS/cm (~ 2.1)
        - solution temp: 22-24°C (~ 23°C)
        - DO target range: ≥ 6 mg/L

    ♡  container:
        - pH target range: 5.7-6.3 (~ 6.0)
        - EC target range: 1.7-2.3 mS/cm (~ 2.0)
        - solution temp: 22-24°C (~ 23°C)
        - DO target range: ≥ 6 mg/L

    ♡ rack:
        - pH target range: 5.8-6.3 (~ 6.0)
        - EC target range: 1.5-2.1 mS/cm (~ 1.8)
        - solution temp: 21-23°C (~ 22°C)
        - DO target range: ≥ 5.5-6 mg/L

### ----------------------------------------

## Reservoirs:
#### Reservoir Sizing:
    ♡ LECA beds retain a lot of moisture in the roots, dutch bucket style containers retain some, and NFT channels don't hold very much so it has the largest reservoir allowance per m²

    ♡ reservoir size is based on effective grow area and hydroponic method

    ♡ reservoirs remain partially unfilled during normal operation to avoid overflow

    ♡ reservoirs are opaque/covered to reduce algae growth

    ♡ preliminary reservoir capacities:
        - the extra space is so the tanks aren't filled at the top during operation

        - structural: ~ 7,000 L
        - container: ~ 9,500 L
        - rack: ~ 10,000 L
    
    ♡ calculation:
        - structural:
            15 L/m² × 420 m²
            = 6,300 L working volume

        - container:
            18 L/m² × 480 m²
            = 8,640 L working volume

        - rack:
            20 L/m² × 450 m²
            = 9,000 L working volume
        
        - total:
            6,300 L + 8,640 L + 9,000 L
            = 23,940 L

#### Reservoir Levels:
    ♡ normal operating level: ~ 85%
    ♡ low: < 50%
    ♡ critical: < 25%

    ♡ 70% triggers make-up water and refills to normal operating levels

    ♡ structural:
        - tank capacity: 7,000 L
        - normal: ~ 5,950 L
        - low: < 3,500 L
        - critical: < 1,750 L
        - auto refill at: 4,900 L

    ♡ container:
        - tank capacity: 9,500 L
        - normal: ~ 8,075 L
        - low: < 4,750 L
        - critical: < 2,375 L
        - auto refill at: 6,650 L

    ♡ rack
        - tank capacity: 10,000 L
        - normal: ~ 8,500 L
        - low: < 5,000 L
        - critical: < 2,500 L
        - auto refill at: 7,000 L

    ♡ calculation:
        - normal:
            ♡ structural:
                reg: 7,000 × 0.85 = 5,950 L
                low: 7,000 L × 0.50 = 3,500 L
                crit: 7,000 L × 0.25 = 1,750 L
                refill: 7,000 L × 0.70 = 4,900 L

            ♡ container:
                reg: 9,500 × 0.85 = 8,075 L
                low: 9,500 L × 0.50 = 4,750 L
                crit: 9,500 L × 0.25 = 2,375 L
                refill: 9,500 L × 0.70 = 6,650 L

            ♡ rack:
                reg: 10,000 × 0.85 = 8,500 L
                low: 10,000 L × 0.50 = 5,000 L
                crit: 10,000 L × 0.25 = 2,500 L
                refill: 10,000 L × 0.70 = 7,000 L

### ----------------------------------------

## Make-up Water System:
    ♡ all three nutrient reservoirs get supplied from a shared clean water set up

    ♡ loop:
        1. habitat potable/treated water
        2. greenhouse make-up water tank
        3. zone valve
        4. nutrient reservoir

    ♡ the greenhouse only uses this top up system if the reservoirs avtual reach 70%, so it will happen gradually and not constantly

    ♡ potable storage loses only the actual greenhouse make-up water

    ♡ calculation:
        target reservoir level − current reservoir level = make-up water needed

### ----------------------------------------

## Design Evolution:
    ♡ I only started with three zones with a shared effective growth rate without going into detail

### ----------------------------------------

## Future Considerations:
## Growing Medium:
    ♡ lightweight clay balls (LECA-style) todo:
        - calculate mass required
        - calculate transport volume
        - estimate degradation rate
        - decide replacement schedule

    ♡ plant health could be considered more in depth in response to the nutrient solution:
        
        - normal pH + normal EC + normal temp + normal DO:
            ♡ health remains ~ 0.98
            ♡ normal growth
        
        - EC too high:
            ♡ health gradually decreases
            ♡ growth slows
            ♡ salt/osmotic stress
            ♡ health penalty

        - EC too low:
            ♡ nutrient limitation
            ♡ health penalty

        - temp out of range:
            ♡ nutrient limitation
            ♡ health penalty
            ♡ gradual stronger root zone health penalties

        - low DO:
            ♡ slower growth
            ♡ health penalty

        - pump failure:
            ♡ NFT flow stops  
            ♡ DO/root water conditions deteriorate
            ♡ rack health falls
            ♡ growth falls
    
### ----------------------------------------

## Design Decisions:
#### Why lightweight clay balls (LECA style) instead of soil?
    ♡ packs tightly and securely for Starship transport

    ♡ it works well with hydroponics and it can be cleaned and reused

    ♡ I learned about these years ago from seeing the hydroponic set up that my friend Joe had created, including clay balls, fish tanks, hanging planters, structural planter area and the whole set up.. the plants were thriving and it looked incredible

#### What is a dutch bucket style system?
    ♡ it's a recirulating drip systems where each plant or small group gets its own bucket, all connected, sharing plumbing

#### Why these chosen values for pH targets?
    ♡ the ranges overlap intentionally, providing a managable operating range to match a mixture of crops in that specific zone

    ♡ although I read that most hydroponic systems have a pH range of 5.5 and 6.5, I didn't like using those numbers as universal targets, especially since I have the different zones

    ♡ for the racks specifically, Virginia Tech says that most NFT plants perform well between 5.5-6.2, after doing a few trials with spinach, so I decided to go with 6.0

#### Why different EC targets?
    ♡ the bigger/longer cycle crops should have a stronger nutrient solution

    ♡ the rack system can have lower concentrations b/c of the smaller, leafier plants there

    ♡ this is a simplification for my simulator, instead of going into detail about specific  plant nutrients like potassium or magnesium

#### Why is the range for DO lower for the rack zone?
    ♡ b/c of using NFT, the rack zone naturally gets good oxygen exposure from the thin moving film

    ♡ the LECA zones rely more on drainage, air gaps, and reservoir aeration


#### Why not simulate  pH, EC nutrients, solution temp and dissolved oxygen for V1?
    ♡ all things that really would only impact plant health and growth rate

    ♡ instead of modeling each factor individually, the simulator can use them as inputs to overall zone/root zone health, which affects growth

#### Why refill at 70%?
    ♡ to ideally not have to worry about the reservoirs reaching 50%

    ♡ in emergencies this gives the reservoirs a bit longer before seriously lacking, giving them a little buffer for a chance at survival

### ----------------------------------------

### Dev Log Notes:
###### 05/08/2026
        ♡ going w. a hydroponic set up, I updated v1_scope to include all my notes about a greenhouse 

###### 05/13/2026
    ♡ adding in hydroponics to the greenhouse list and starting from greenhouse lighting to make the greenhouse file be how I want it to be

    ♡ I didn't want the multipliers in the constants like some other files, b/c they are different for each zone 

    ♡ I connected the new greenhouse variables and logic to the other files

###### 08/12/2026
    ♡ I'm looking into hydroponic set ups and how they work today, I'm not going to go too far into this, again b/c I don't want this to become a main focus, it's not a greenhouse simulator

    ♡ I'm looking into Nutrient Film Technique (NFT) where the plants need a constant flowing nutrient solution, and it seems like this is better for more shallow plans, so it would make sense that the rack system has these


    ♡ reading about recirulating drip systems using dutch bucket set ups, meaning each plant or small group gets its own bucket, all connected sharing plumbing which is exactly what I had planned so this is perfect

    ♡ I'm choosing targets to be averaged per zone

    ♡ I'm trying to decide how in depth to make this, I was considering pH, EC nutrients, solution temp and dissolved oxygen, but these are all things that really would only impact plant health and growth rate, so I'll just make note of them for now, for potential future reference

    ♡ I put a lot of notes right into the hydroponic.md file instead of here

    ♡ EC (Electrical Conductivity) is measures in mS/cm, indicating how concentraed the solution is, not which nutrients are present or if the ratios are perfect, just the overall ionic concentration (so you can tell if the concentration has changed)

    ♡ DO (Dissolved Oxygen)how many oxygen molecules a present in water, essential for the respiration of fish, bacteria, and other aquatic organisms, making it a key indicator of water quality. Low DO stresses roots, slows uptake, and raises the risk of root problems. 

    ♡ the rack zone naturally gets good oxygen exposure from the thin moving film, while the LECA zones rely more on drainage, air gaps, and reservoir aeration

    ♡ I'm not so worried about an upper range for the dissolved oxygen target b/c the most important thing is if it's high enough
    
    ♡ hydroponic research is now stopping for now, b/c I have more than enough for v1

