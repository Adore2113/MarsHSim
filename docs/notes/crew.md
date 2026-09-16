# Crew and Scheduling
### General Notes:
    ♡ crew total: 30

    ♡ each crew member has private space for sleep, work, relaxation and time alone

    ♡ comfort features remain limited by habitat-wide safety, atmosphere, power, water and thermal requirements

    ♡ Crew Quarter layout and room details are kept in the Social and Shared Living Space Layout file

    ♡ V1 models the combined metabolic effects of the full crew

    ♡ individual crew schedules, shifts and assignments are planned but are not implemented yet

### ----------------------------------------

## Crew and Habitability Plan (updated 08/31/2026):
### Sleep and Lighting Schedule:
    ♡ overnight sleep period: 21:30-06:00 LMST
    ♡ scheduled sleep period: 8.5 hours
    ♡ intended actual sleep: ~ 8 hours
    ♡ habitat lights begin dimming at 21:30 LMST
    ♡ habitat lights begin brightening at 06:00 LMST
    
    ♡ calculation:
        - scheduled sleep period:
            21:30-24:00 = 2.5 hours
            00:00-06:00 = 6.0 hours
            2.5 hours + 6.0 hours = 8.5 hours

### Current Crew Activity Model:
    ♡ current activity states:
        - normal:
            - O₂: 1.0
            - CO₂: 1.0
            - breath vapor: 1.0
            - skin vapor: 1.0
            - heat: 120 W/person
            - nourishment and hygiene water: 1.0
        
        - sleep:
            - O₂: 0.8
            - CO₂: 0.8
            - breath vapor: 0.8
            - skin vapor: 0.4
            - heat: 83 W/person
            - nourishment and hygiene water: 0.6

        - exercise:
            - O₂: 1.5
            - CO₂: 1.5
            - breath vapor: 1.4
            - skin vapor: 2.0
            - heat: 280 W/person
            - nourishment and hygiene water: 1.8

        - intense:
            - O₂: 2.0
            - CO₂: 2.0
            - breath vapor: 1.8
            - skin vapor: 3.0
            - heat: 350 W/person
            - nourishment and hygiene water: 2.2

    ♡ each activity state changes:
        - O₂ consumption
        - CO₂ production
        - breath water vapor
        - skin water vapor
        - crew heat
        - nourishment and hygiene water demand

    ♡ V1 uses one shared crew_activity state for the entire crew meaning all 30 crew currently use the same activity multipliers during a timestep

### Atmosphere Metabolism:

    ♡ base O₂ decrease: 0.00011 kPa/person/hour
    ♡ base CO₂ increase: 0.0000967 kPa/person/hour
    ♡ the activity state scales both values

    ♡ calculation:
        - step duration in hours:
            step duration in minutes ÷ 60

        - O₂ consumed this step:
            0.00011 kPa × crew count × O₂ activity multiplier × step duration in hours

        - CO₂ produced this step:
            0.0000967 kPa × crew count × CO₂ activity multiplier × step duration in hours

    ♡ the approximate 1 kg CO₂/person/day research note is background support, while V1 directly changes cabin CO₂ in kPa

### Crew Humidity:
    ♡ base breath vapor: ~ 1.0 kg/person/day
    ♡ base skin vapor: ~ 0.8 kg/person/day
    ♡ breath and skin vapor use separate activity multipliers and are added to the habitat humidity balance

    ♡ calculation:
        - breath vapor this step:
            (1.0 kg/day × crew count × breath-vapor multiplier × step duration in hours) ÷ 24

        - skin vapor this step:
            (0.8 kg/day × crew count × skin-vapor multiplier × step duration in hours) ÷ 24

        - total crew vapor this step:
            breath vapor + skin vapor

### Crew Heat:
    ♡ crew heat depends on activity state
    ♡ watts are converted to kilowatts before being added to the thermal system
    ♡ conversion: 1,000 W = 1 kW

    ♡ calculation:
        - crew heat output:
            heat per person in W × crew count ÷ 1,000

        - crew heat energy this step:
            crew heat output in kW × step duration in hours

### ----------------------------------------

### Crew Staffing:
    ♡ command, scheduling / general operations: 3
    ♡ ECLSS, atmosphere / water: 5
    ♡ Power, thermal / ISRU: 4
    ♡ Greenhouse / food systems: 6
    ♡ Medical / crew health: 3
    ♡ Maintenance, fabrication / repair: 5
    ♡ Software, automation, communications / science: 4
    ♡ Total: 30

### ----------------------------------------

## Design Evolution:
####

### ----------------------------------------

## Future Considerations:
    ♡ crew temprise needs to be returned!

    ♡ crew waste goes to wastewater, to water/nutrient recovery, to treated nutrient concentrate to greenhouse to zoner reservoirs

### ----------------------------------------

## Design Decisions:


### ----------------------------------------

### Dev Log Notes:
###### From v1_scope:
    ♡ crew receive an 8.5 hour overnight sleep period from 21:30–06:00 LMST, to allow ~ 8 hours of actual sleep

    ♡ habitat lights begin dimming at 21:30 LMST and brighten at 06:00 LMST

###### 03/09/2026
    ♡ NASA references: crew CO₂ production is ~ 1 kg pp/day

###### 03/21/2026
    ♡ going to go w. the crew getting ~ 8 hours of sleep/night so lights will dim at 9:30pm (21:30) and they will brighten at 6:00am, using level of brightness for now

###### 03/28/2026
    ♡ making crew metabolism into its own file for organization and considering breaking it into smaller functions for quicker/easier readability as I add to the file

###### 07/12/2026
    ♡ I'm going to be adding crew scheduling, maintenance and a few updates, w. any complaints or any positive feedback from the crew when things are running well

