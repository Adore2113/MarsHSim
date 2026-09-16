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

### ----------------------------------------

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

### Crew Water Use:
    ♡ base nourishment water: ~ 2.35 kg/person/day
    ♡ includes drinking and food preparation
    ♡ base hygiene water: ~ 1.5 kg/person/day
    ♡ base black water: ~ 1.8 kg/person/day
    ♡ nourishment and hygiene water use the activity state water multiplier
    
    ♡ black water production does not currently use the activity multiplier
    
    ♡ nourishment and hygiene water are removed from potable water storage
    
    ♡ 75 % of hygiene water is routed to gray-water storage

    ♡ calculation:
        - nourishment water this step:
            (2.35 kg/day × crew count × water multiplier × step duration in hours) ÷ 24

        - hygiene water this step:
            (1.5 kg/day × crew count × water multiplier × step duration in hours) ÷ 24

        - potable water used:
            nourishment water + hygiene water

        - black water this step:
            (1.8 kg/day × crew count × step duration in hours) ÷ 24

        - gray water recovered:
            hygiene water × 0.75

### ----------------------------------------

### Habitability and Crew Wellbeing:

    ♡ private Crew Quarters provide a place to sleep, work, relax and be alone

    ♡ personal room controls and visual customization gives familiarity and a sense of control

    ♡ distinct room identities support navigation, familiarity and choice

    ♡ shared living, creative, media, exercise, quiet and reflection spaces gives different social and sensory options

    ♡ wellness lighting supports crew wellbeing during extended low-sunlight periods and dust storms

    ♡ future crew reports will include both complaints and positive feedback

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
    ♡ crew metabolism was handled with other habitat systems and was moved into its own file for organization and future readability

    ♡ metabolism outputs were organized into a dictionary as the project structure became more consistent

    ♡ moisture contributions were added later when humidity control was implemented

    ♡ the crew sleep period was set to 21:30-06:00 LMST to allow ~ eight hours of actual sleep

    ♡ habitat lighting was connected to the sleep schedule by dimming and brightening at those times

    ♡ an early dashboard plan added a crew information panel and a separate alerts panel

    ♡ the habitat log was expanded to eventually include crew symptoms, complaints, positive feedback and recovery updates

    ♡ early habitat planning focused more heavily on minimum volume and later focused more importance on privacy, environmental control, room identity, comfortable shared areas and mostly long term psychological wellbeing

### ----------------------------------------

## Future Considerations:
    ♡ crew temprise needs to be returned!

    ♡ crew waste goes to wastewater, to water/nutrient recovery, to treated nutrient concentrate to greenhouse to zoner reservoirs

    ♡ create individual crew schedules instead of applying one shared activity state to all 30 crew

    ♡ define work shifts, off-duty periods, exercise, personal time and sleep for each crew member

    ♡ add on-call and emergency scheduling without eliminating protected sleep and recovery time

    ♡ connect maintenance assignments to equipment condition, faults and planned service intervals

    ♡ add crew complaints, symptoms, positive feedback and wellbeing updates to the habitat log

    ♡ develop crew psychology and social friction modeling without reducing wellbeing to a single unrealistic score

    ♡ decide if daily water and vapor rates should divide by 24 hours or the full ~ 24.66-hour Martian sol !!

    ♡ return crew_temp_rise_kwh if downstream systems or logs need crew heat energy as well as heat flow

    ♡ decide where the remaining 25 % of hygiene water goes after 75 % is routed to gray-water storage

    ♡ decide if black-water production should change with activity state

    ♡ consider scheduling nourishment and hygiene events instead of spreading their water demand continuously across every timestep

    ♡ connect treated crew waste to wastewater recovery, nutrient processing, greenhouse nutrient concentrate and zone reservoirs

    ♡ define how the two unassigned Crew Quarters are assigned during maintenance, medical isolation or other temporary needs

### ----------------------------------------

## Design Decisions:
#### Why use 30 crew?
    ♡ 30 people provide enough staffing to cover multiple essential technical, medical, food and operational roles

    ♡ the habitat is also assumed to use extensive automation so a relatively small crew can operate the full system

#### Why give every crew member private quarters?
    ♡ long-term habitation requires more than a place to sleep and lets crew members work, recover, control stimulation and spend time alone

    ♡ personal control and customization support identity, comfort and psychological wellbeing

    ♡ there are only 30 crew members so it is managable

#### Why use activity multipliers?
    ♡ sleep, normal activity and exercise don't create the same atmosphere, humidity, heat or water loads

    ♡ multipliers let one base metabolism model respond to different activity levels

    ♡ this keeps V1 manageable while leaving room for individual scheduling later

#### Why use an 8.5-hour sleep period?
    ♡ the full period includes time for settling down and waking up

    ♡ it's made to allow ~ 8 hours of actual sleep

#### Why connect lighting to the sleep schedule?
    ♡ gradual dimming and brightening provide consistent environmental time cues for psychological wellbeing and familiarity

    ♡ predictable lighting supports the crew's daily routine


### ----------------------------------------

### Dev Log Notes:
###### 03/09/2026
    ♡ NASA references: crew CO₂ production is ~ 1 kg pp/day

###### 03/21/2026
    ♡ going to give the crew ~ eight hours of sleep each night, so lights will dim at 21:30 and brighten at 06:00; using brightness level for now

###### 03/28/2026
    ♡ making crew metabolism its own file for organization and considering breaking it into smaller functions for quicker and easier readability as I add to the file

###### 03/29/2026:
    ♡ made a crew-metabolism dictionary while improving file organization, naming consistency and code consistency

###### 04/09/2026:
    ♡ considering an extra lighting option for periods without sunlight to help support crew morale

    ♡ added a wellness-light function because the crew may need additional support during frequent dust storms or several low-sunlight days

###### 04/20/2026:
    ♡ added moisture variables to the crew-metabolism file and updated temp_system.py

###### 07/04/2026:
    ♡ adding a habitat log screen so status and alerts can include crew complaints about symptoms from pressure, hunger and other conditions, along with emergency system actions

###### 07/12/2026:
    o add a crew information panel beside the status panel and a separate alerts panel on the other side
    
    ♡ going to add crew scheduling, maintenance updates, crew complaints and positive feedback when systems are running well

###### 07/22/2026:
    ♡ I need to consider crew psychology in more depth

###### 08/19/2026:
    ♡ crew waste goes to wastewater, then water and nutrient recovery, then treated nutrient concentrate, and then to greenhouse zone reservoirs