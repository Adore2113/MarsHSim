# To Do List:

#### I will be adding and removing from this. I needed somewhere to organize my ideas and thoughts

### Current Focus:
    ♡ stablize all system logic to make sure things are working as I want them to, specifically:
        - water recovery balance
        - greenhouse behavior over day and night cycles
   
     ♡ update irsu to include dust buildup per pipe, efficency loss, ect.

### Next Focus:      


### Later Focus:
    ♡ add greenhouse to crew and other things

    ♡ add tank depletion alerts   

    ♡ add electronic and misc heat and power

    ♡ double check unit consistencies: 
       
        - kpa
        
        - kg
        
        - kw
        
        - kwh

        - ect.


    ♡ consider seperating files for values:
        
        - quick_test = starting values

        - state = things that change per timestep

        - separate file = constants, limits, targets


    ♡ add system efficiency modifiers:
        
        - dust

        - wear

        - environment

   
    ♡ update alerts: 
        


### Eventual Focus:
    ♡ add to file for handling dust:
        
        - finish dust accumulation function
        
        -make dust factor 0.0 - 1.0


    ♡ turn seasons into a list with different changes


    ♡ add crew scheduling


    ♡ have logs for crew reacting to system events
        
        - "some of the crew members are starting to report headaches", etc.

   
    ♡ add maintenance scheduling


    ♡ add wind effects:
        
        - solar effects

        - external habitat effects


    ♡ add random events:
        
        - extra dust accumulation

        - wind removing dust from arrays

        - daily temperature and sunlight events

        - dust storms

        - leaks

        - micrometeorite damage (microscopic)? 


    ♡ add cute messages when system is running perfectly well


    ♡ consider adding disease_risk to greenhouse plants


    ♡ add alerts for: 
        -dust build up
        
        -system efficiency
        
        -weather
        
        -alert for when wellness lights come on
        
        -leak detection
        
        -when scrubbers are full (saturated)


    ♡ add rations, maybe?


### Completed / Mostly Completed:
    I should have added this way earlier to track things.. 

    ♡ add greenhouse variables and greenhouse subsystem

    ♡ add greenhouse water, CO2, O2, heat, LED, and transpiration outputs

    ♡ integrate greenhouse with atmosphere, humidity, water, thermal, and power

    ♡ add dust file

    ♡ add Sabatier system

    ♡ update alerts for gas, pressure, water, power, humidity, thermal, and subsystem modes

    ♡ go through many major unit consistency fixes:
        - kPa atmosphere
        - kg storage
        - kW power
        - kWh energy

    ♡ move some constants and variables out of greenhouse.py and add them to state variables

    ♡ continue adding heat generated and heat waste

        ♡ add power priority systems

