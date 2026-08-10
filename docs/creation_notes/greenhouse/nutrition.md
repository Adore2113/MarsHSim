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
            sweet potato, quinoa, peanuts, dwarf banana

    ♡ container zone:
        - medium crops
        - some vertical growing
        - best for:
            tall plants and mixed plantings

        - crop considerations: 
            sweet corn, sunflowers, dwarf passionfruit, mixed medium plants

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
    ♡ sweet potato (priority crop)
        - high calories, edible leaves, good   vertical growth
        - harvest window: ~ 3 months

    ♡ regular potato
        - dietary variety, high calories,
        - harvest window: ~ 3 months
    
    ♡ sweet corn
        - dietary variety, high calories,carbohydrates
        - harvest window: ~ 2-3 months

    ♡ quinoa
        - protein, carbohydrates, resilient, low processing after harvest
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
        - edible seeds, morale value
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

    ♡ determine how nutrient imbalance will be represented

    ♡ decide which herbs would provide more than one use

    ♡ factor in:
        - morale value
        - labour hours

    ♡ research animal/insect species that build efficient structures and systems

### ----------------------------------------

## Design Evolution
#### Initial Nutrition Goal:
    ♡ macronutrient targets:
        - carbohydrates: 
            ♡ 40%
            ♡ open to lowering this percentage
            ♡ current value chosen from general research

        - fat:
            ♡ 45%
            ♡ calorie dense
            ♡ helps keep the crew full longer

        - protein:
            ♡ 15%
            ♡ kept lower because high protein may not be ideal in a long term survival environment
    
#### Early Greenhouse Model:
    ♡ considered simulating each individual crop type with its own growing conditions

    ♡ decided to use 3 separate zones based on container type

    ♡ each zone now uses averages from the plants grown within it

#### Removed or De-prioritised:
    ♡ plantain leaf
        - harvest cycle too long (1–2 years) for current simulation needs

    ♡ lentils (as fresh greenhouse crop)
        - better as stored / emergency food

    ♡ very long cycle crops are deprioritised unless they provide enough morale, dietary, spatial or secondary value to justify taking up greenhouse space

    ♡ origionally considering avocados, I still wish the avacado tree would work, but it doesn't fit my fast, calorie dense and/or multipurpose crops first goal so I couldn't justify such a slow and finicky crop

### ----------------------------------------

## Design Decisions:
#### Why use the 40/40/20 nutrition targets?
    ♡ fat is kept high because it is calorie dense and helps crew feel full longer

    ♡ crops for fat have a smaller yield

    ♡ 20% protein seems like good support for muscle maintenance under partial gravity and physical work
  
    ♡ high protein food production seems not practical long term with a greenhouse

    ♡ I was considering fullness, digestion, blood sugar, mood impact and energy

    ♡ these targets work with my preference for crops that don't require a lot of processing

    ♡ targets sit slightly outside NASA exploration ranges (carb low, fat high)

#### Why use 3 zones by container type?
    ♡ for flexible crop placement
    
    ♡ I considered grouping them by growing conditions, crop type, etc. but decided on this because there are different things to consider for each individual crop as far as needs, growing, timing, and density go

#### Why consider these crops?
    ♡ I wanted to choose crops by nutrition value, yield and usefulness, space efficiency, harvest speed, hydroponic practicality, processing/labour, secondary uses, and morale

    ♡ other reasons are included beside each crop in the 'subsection primary crop list' above 

#### Why sweet corn specifically?
    ♡ it's very sweet, nutritious and familiar for morale

    ♡ it required less processing and could potentially grow better in hydroponics compared to other corn varieties

    ♡ it can be grown in blocks instead of rows so it can have it's own dedicated area

#### Why is sweet potato a priority?
    ♡ both the storage roots and leaves are edible, increasing usable biomass
    
    ♡ vines can use vertical growing space while the roots grow in the structural zone
    
    ♡ requires little processing after harvest
    
    ♡ provides a reliable carbohydrate source while also providing fresh greens
    
    ♡ it meets my crop goals/targets very well


#### Why dwarf banana and passionfruit trees?
    ♡ bananas are a familiar, sweet morale food while still being compact

    ♡ passionfruit has a pleasant smell, it's high in vitamins, it has a very specific taste and it's more acidic adding variety, so overall morale

    ♡ passionfruit is a climbing vineso it can be treated vertically instead of treating it like another tree
    
    ♡ fleshy fruits are good for high water content and high morale and dry fruits are good for seeds and plant reproduction 

   ♡ they aren't intended as a staple or fast food source

#### Why avoid heavily processed crops?
    ♡ reduces the equipment and labour required after harvest

    ♡ simpler to represent in the simulation

    ♡ more practical for early habitat operations

### ----------------------------------------

### Dev Log Notes:
###### 05/09/2026:
    ♡ researched crops and crew nutrition
    ♡ decided to track plants by zone instead of individual plants

###### 05/16/2026:
    ♡ began considering crops that support both nutrition and morale

###### 08/06/2026:
    ♡ cleaned crop list and assigned crops to the three zones of the new large greenhouse

##      08/09/2026
    ♡ going over nutrition plan and  macronutrient targets

    ♡ I chose these targets intitally (carbohydrates: 40%, fat: 45%, protein: 15%) b/c I was taking crew stability into consideration, as well as crew performance, cognition and overall wellbeing. I need to choose between this and a conventional nuritional range, so I decided to try to stay closer to the suggested range but still make it a bit different like a sort of compromise 

    ♡ I want the habitat food system biased toward steady energy, satiety, minimally processed foods and avoiding excessive carbohydrate dependence still so I will change the fat and protein goals, and keep the carb target as is

### ----------------------------------------
## more in depth crop notes I wanted to keep:
    ♡ fleshy fruits:
        high water content, high morale

    ♡ dry fruits:
        good for seeds and plant reproduction 

    ♡ sweet potato:
        - high in calories
        - edible leaves
        - can grow vertically
        - germination: 1–14 days
        - vegetative growth: 2–8 weeks
        - flowering: 6–12 weeks
        - harvest: ~ 3 months

    ♡ potato:
        - high in calories
        - edible leaves
        - can grow vertically
        - germination: 1–14 days
        - vegetative growth: 2–8 weeks
        - flowering: 6–12 weeks
        - harvest: ~ 3 months
        
        - Nasa notes:
            - comparison of hydroponically grown underground crops reported maximum dry weight yields of ~ 4.69 kg/m² for potato versus 2.54 kg/m² for sweet potato under the tested controlled environment conditions

            - Denali and Norland potatoes were planted using nutrient film hydroponics for 112 days, producing  ~1.8–2.85 kg fresh tubers per plant depending on cultivation and spacing (water use in that experiment was about 2 L/m²/day)
        
            - hydroponic sweet potato experiments produced ~ 1.79 kg of fresh storage root per plant, with reported edible biomass ~ 60–89% (depending on the experiment) and harvest periods were around 105–130 days

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

    ♡ SWEET corn:
        - stalks/leaves = biomass after harvest
        - grows upward rather than sprawling horizontally
        - germination: 5–12 days
        - vegetative growth: 30-50 days
        - flowering: 32-62 days
        - harvest: ~ 2-3 months
        - one cup of cooked sweet corn = 
            ~ 130 calories, 3 grams of protein, and 2 grams of fat

        - cons: highly parishable on earth, space considerations
        

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