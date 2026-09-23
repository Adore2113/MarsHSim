# Time, Seasons, Dust and Weather
### General Notes:
    ♡ time is tracked continuously in mission seconds

    ♡ one Martian sol is divided into 24 LMST hours for display

    ♡ daylight length changes with season and the habitat's latitude

    ♡ sunlight rises and falls smoothly across the daylight period using a sine wave

    ♡ background atmospheric opacity changes through the dust-storm season

    ♡ dust storms begin and end through random daily rolls

    ♡ equipment dust accumulation reduces radiator, compressor and ISRU-water-pipe efficiency

    ♡ temperature values are handled by the Thermal / Humidity Control system

### ----------------------------------------

## Arcadia Time, Seasons, Dust and Wheather Plan:
### Mission Time and Sols:
    ♡ mission time begins at 0 seconds
    ♡ seconds per sol: 88,775.244
    ♡ sols per Mars year: 668.599
    ♡ Mars year duration is calculated from sols per year and seconds per sol

    ♡ calculation:
        - seconds per Mars year:
            668.599 sols × 88,775.244 seconds/sol

        - current sol number:
            whole-number portion of mission time in seconds ÷ 88,775.244

        - time within the current sol:
            mission time in seconds modulo 88,775.244

        - orbital degrees advanced per second:
            360° ÷ seconds per Mars year

### LMST Display Time:
    ♡ each sol is displayed as 24 LMST hours
    ♡ each LMST hour is longer than one Earth hour because the full Martian sol is longer
    ♡ the display returns the current sol number, hour and minute

    ♡ calculation:
        - LMST hour length:
            88,775.244 seconds ÷ 24

        - LMST minute length:
            LMST hour length ÷ 60

        - current LMST hour:
            whole-number portion of current-sol seconds ÷ LMST hour length

        - current LMST minute:
            whole-number portion of remaining hour seconds ÷ LMST minute length

### ----------------------------------------

### Habitat Location:
    ♡ location: Arcadia Planitia
    ♡ latitude: 47.0°N
    ♡ longitude: 184.0°E
    ♡ latitude is used to calculate seasonal daylight length
    ♡ longitude is stored but isn't currently used by the V1 time or daylight calculations

### Mars Orbit:
    ♡ axial tilt: 25.19°
    ♡ orbital eccentricity: 0.0934
    ♡ Lₛ at perihelion: 251.0°
    ♡ mean anomaly at mission start: 98.658°
    ♡ mean anomaly represents time-based progress around the orbit

    ♡ eccentric anomaly is an intermediate angle used to solve the elliptical orbit

    ♡ true anomaly represents Mars' actual angular position relative to perihelion

    ♡ northern seasons are defined by areocentric solar longitude as Lₛ, Mars' seasonal position around the Sun

    ♡ Mars' elliptical orbit is modeled so seasonal timing doesn't progress at a constant angular speed

    ♡ northern seasons are defined by areocentric solar longitude (Lₛ)

#### Kepler's Equation:
    ♡ equation: M = E - e sin(E)
    ♡ M: mean anomaly
    ♡ E: eccentric anomaly
    ♡ e: orbital eccentricity

    ♡ Kepler error: E - e sin(E) - M
    ♡ Kepler slope: 1 - e cos(E)

    ♡ the code uses five Newton-Raphson iterations to solve for eccentric anomaly

    ♡ each iteration measures the current error and divides it by the slope to improve the estimate

    ♡ calculation:
        - mean anomaly at the current time:
            starting mean anomaly + mission seconds × degrees advanced per second

        - improved eccentric anomaly:
             current E - Kepler error ÷ Kepler slope

        - true anomaly:
            convert the solved eccentric anomaly through the elliptical-orbit angle relationship

        - areocentric solar longitude:
            (true anomaly + 251.0°) modulo 360°

### Northern Seasons:
    ♡ northern spring:
        - Lₛ from 0° to below 90°

    ♡ northern summer:
        - Lₛ from 90° to below 180°

    ♡ northern autumn:
        - Lₛ from 180° to below 270°

    ♡ northern winter:
        - Lₛ from 270° to below 360°

    ♡ the 90° Lₛ ranges do not take equal amounts of time because Mars moves faster near perihelion and slower near aphelion

    ♡ approximate research estimates:
        - northern spring: ~ 194 sols
        - northern summer: ~ 178 sols
        - northern autumn: ~ 142 sols
        - northern winter: ~ 154 sols

### ----------------------------------------

### Solar Declination:
    ♡ solar declination describes how far north or south the Sun appears relative to the equator through the seasons

    ♡ calculation:
        - 25.19° × sin(Lₛ) = solar declination

### Daylight Length:
    ♡ daylight length depends on latitude and solar declination

    ♡ the calculated daylight period is centered around the middle of the sol

    ♡ calculation:
        - Sun visibility value:
            -tan(latitude) × tan(solar declination)

        - if Sun visibility is at or below -1.0:
            daylight fraction = 1.0

        - if Sun visibility is at or above 1.0:
            daylight fraction = 0.0

        - otherwise, daylight fraction:
            arccos(Sun visibility) ÷ π

        - daylight duration:
            seconds per sol × daylight fraction

        - night duration:
            seconds per sol - daylight duration

        - sunrise:
            night duration ÷ 2

        - sunset:
            sunrise + daylight duration

### Sunlight Across the Sol:
    ♡ maximum daylight intensity: ~ 0.57 kW/m²
    ♡ sunlight is 0.0 before sunrise and after sunset
    
    ♡ during daylight, sunlight follows a sine curve
    ♡ the curve begins at 0.0 at sunrise, reaches 1.0 at the middle of the daylight period and returns to 0.0 at sunset

    ♡ calculation:
        - progress through daylight:
            seconds since sunrise ÷ daylight duration

        - sunlight amount:
            sin(π × progress through daylight)

        - daylight intensity per m²:
            0.57 kW/m² × sunlight amount

### Low-Sunlight Streak:
    ♡ low-sunlight threshold: below 0.30 kW/m²

    ♡ if the peak sunlight for the completed sol is below the threshold, the low-sunlight streak increases by one sol

    ♡ otherwise, the streak resets to 0

### ----------------------------------------

### Atmospheric Dust and Storms:
#### Background Atmospheric Opacity:
    ♡ opacity is represented by optical depth, or tau
    ♡ clear-sky opacity: ~ 0.35 tau
    ♡ maximum background storm-season opacity: 
        ~ 1.15 tau

    ♡ background opacity follows the same seasonal sine shape as storm likelihood

    ♡ calculation:
        - background opacity:
            0.35 + (1.15 - 0.35) × storm-season probability

#### Storm Season:
    ♡ storm season begins at Lₛ 180°
    ♡ storm season ends at Lₛ 330°

    ♡ the seasonal probability factor begins at 0.0, peaks halfway through the season and returns to 0.0 at the end

    ♡ peak seasonal probability occurs near Lₛ 255°
    ♡ calculation:
        - degrees into storm season:
            current Lₛ - 180°

        - storm-season length:
            330° - 180° = 150°

        - progress through storm season:
            degrees into storm season ÷ 150°

        - storm-season probability factor:
            sin(π × progress through storm season)

#### Daily Storm Chance:
    ♡ base daily storm probability: 0.001
    ♡ maximum seasonal probability bonus: 0.02
    ♡ daily storm chance outside storm season: 0.001, or 0.1 %

    ♡ maximum daily storm chance near the middle of storm season: 0.021, or 2.1 %

    ♡ calculation:
        - daily storm chance:
            0.001 + 0.02 × storm-season probability factor

        - storm begins:
            random number from 0.0 to below 1.0 < daily storm chance

#### Storm Duration and Severity:
    ♡ daily storm-end probability: 0.15

    ♡ when a storm starts, its tau is selected randomly from 1.75 to 5.0

    ♡ storm severity stays unchanged for the duration of that storm in V1

    ♡ storm_sols_passed starts at 1 on the starting sol

    ♡ if the storm continues, storm_sols_passed increases by one each sol

    ♡ when the storm ends, storm tau and sols passed reset to 0

    ♡ calculation:
        - storm ends today:
            random number from 0.0 to below 1.0 < 0.15

### Weather Status:
    ♡ clear: opacity below 0.65 tau
    ♡ dusty: opacity from 0.65 tau to below 1.75 tau
    ♡ storm: opacity at or above 1.75 tau

    ♡ maximum modeled storm opacity: 5.0 tau

### Equipment Dust Accumulation:
    ♡ base dust-efficiency loss: 0.007 per sol
    ♡ online systems accumulate dust 1.25 times faster
    ♡ dust loss is scaled to the duration of each step

    ♡ calculation:
        - seconds this step:
            step duration in minutes × 60

        - sols this step:
            seconds this step ÷ 88,775.244

        - efficiency loss:
            base dust rate × equipment multiplier × online multiplier when applicable × sols this step

        - new dust factor:
            the larger of minimum efficiency or current dust factor - efficiency loss

### ----------------------------------------

## Design Evolution:
    ♡ the first time model assumed a 24 hour day and was updated to use a Martian sol of 24 hours, 39 minutes and 35 seconds

    ♡ timekeeping was moved into Mars_time.py

    ♡ daylight was originally going to use hardcoded percentages

    ♡ a sine wave was added so sunlight changes smoothly through the sol

    ♡ latitude, axial tilt, sunrise, sunset and seasonal daylight fraction were added

    ♡ early seasons used simpler midpoint estimates

    ♡ the orbital model was updated after recognizing that Mars does not move around the Sun at a constant speed

    ♡ Kepler's equation and Newton-Raphson iteration were added to calculate true orbital position

    ♡ atmospheric opacity was added after the seasonal model

    ♡ random storm starts were added so weather would not be completely predictable

    ♡ storm tau remains fixed throughout each storm in V1

    ♡ dust began as a general 0.0-1.0 efficiency factor

    ♡ equipment specific accumulation rates, online multipliers and minimum efficiencies were added

### ----------------------------------------

## Future Considerations:
    ♡ use longitude when converting mission time into location specific solar time, if mission time isn't already treated as Arcadia LMST

    ♡ rename get_solar_decline_deg to get_solar_declination_deg for clarity ?

    ♡ confirm the selected starting mean anomaly and its intended starting Lₛ

    ♡ make sure peak_sunlight_today resets once per sol and low-sunlight streak updates only once after the peak is finalized

    ♡ confirm where atmospheric opacity reduces sunlight and solar generation in the engine

    ♡ allow storm tau and severity to change during a storm

    ♡ allow storms to change temperature, solar performance and equipment dust accumulation directly

    ♡ add storm movement, regional versus global scale and more varied duration

    ♡ add wind calculations in a future version

    ♡ research dune migration and longer-term surface changes

    ♡ model changes in sunlight absorption caused by ice and dust

    ♡ add solar array dust accumulation and automated cleaning behavior

    ♡ consider electrostatic dust removal, vibration cleaning, protective covers and automated panel movement

    ♡ add maintenance or cleaning that can restore radiator, compressor and pipe dust factors

    ♡ decide whether backup radiators should accumulate dust more slowly than primary radiators when both have the same status

    ♡ decide whether deploying and retracting ISRU pipes should accumulate dust differently from offline pipes

    ♡ connect storm intensity to the base equipment dust-accumulation rate

    ♡ replace midpoint seasonal temperature assumptions with a more detailed surface-weather model if needed beyond V1

### ----------------------------------------

## Design Decisions:
#### Why use mission seconds as the main clock?
    ♡ one continuous value makes timestep calculations consistent

    ♡ sol number, LMST, season and orbital position can all be derived from mission time and I like how it looks

#### Why display each sol using 24 LMST hours?
    ♡ it provides a familiar clock format while preserving the full Martian sol length

    ♡ each displayed LMST hour automatically becomes slightly longer than an Earth hour

#### Why model Mars' elliptical orbit?
    ♡ Mars travels faster near perihelion and slower near aphelion, changing the duration of the seasons affecting solar energy and dust storm timing

#### Why use Newton-Raphson iteration?
    ♡ Kepler's equation can't be rearranged into one simple direct solution for eccentric anomaly

    ♡ Newton-Raphson quickly improves the estimate by using the current error and slope and felt like the most efficent choice for this (moderate eccentricity allows five iterations to provide a stable V1 result)

#### Why use Lₛ for seasons?
    ♡ Lₛ describes the actual Mars seasonal position around the Sun

    ♡ it gives consistent boundaries for spring, summer, autumn and winter and provides a useful position for defining dust-storm season

#### Why use a sine wave for daylight?
    ♡ sunlight should rise gradually after sunrise and fall gradually before sunset

    ♡ a sine wave makes a smooth daily curve without hardcoded hourly percentages, which I wanted to avoid

#### Why use random storm rolls?
    ♡ season affects storm likelihood but does not make individual storms completely predictable

    ♡ a random daily roll allows different simulation runs to experience different weather

    ♡ roll_for_storm is also a reference to rolling for events in tabletop role playing games, like dnd

#### Why give equipment minimum dust efficiencies?
    ♡ the floors prevent dust accumulation from reducing equipment output below the selected V1 minimum

    ♡ different equipment types can retain different minimum capability

### ----------------------------------------

### Dev Log Notes:
###### From v1_scope:
    ♡ dune migration (research this more)

    ♡ sun absorption changes from ice / dust
    
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

    ♡ I'm going to add random dust storms right now, while I'm working on season changes and atmospheric opacity, checking if Mar's is in storm season, how far through it it is and also have random wheather b/c predictable wheather isn't realistic

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

