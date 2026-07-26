# Power System
### General Notes:
    ♡ I read that even during global dust storms, tilted panels (~ 30° southward) keep minimum irradiance in the 20–60 W/m² range under worst conditions.

    ♡ Actual irradiance will depend on:
        -season
        -solar angle
        -atmospheric dust opacity
        -array tilt

    ♡ maintenance itself will consume power and temporarily take equipment offline, creating another engineering trade off for the habitat.
### ----------------------------------------

### Arcadia Planitia 50 Acre Solar Plan (25/07/2026):
### ----------------------------------------
#### Land area:
    ♡ 50 acres 
    ♡ 20.23 hectares
    ♡  ~ 202,300 m²

#### Panels:
    ♡ total panels: 101,250
    ♡ panels/array: 45
    ♡ tilt: 30° southward
    ♡ allocated field area: ~ 2.0 m²/panel
    ♡ large ground-mounted size
    ♡ calculation: 
        - 202,300 m² ÷ 2,250 arrays ≈ 89.9 m²/array
        - 89.9 ÷ 45 ≈ 2.0 m²/panel

#### Arrays:
    ♡ total arrays: 2,250
    ♡ panels/array: 45
    ♡ allocated field area: ~ 89.9 m²/array
    ♡ calculation:
          202,300 m² ÷ 2,250 ≈ 89.9 m²/array 

#### Control blocks: 
    ♡ total control blocks: 50
    ♡ arrays/block: 45 
    ♡ panels/block: 2,025 
    ♡ calculation:
        - 45 arrays × 45 panels = 2,025 panels/block
        - 89.9 m² × 45 ≈ 4,046 m²/block

### ----------------------------------------
#### Power Production:
    ♡ typical operating capacity w. ~ 70% online:
           2.5–2.7 MW
    ♡ full-capacity continuous average: 
          ~ 3.6–3.8 MW

### ----------------------------------------
#### Seasonal Operation:
#### N Summer: 
    ♡ 1,575 arrays online (35 blocks)
    ♡ 675 arrays offline (15 blocks)
    ♡ transition energy (flips + covers): ~ 2.1–9.1 kWh
    ♡ calculation:
        -flips: 
            675 arrays × 3–13 Wh/array = 2,025–8,775 Wh 
            ≈ 2.0–8.8 kWh
        -covers: 
            675 arrays × 0.1–0.5 Wh/array = 68–338 Wh 
            ≈ 0.07–0.34 kWh
        -combined:
            2.0–8.8 kWh + 0.07–0.34 kWh
             ≈ 2.1–9.1 kWh

#### Spring/Autumn:
    ♡ 1,710 arrays online (38 blocks)
    ♡ 540 arrays offline (12 blocks)
    ♡ transition energy: ≈ 1.7–7.3 kWh
    ♡ calculation:
        -flips: 
            540 arrays × 3–13 Wh/array = 1,620–7,020 Wh
            ≈ 1.6–7.0 kWh
        -covers: 
            540 arrays × 0.1–0.5 Wh/array = 54–270 Wh
            ≈ 0.05–0.27 kWh
        -combined: 
            1.6–7.0 kWh + 0.05–0.27 kWh
            ≈ 1.7–7.3 kWh

#### N Winter:
    ♡ 1,935 arrays online (43 blocks)
    ♡ 315 arrays offline (7 blocks)
    ♡ transition energy: ~ 1.0–4.3 kWh
    ♡ calculation:
        -flips:
            315 arrays × 3–13 Wh/array = 945–4,095 Wh
            ≈ 0.95–4.10 kWh
        -covers:
            315 arrays × 0.1–0.5 Wh/array = 31.5–157.5 Wh
            ≈ 0.03–0.16 kWh
        -combined:
            0.95–4.10 kWh + 0.03–0.16 kWh ≈ 0.98–4.26 kWh
            ≈ 1.0–4.3 kWh

### ----------------------------------------
#### Electrodynamic Dust Shields (EDS):
    ♡ uses a travelling electric field to lift and push dust from the panel surface
    ♡ can be scheduled or triggered by weight or dust sensors
    ♡ NASA describes EDS as using high voltage but low current, making these values estimates
    ♡ run time: ~ 1–5 minutes
    ♡ power: 
          ~ 40–180 W/array while active
    ♡ energy: 
          ~ 0.7–15 Wh/array/cycle
    ♡ calculation:
        - 40 W/array × (1 min ÷ 60) ≈ 0.67 Wh/array
        - 180 W/array × (5 min ÷ 60) = 15 Wh/array

#### Vibration Cleaning:
    ♡ uses piezoelectric actuators or small motors to shake dust loose
    ♡ can be scheduled or triggered by weight or dust sensors
    ♡ run time: 20–60 seconds
    ♡ power: 
          ~ 20–100 W/array while active
    ♡ energy: 
          ~ 0.1–1.7 Wh/array/cycle
    ♡ calculation:
        - 20 W/array × (20 s ÷ 3600) ≈ 0.11 Wh/array
        - 100 W/array × (60 s ÷ 3600) ≈ 1.67 Wh/array

#### EDS & Vibration Combined Cleaning:
    ♡ can be scheduled or triggered by weight or dust sensors
    ♡ these values represent a typical cleaning cycle
    ♡ the systems are not expected to operate at their individual maximums simultaneously
    ♡ run time: 1–3 minutes
    ♡ power: 
          ~ 60–250 W/array (estimated)
    ♡ energy: 
          ~ 2–12 Wh/array/cycle (estimated)
    ♡ theoretical combined range:
        - power: 60–280 W/array
        - energy: 0.8–16.7 Wh/array/cycle
    ♡ calculation:
        - 40–180 W/array + 20–100 W/array = 60–280 W/array
        - 0.7–15 Wh/array + 0.1–1.7 Wh/array = 0.8–16.7 Wh/array
    
### ----------------------------------------
#### Flip & Cover Assumptions:
    ♡ preliminary estimates
    ♡ these values will be updated as I continue designing the flip and cover mechanisms
    ♡ power estimates include movement only unless otherwise stated

#### Array Flip:
    ♡ array flips upside down, releasing dust
    ♡ the array can return upright after the cleaning flip
    ♡ can be scheduled or triggered by weight or dust sensors
    ♡ run time: ~ 2–5 minutes
    ♡ power: 
        -  100–150 W/array while moving
        - ~ 2.2–3.3 W/panel
        - ~ 4.5–6.75 kW/block
    ♡ energy: 
        - ~ 3–13 Wh/array/complete flip
        - ~ 0.07–0.29 Wh/panel
        - ~ 0.14–0.59 kWh/block
    ♡ operation:
        - start up: ~ 150–300 W/array, run time: ~1 –3 seconds
        - actual rotation: ~ 80–180 W/array, run time: ~ 2–5 minutes
        - idle: ~ 0 W
    ♡  calculation:
        - 100 W/array × (2 min ÷ 60) ≈ 3.33 Wh/array (rounding to 3)
        - 150 W/array × (5 min ÷ 60) = 12.5 Wh/array (rounding to 13)
        - 3–13 Wh/array ÷ 45 panels ≈ 0.07–0.29 Wh/panel
        - 3–13 Wh/array × 45 arrays/block ≈ 135–585 Wh/block
                ≈ 0.14–0.59 kWh/block


#### Protective Covers:
    ♡ one sliding cover/array
    ♡ protects arrays while offline against debris and storm damage
    ♡ reduces dust accumulation
    ♡ can be scheduled or triggered by weight/dust sensors
    ♡ run time: ~ 15–30 seconds
    ♡ power: 
        - ~ 25–40 W/array while moving
        - ~ 0.56–0.89 W/panel
        - ~ 1.13–1.80 kW/block
    ♡ energy: 
        - ~ 0.1–0.5 Wh/array/opening or closing
        - ~ 0.002–0.011 Wh/panel
        - ~ 0.0045–0.0225 kWh/block
    ♡ operation:
        - start up: ~ 40–80 W/array, run time: ~ 1–3 seconds
        - sliding: ~ 25–40 W/array, run time: ~ 10–30 seconds
        - holding: ~ 0 W once mechanically latched
    ♡ calculation:
        - 25 W/array × (15 s ÷ 3600) ≈ 0.10 Wh/array
        - 40 W/array × (30 s ÷ 3600) ≈ 0.33 Wh/array
        - 0.1–0.5 Wh/array ÷ 45 panels ≈ 0.002–0.011 Wh/panel
        - 0.1–0.5 Wh/array × 45 arrays/block ≈ 4.5–22.5 Wh/block
                ≈ 0.0045–0.0225 kWh/block


#### Array Flip & Protective Cover:
    ♡ can be scheduled or triggered by weight or dust sensors
    ♡ these values are for quick reference, the systems actually run one after the other
    ♡ power: 
          ~ 125–190 W/array
        - flip: 100–150 W/array
        - cover: 25–40 W/array
    ♡ run time: 
          ~ 2.25–5.5 minutes
    ♡ energy: 
          ~ 3.1–13.5 Wh/array/complete cycle
    ♡ calculation:
        - 100–150 W/array + 25–40 W/array = 125–190 W/array
        - 3–13 Wh/array + 0.1–0.5 Wh/array = 3.1–13.5 Wh/array

### ----------------------------------------
#### Lighting System:
    ♡ 
    
    ♡ planned automatic lighting schedule:
            -brighten at 6:00 AM
            -dim at 9:30 PM (21:30)

    ♡ adaptive lighting based on available sunlight

### ----------------------------------------
#### Future Considerations:
        ♡ I haven't decided which material the covers will be
        
        ♡ how to handle damaged equipment

        ♡ consider changing angles a bit per season and by how much

        ♡ start looking into realistic battery reserves and how much space they take up
        
        ♡ figure out a subsystem power priority system:
            -priority 0:
                -oxygen generation
                -CO₂ scrubbing

            -priority 1:
                -thermal control
                -water systems

            -priority 2:
                -greenhouse
                -lighting support

            -priority 3:
                -comfort systems
                -wellness lighting



### ----------------------------------------
### Early Power System Ideas:
#### Initial Solar Plan:
        ♡ planned to use 30–40 smaller solar panels
        
        ♡ later simplified to 10 larger panels
        
        ♡ eventually implemented my 50 acre solar plan

#### Battery Plan:
        ♡ battery capacity: 4000.0 kWh

#### Solar Panel Model:
        ♡ solar panels modeled similarly to amine beds:
            - each panel has a status
            - power output in full sunlight
            - efficiency
            - dust build up
            - overall condition (for future repair handling)

#### Alternative Solar Plans:
        ♡ I thought about having panels on the outside of my habitat that are foil on one side and black on the other (like a car window shield), that could be flipped like a billboard (one of the ones that have two images on them and they flip to reveal the other image)
        
        ♡ decided to go with a dedicated ground-mounted solar field instead, the other idea has more parts among other potential issues and I want the most daylight possible to reach the inside of the habitat     

#### Low Power Mode:
        ♡ normal

        ♡ low:
            -dim habitat lighting
            -disable wellness lights
            -maintain life support and other essential systems

        ♡ critical/emergency:
            -reduce lighting to the minimum
            -prioritize the OGA and CO₂ scrubbers
            -reduce non-essential systems (planned for future implementation)

#### Lighting:
        ♡ light level goes from 0-1

        ♡ minimum light levels:
            -daytime support: 0.30 (when sufficient sunlight is available)
            -minimum lighting: 0.20
            -emergency lighting: 0.10 (during severe power shortages, if sufficient sunlight is available)

### ----------------------------------------
### Arcadia Planitia 50 Acre Solar Design Decisions:
#### Why 50 acres?
        ♡ I chose 50 acres because it's a land size I grew up around
        
        ♡ I can picture its scale clearly, which makes the solar field easier for me to understand and design
        
        ♡ it feels large enough to support the habitat while still being a manageable area

        ♡ it didn't seem like overkill (maybe seems modest) after looking into the sizes of some solar farms on Earth

#### Why divide the field into arrays and control blocks?
        ♡ the design consists of 101,250 solar panels organized into 2,250 arrays
        
        ♡ the arrays are grouped into 50 independent control blocks of 45 arrays each
        
        ♡ this should make maintenance, fault isolation, seasonal operation and power management more practical
        
        ♡ control blocks can be taken offline at a larger scale
        
        ♡ more manageable, instead of turning panels or arrays off individually

#### Why use multiple dust-removal systems?

        ♡ Mars dust can reduce solar output and interfere with exposed equipment

        ♡ no single cleaning method can handle every condition

        ♡ no single system is likely to handle every situation

        ♡ electrodynamic dust shields can move fine dust from the panel surface     

        ♡ vibration cleaning can help loosen dust that remains attached

        ♡ array flips can release heavier buildup using gravity and movement

        ♡ backup, in case one system fails or can't remove a certain type of buildup

#### Why include protective covers?
        ♡ to protect from storm debris and dust, less wear on the panels and mostly to avoid breakage

        ♡ arrays that are offline don't need to remain exposed
        
        ♡ sliding covers can reduce additional dust accumulation

        ♡ I wanted the cover to be as simple as possible so it wouldn't add to cost, power use or maintenance

        ♡ the covers mechanically latch after moving so they don't continuously consume power

#### Why make maintenance consume power?
        ♡ realism

        ♡ cleaning, flipping and covering the arrays shouldn't happen for free

        ♡ maintenance consumes energy and temporarily removes equipment from service

        ♡ a trade-off between spending power on maintenance & lower solar production now vs more damage later


#### Why use scheduled and sensor-triggered maintenance?
        ♡ scheduled maintenance provides regular cleaning before efficiency drops too low

        ♡ to preserve panels for as long as possible

        ♡ dust or weight sensors allow the system to react to faster buildup between scheduled maintenance

        ♡ using both methods avoids relying entirely on a schedule or sensor readings

        ♡ backup, in case one system fails or isn't enough

#### Why tilt the panels 30° southward?
        ♡ The southward tilt is supposed to improve sun exposure at the habitat N Arcadia Planitia location

        ♡ I read that tilted panels ~ 30° southward keep minimum irradiance in the 20–60 W/m² during severe dust-storm conditions

        ♡ The tilt might help loose dust slide or be carried off of the panel surface

        ♡ I'm considering angle changes after seasonal production is tested in the simulation

### ----------------------------------------
### Power System Notes:
###### 03/29/2026:
        ♡ battery capacity 4000.0 kWh

        ♡ started power_system.py
        
        ♡  since I want to have solar, I'm going to need to have a huge battery storage for when there are dust storms and other impacting factors

###### 04/03/2026:
    ♡ using 0.50kw of sunlight for every 1 square meter (m²) for now, b/c my research showed that Mars sunlight is btwn 0.4 - 0.6 kw / 1 m² during daytime

###### 04/05/2026:
    ♡ the lighting function will react and adjust to the level of daylight

###### 04/10/2026:
    ♡ solar power will recharge habitat batteries

###### 05/25/2026:
    ♡ updating systems to include low power mode

###### 07/21/2026:
    ♡ considering if all of a sudden the pipes are deploying and the low power mode hits or I lose power if the pipes don't retract, they will freeze or use a lot of power w. the heated pipes, but retracting doesn't use power in v1, which I'm questioning now

###### 07/22/2026:
    ♡ today I was thinking about my power reserves and power set up, I am really starting to consider what can ruin my simulation and I need to consider more of a crew psycholoy as well

###### 07/23/2026:
    ♡ since adding in seasons, the daily solar power isn't going to be enough for even daily consumption, I need to consider more options for power

    ♡ my sim is running on average:  Solar Generated = 559.26 kwh, Total Power Used = 649.12 kWh, Net Energy = -89.86 kWh

    ♡ I isolated the subsystems and the greenhouse power is taking up a high percentage of the power, I have it set up to be running w. daylight, but now I'm thinking about having the lights on a 12 hour cycle

    ♡ finished updating the greenhouse lights, at 16 base hours for the greenhouse lights I've manaed to get the Greenhouse energy usage to : 260.46 kwh, instead of 325.55kwh

###### 07/25/2026
    ♡ I am reading about RTG, considering more arrays, maybe  like I mentioned in the past.. 