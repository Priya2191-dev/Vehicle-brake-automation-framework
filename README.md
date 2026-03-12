# Vehicle Brake Automation Framework

This project implements an automation testing framework for validating vehicle braking systems.

## Features

- BDD test scenarios
- Digital twin vehicle model
- Automated braking
- CAN bus communication
- Brake simulation engine
- Telemetry monitoring
- AI anomaly detection
- Dashboard visualization
- CI/CD automation using Jenkins

## Architecture

BDD Scenario → Automation → Simulation → Telemetry → Dashboard

## Technologies

Python  
Behave BDD  
Matplotlib  
NumPy  
Jenkins CI/CD

## Repository Structure
 
digital_twin -> vehicle model  
scenarios -> automated braking
can_simulaton -> send/receive messages
simulation -> brake physics
telemetry -> data collection  
ai_analysis -> anomaly detection
dashboard -> visualization  

## Example Output

Initial speed: 120 km/h  
Brake pressure: 30  

Speed after braking: 115.5 km/h

## CI/CD

Automated pipeline runs tests whenever code is updated.
