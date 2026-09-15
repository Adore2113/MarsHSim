# Thermal / Humidity Control
### General Notes:
    ♡ preliminary estimates

    ♡ V1 uses one cabin temperature
    ♡ heaters, radiators, solar gain, leak, crew and equipment heat all hit that one number

    ♡ greenhouse CHX stays in Hive-8
    ♡ habitat CHX lives in the Atmosphere / Resource Recovery Room
    ♡ both still report heat into the same cabin temperature for V1

    ♡ kW is the heat flow
    ♡ °C is the result after it hits thermal mass
### ----------------------------------------

## Habitat Thermal Plan (updated 09/15/2026):

#### Targets:
    ♡ habitat start / target: ~ 23.0 °C
    ♡ comfort: ~ 20.0-25.0 °C
    ♡ too hot alert: > 28 °C
    ♡ too cold alert: < 18 °C
    ♡ humidity start / target: ~ 48 %
    ♡ humidity stays between 20 % and 80 %

    ♡ low power target: ~ 21.0 °C
    ♡ critical power target: ~ 19.0 °C

    ♡ V1 uses one temperature for the whole habitat

### ----------------------------------------

### Dev Log Notes:
###### From v1_scope:
    ♡ going to use kilowatts (kW) for heat sources (kW = change) (C = result)

    ♡ adding a variable for the habitat's insulation as a heat leak rate and I'm using 1.0 kw/C as a starter value

    ♡ I decided to go with radiator arrays, mostly to keep my code more manageable

    ♡ after doing some research, I decided to go with a 6 array set up with a total of 50 panels for now

    ♡ a condensing heat exchanger (CHX) which I read removes humidity while it could cool the cabin but I'm going to make it mainly a humidity control subsystem first with slight cooling, b/c I already have the radiators

###### 03/17/2026
    ♡ moving to temp management today and thermal control, I decided to get the main ideas down using radiators and do more research into other ideas later on

###### 03/18/2026
    ♡ deciding if I should add heat output into current functions, or have its own. I'm going to keep adding to the proper functions

    ♡ adding heat produced by amine beds w. exothermic absorption (the amine molecules catch the CO₂ which releases heat) and regeneration

###### 04/14/2026
    ♡ I'm going to focus on the thermal parts before considering humidity

###### 04/15/2026
    ♡ fixed insulation and thermal mass values

    ♡ adding electric heaters and radiators and I want to make both of them like I did some of the other systems w. lists (amine beds, etc.)

###### 04/16/2026
    ♡ going to change the way I have the radiators_online function set up b/c I don't like to hardcode the numbers like I did and I'm going to have a hysteresis so that my new setup doesn't turn on and off abruptly too often

    ♡ added radiator power usage and added radiator info to the other necessary files

    ♡  still playing around w. insulation values (0.3 - 0.8?)

###### 04/18/2026
    ♡ I'm going to keep the radiators using the habitat temp directly to run and focus on adding in the electric heaters until then

    ♡ I am going to worry about emergencies later and just get the foundation down first, but I did add another two radiators to the radiator list

    ♡ making heaters their own list to be handled the same way the other systems are

###### 04/20/2026
    ♡ moving onto humidity in thermal b/c I decided I will alter the insulation and mass values once I have all the systems implemented including water and everything

    ♡ added moisture variables to the crew metabolism file and updated temp_system.py

    ♡ I'm considering adding a new file to handle humidity depending on how big that part gets

###### 04/21/2026
    ♡ adding sunlight to the thermal system

###### 04/23/2026
    ♡ adding condensate/CHX to water_system and engine and made OGA use potable water

    ♡ fixing heating issue, my hysteresis was WAY too high in temp_system.py

###### 04/24/2026
    ♡ starting by fixing my thermal mass value and insulation strength

    ♡ fixed thermal_system.py by cleaning up globals, changing placeholder values to real/accurate values and updating the rad heat function

    ♡ started adding backup radiators and heaters

###### 04/25/2026
    ♡ updated CHX to include cooling

###### 06/14/2026
    ♡ fixing temp issues, starting w. the insulation strength/thermal mass and fixing my heater logic

###### 06/16/2026
    ♡ fixing radiator and heaters to make things smooth and effective

    ♡ I'm happy w. how the temp system is running for now, so now I'm running atmosphere again




