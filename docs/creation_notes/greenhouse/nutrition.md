# Greenhouse 
### General Notes:
    ♡ this isn't a greenhouse simulator, so it's intentionally not as complex as it could be

    ♡ plants are tracked by zone using averages instead of individual crops 

    ♡ some longer cycle crops are included mainly for morale and dietary variety

    ♡ zones seal separately for redundancy and quarantine purposes

    ♡ dual-purpose crops are preferred when possible

    ♡ preference for crops that do not require a lot of processing

    ♡ exact yield numbers and growth rates remain flexible

    ♡ subject to change as the greenhouse design develops

### ----------------------------------------

## Nutrition Plan (08/09/2026):
#### Crew Nutrition Targets:
    ♡ macronutrient targets:
        - carbohydrates: 40%
        - fat: 40%
        - protein: 20%

### ----------------------------------------

#### Zone Crop Roles:
    ♡ structural zone:
        - larger crops
        - longer cycle crops
        - best for:
            bulk calories, fat and protein crops that need more space and time

        - crop considerations: 
            sweet potato, quinoa, peanuts, dwarf banana, dwarf passionfruit

    ♡ container zone:
        - medium crops
        - some vertical growing
        - best for:
            tall plants and mixed plantings

        - crop considerations: 
            corn, sunflowers, mixed medium plants

    ♡ rack zone:
        - smaller crops
        - fast leafy greens
        - hanging plants
        - best for:
            quick harvests and high density growing
        
        - crop considerations: 
            peas, spinach, herbs, smaller vertical crops

    ♡ crops might be in different zones:
        - sweet potato: 
            main in structural, vines and leaves in racks for extra greens
        
        - peas:
            mostly in racks, some in containers if needed
        
        - spinach:
            mainly racks (grows very well this way), a few in containers for variety
        
        - peanuts and sunflowers:
            mostly structural or container for better space and access
        
        - quinoa:
            flexible so between structural and container
        
        - herbs and small vertical plants:
            almost always racks

#### Crop Rotation:
    ♡ rotation notes:
        - the greenhouse stays consistent all the time, so season changes don't really apply
        
        - plant fast crops in small new batches every few weeks  (spinach, peas) 
        
        - medium crops get planted every 1–2 months so harvests overlap (sweet potato, quinoa, peanuts, sunflowers)
        
        - dwarf banana and passionfruit are long term plants that just keep producing once established

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

## Primary Crop List:
    ♡ sweet potato
        - high calories, edible leaves, good   vertical growth
        - harvest window: ~ 3 months

    ♡ quinoa
        - protein + carbohydrates, resilient, low processing after harvest
        - harvest window: 3–4 months

    ♡ peanuts
        - high fat, protein and calories
        - harvest window: 4–5 months

    ♡ peas
        - fast growth, good early harvests
        - harvest window: 2–2.5 months

    ♡ spinach
        - fast leafy green
        - grows amazing hydroponically
        - harvest window: 1–2 months

    ♡ sunflowers
        - edible seeds + morale value
        - harvest window: 2.5–4 months

    ♡ dwarf banana
        - strong morale fruit
        - harvest window: 11–14 months

    ♡ dwarf passionfruit
        - vitamins, pleasant smell, morale value
        - harvest window: 1–1.5 years

### ----------------------------------------

#### Future Considerations:
    ♡ zone subdivisions, I don't have racks per zone or containers per rack counts recorded yet

### ----------------------------------------

## Design Evolution
#### Initial Nutrition Goal:
    ♡ macronutrient targets:
        - carbohydrates: 40%
        - fat: 45%
        - protein: 15%

    ♡ carbohydrates:
        - open to lowering this percentage
        - current value chosen from general research

    ♡ fat:
        - calorie dense
        - helps keep the crew full longer

    ♡ protein:
        - kept lower because high protein may not be ideal in a long term survival environment

#### Removed or De-prioritised:
    ♡ plantain leaf
        - harvest cycle too long (1–2 years) for current simulation needs

    ♡ lentils (as fresh greenhouse crop)
        - better as stored / emergency food

    ♡ highly processed or any very long cycle crop ideas
