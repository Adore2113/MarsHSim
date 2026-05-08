# ♡ MarsHSim ♡

![MarsHSim Banner](assets/github_preview.jpg "MarsHSim")

I'm building a Mars habitat simulation where a closed system keeps a crew alive with no resupply, one subsystem at a time.

<p align="center">
♡♡♡
</p>

MarsHSim models a self sustaining Environmental Control and Life Support System (ECLSS) for a crew of 30 inside a closed 2000 m3 habitat on Mars.

♡ The focus is on reliability, realism, machine learning integration, reusability, and eventually cost considerations.


## Overview:

MarsHSim simulates a habitat in Arcadia Planitia running on Mars time (sols and LMST).

The system updates continuously using a timestep based simulation, modeling how a closed life support system maintains stability over time.

<p align="center">
♡♡♡
</p>

My goal is to build something that feels real, structured, autonomous and potentially slighlty interactive on a UI I designed


## Systems:

#### Atmospheric gases:
♡ oxygen (o2)

♡ carbon dioxide (co2)

♡ nitrogen (n2)

♡ argon (ar)

#### Core life support:
♡ amine swing beds

♡ oxygen generation assembly (OGA)

♡ water electrolysis

♡ Sabatier reaction system

♡ major constituent analyzer (MCA)

♡ buffer gas management

#### Environmental systems:
♡ habitat temperature control

♡ radiator cooling

♡ heater systems

♡ humidity control

♡ day/night thermal behavior

♡ Mars solar cycles 

#### Resource systems:
♡ power generation and battery storage

♡ water storage and recovery

♡ hydrogen byproduct storage

♡ atmospheric pressure stabilization

#### Crew and Habitat:
♡ crew metabolism

♡ oxygen consumption & CO2 production

♡ crew heat generation

♡ day and night behavior 


## Planned Features:
♡ greenhouse (in progress)

♡ food supplies

♡ environmental monitoring

♡ emergency scenarios

♡ pressure leaks

♡ crew illness

♡ plant disease

♡ dust storms

♡ extreme temperature shifts

♡ interactive monitoring and control interface


## Current Focus:

♡ greenhouse and food production systems  

♡ expanding closed loop habitat resource management  

♡ laying groundwork for future AI habitat oversight

This project is in active development.


## Project Structure:

♡ docs /
    
    - todo.md = planned systems, ideas, fixes and future tasks

    - dev_log.md = active development log and my thought process

    - v1_scope.md  =  project info and notes

    - v1_state_variables.md  =  reference of all tracked variables

♡ src /sim /

    - alerts.py = simulation alerts and warning systems (very incomplete, not a main focus right now)

    - buffer_gas.py = nitrogen and argon pressure balancing

    - co2_scrub.py = amine swing bed CO2 scrubbing

    - crew.py = crew metabolism and environmental impact

    - dust.py = dust accumulation and environmental dust effects

    - engine.py = main simulation loop and subsystem coordination

    - greenhouse.py = future greenhouse and food production systems

    - mars_time.py = Mars sols, LMST, and day/night cycles

    - oxygen_system.py = oxygen generation assembly (OGA) and electrolysis

    - power.py = solar, batteries, power distribution and power consumption

    - quick_test.py = simulation entry point and testing environment (name subject to change..)

    - sabatier.py = CO2 conversion and methane production systems

    - state.py = habitat state and tracked simulation variables

    - temp_system.py = habitat thermal control and heat modeling

    - water.py = water storage, recovery, and usage tracking

♡ gitignore  =  ignored files

♡ README.md  =  project overview

♡ requirements.txt  =  project dependencies


## Running the Simulation

Currently running as a terminal based simulation.

Make sure Python is installed, then run:
    py -m src.sim.quick_test


## Why this project:

I wanted to build something that feels real, and something I was genuinely interested in and excited about.

MarsHSim started as a way to explore how a closed life support system actually behaves over time, not just as isolated calculations but as a connected system where everything affects everything else.

Instead of solving problems individually, this project focuses on how systems interact, drift, stabilize, learn, and fail.

My long term goal is to move toward a simulation that can support autonomous decision making and eventually integrate machine learning for prediction and control, while keeping it structured, autonomous, and slightly interactive to make it more engaging.

For a more detailed breakdown of how this is being built step by step, see my raw development log that I update as I work on it:

docs/dev_log

-Adore2113 ♡