# 🚗 Vehicle Brake Automation Framework

## Objective

This project is BDD-based python aautomation framework designed to validate vehicle braking systems by simulating different driving conditions such as speed, brake pressure and failure scenarios.

## Overview

The Vehicle Brake Automation Framework is an end-to-end Python-based automation testing system designed to simulate and validate vehicle braking behavior.

This project mimics real-world automotive systems by integrating:

- Digital Twin vehicle modeling
- Automated braking scenario
- Brake system simulation  
- CAN bus communication  
- Telemetry monitoring  
- AI-based anomaly detection  
- Dashboard visualization  
- BDD and unit test automation

## Features

- Digital Twin Vehicle Model:
  
  Simulates speed, brake pressure, and acceleration.  

- Brake Simulation Engine:
  
  Uses formula: new_speed = speed − (pressure × factor).

- Automated Braking:
  
  Detects obstacles and applies brakes automatically. 

- CAN Bus Simulation:
  
  Simulates ECU communication.  

- Telemetry Monitoring:
  
  Captures speed, pressure, and sensor data. 

- AI Anomaly Detection:
  
  Detects abnormal system behavior. 

- Dashboard Visualization:
  
  Graphs using Matplotlib. 

## Installations

git clone https://github.com/Priya2191-dev/Vehicle-brake-automation-framework.git

cd Vehicle-brake-automation-framework

pip install -r requirements.txt

## Interactive Simulation Demo

[Open in google collab] (https://colab.research.google.com/github/Priya2191-dev/Vehicle-brake-automation-framework/blob/main/notebook/Vehicle-brake-automation-framework.ipynb)

## Testing

- Automation Testing (Pytest + BDD)
- CI/CD Integration

## Usages

Run tests:

- pytest
  
- behave

## CI/CD

GitHub actions pipeline run pytest and behave automatically. 

## Technologies

- matplotlib
- python -can
- numpy
- pytest
- behave

## Conclusion

The framework successfully automates validation of braking functionalities under various scenarios. CI/CD integration ensures consistent and reliable execution of tests.

## Author

Priyanka Lale
