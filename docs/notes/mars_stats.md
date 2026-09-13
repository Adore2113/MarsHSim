# Time, Seasons, Dust and Weather
### General Notes:

### ----------------------------------------

## _____ Plan ():
####

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
###### From v1_scope:
    ♡ dune migration (research this more)

    ♡ sun absorption changes from ice/dust
    
    ♡ dust factor ranges from 0.0 - 1.0

    ♡ eventually have Mars dust storms and things added in with random, maybe wind cleaning off some of the dust from the solar arrays as well

    ♡ N spring / S fall:
        - 194 sols
        - average temp: ~(-25°C) - ~(-5°C)
        - daytime highs: ~(-10°C) - ~(10°C)
        - nighttime lows: ~(-80°C) - ~(-110°C)
        - warms gradually
        - slightly better ice stability
        - dust: frequent dust devils (small, short dust whirlwinds)

    ♡ N summer / S winter:
        - 178 sols
        - average temp: ~(-15°C) - ~(0°C)
        - daytime highs: ~(0°C) - ~(20°C)
        - nighttime lows: ~(-85°C) - ~(-115°C)
        - better solar reliability
        - dust: lower risk

    ♡ N fall / S spring:
        - 142 sols
        - average temp: ~(-25°C) - ~(-10°C)
        - daytime highs: ~(-15°C) - ~(5°C)
        - nighttime lows: ~(-90°C) - ~(-120°C)
        - occasional high temp: ~(10°C) - ~(15°C)
        - cools gradually
        - dust: frequent dust devils

    ♡ N winter / S summer:
        - 154 sols
        - average temp: ~(-35°C) - ~(-15°C)
        - daytime highs: ~(-25°C) - ~(-5°C)
        - nighttime lows: ~(-100°C) - ~(-130°C)
        - dust: storms, sometimes global

    ♡ global dust storms can drop surface temp averages by 10-20°C for weeks

    ♡ I'm going off of approximate surface temp daily averages for mid-latitude from NASA (Viking 2)

    
    ♡ mission_time_s = current time of day

    ♡ dt_min = how long the step lasts

    ♡ hours_per_step = scaling, production, etc

    ♡ using 0.50kW of sunlight for every 1 square meter (m2) for now

    ♡ Mars sunlight is between 0.4 - 0.6 kW / m2 during daytime

    ♡ Mars time runs at 24 hours and 39 minutes and 35 seconds

    ♡ I'm going to hardcode Mars' tilt to be 25.19 degrees b/c my model isn't going to run long enough to take that slow progression into consideration

    ♡ going to use the midpoint range of each season for now (v1?)

###### 04/04/2026
    ♡ while trying to come up w. a way to make the daylight run smoothly and over time (instead of hardcoding w. certain percentages), I learned what a sine wave is and I'm going to try to use that

    ♡ considering where to add a function for calculating daylight over time (power_system.py or in engine where it handles timestep math, or in its own file completely?)

    ♡ making a file for handling timesteps and related functions

    ♡ I learned today that instead of 24 hours, Mars time actually runs at 24 hours and 39 minutes and 35 seconds, not just 24 hours, so I'm going to fix that now, while I'm working on the new Mars_time.py file

###### 04/05/2026
    ♡ adding in the coordinates for the location of the habitat to make time passing and daylight and everything that goes along w. that more accurate

###### 04/07/2026
    ♡ starting by reviewing my Mars_time file

    ♡ added Mars 24 hours time format

    ♡ added function to determine how the sun shifts from it's orbital position and hardcoded Mars' tilt to be 25.19°

###### 04/08/2026
    ♡ added function to calculate daylight and sunset times to determine the dyalight fraction for one sol

###### 04/13/2026
    ♡ fixed peak daylight today to reset for each sol

###### 04/14/2026

    ♡ adding seasons to Mars_time.py to help w. my temp_system.py file

###### 04/21/2026
    ♡ fixed time, solar and daylight update in step and renamed new state variable to NEW_STATE in caps to make it easier to see while I fix some parts of step
    
###### 04/24/2026
    ♡ I'm reading about dust and how it's managed best on Mars, there are a lot of different ways it's handled.. I like the idea of:
        - electrostatic dust repulsion (EDS) b/c of the fact that it's passive

        - scheduled cleaning, although I like the idea of the crew having one less thing to worry about and maintain, if it can be done on its own
        
        - dust repellent coatings for sure that will need to be redone over a certain amount of times(?)

    ♡ started file for handling dust

###### 04/28/2026

    ♡ mostly a research day about Mars and seasons, temperature, atmosphere and more on systems that would be needed in a real Mars habitat

    ♡ lot's of whiteboard notes and new considerations regarding handling gases and future dust and other events

###### 07/16/2026
    ♡ I'm going to implement seasons into my sim before adding anything else. After doing some research I realized that I had my get_season_angle_deg wrong, b/c Mars doesn't move around the Sun at a constant speed moving faster near perihelion and slower near aphelion, which affects seasonal timing, dust storm season, solar energy and some of the other systems I have set up

    ♡ Reading about Kepler's equation:

    M = E − e sin(E)

    M = Mean Anomaly

    E = Eccentric Anomaly

    e = Orbital Eccentricity

    ♡ I'm considering the options I have for this.. there's the Newton Raphson for eccentric anomaly E. Starting w. E = M, each iteration calculates the current wrong answer and divides it by the 'slope' for a better estimate:

    new estimate = old estimate - error / slope

    ♡ The other option is fixed-point iteration, which rearranges Kepler's equation into:

    E = M + e sin(E)

    But that seems very... inefficient.

    ♡ the eccentricity for Mars is low, so this shouldn't take too many tries to get close using Newton Raphson 

    ♡ anomaly = the angular distance from it's last perihelion


###### 07/18/2026
    ♡ finished adding seasons

    ♡ I'm reading about atmospheric opactiy and tau (how much sunlight the atmosphere blocks before it reaches the ground and optical depth being tau the number used to use the amount), low: 0.2 - 0.5, medium: 0.8 - 1.5 for dusty skies and high:  2 - 5 for major dust storms, these are related to seasons so I figured it was a good next step

###### 07/20/2026
    ♡ I wanted to have a percentage of how far Mar's is through it's storm season

    ♡ I'm going to add random dust storms right now, while I'm working on season changes and atmospheric opacity, checking if Mar's is in storm season, how far through it it is and also have random wheather b/c predictable wheather is not realistic

    ♡ roll_for_storm is both accurate and a nod to dnd

    ♡ the storm opacity is going to be hardcoded for V1

###### 07/21/2026
    ♡ the severity of the same storm stays the same for v1

    ♡ my ui_export.py file is messy right now and unorganized, while I make other changes and make more decisions about the panels for the ui, so I'm going to wait to update that for now and add the dust/storm updates to the alerts.py

    ♡ I've used dust and storm as the same thing in the file, hopefully that isn't confusing for anyone checking it out, I might change this even though the storms on Mars are dust storms

    ♡ I've decided to make a separate file that updates the probability/prediction logicm like the chances of a sotrm today, thermal issues, etc.

###### 08/02/2026
    ♡ I'm going to stick w. a hardcoded tilt angle for v1 instead of adding in the sun's elevation angle

    ♡ add wind calculations to Mars_time.py for v2?

