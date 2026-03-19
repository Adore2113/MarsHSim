# MarsHSim

I'm building a Mars habitat simulation where the system tries to keep the crew alive.

A realistic Mars habitat life support simulator.

MarsHSim models a self-sustaining Environmental Control and Life Support System (ECLSS) for a crew of 30 people inside a closed 2000 m3 habitat on Mars with no Earth resupply. 

The focus is on reliability, realism, machine learning integration, reusability, and (eventually) cost considerations.

## What it does / What it will do:

- Simulates a 30 crew habitat on Mars in Arcadia Planitia with a habitat size of 2000 m3 

- Runs a timestep based simulation with continuous updates that will be adjustable (currently fixed at 5min intervals)

- Will run an interactive ui I designed

- Runs on sols and Mars local mean solar time (LMST)

- Tracks and maintains:
    - Atmospheric gases:
        - oxygen (o2)
        - carbon dioxide (co2)
        - nitrogen (n2)
        - argon (ar)

    - Core life support systems:  
        - Amine swing beds  
        - Oxygen generation assembly (OGA) and water electrolysis  
        - Major constituent analyzer (MCA)

    -Environmental systems:  
        - Temperature (Celsius)  
        - Power  
        - Water  
        - Food supplies  
        - Crew metabolism  
        - Day and night environment behavior
    
    - Planned future features:

        - Emergency scenarios  
        - Leaks  
        - Illnesses affecting the environment  
        - Dust storms  
        - Extreme temperature changes  

        - Interactive interface for monitoring and control

## Current Focus:

    This simulator is in active development and still in it's early stages.

    Right now the focus is building the core systems one at a time and making sure each one behaves clearly and consistently.  

## Project Structure:
    
- state.py:
  Defines the habitat state and all tracked variables

- engine.py:
  Contains the simulation step and subsystem logic

- quick_test.py:
  Sets initial conditions and runs the simulation loop

- v1_scope.md:
  Creation notes and development process

- v1_state_variables.md: 
  Reference list of all variables used in the state

## How to run:

This project is in early development and currently runs as a simple simulation loop in the terminal.

To run:
1. Make sure Python is installed
2. Run the simulation file

```bash
py -m src.sim.quick_test