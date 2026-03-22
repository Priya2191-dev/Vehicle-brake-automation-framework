# 🚗 Vehicle Brake Automation Framework

## Objective

- To design and develop an automation framework for validating vehicle braking system using Python and BDD.
- To simulate real world braking scenarios including normal, edge and failure conditions.
- To ensure system reliability by validating brake response, safety thresholds, input handling.
- To integrate CI/CD for continuous testing and faster feedback on code changes.

## Overview

The Vehicle Brake Automation Framework is an end-to-end Python-based automation testing system designed to simulate and validate vehicle braking behavior.

This project mimics real-world automotive systems by integrating:

- Digital Twin vehicle modeling
- Automated braking scenario
- Brake simulation engine
- CAN bus communication  
- Telemetry monitoring  
- AI-based anomaly detection  
- Dashboard visualization  
- BDD and unit test automation

## Features

- Digital Twin Vehicle Model:
  
  Simulates speed, brake pressure, and acceleration.  

- Automated Braking:
  
  Detects obstacles and applies brakes automatically.

- Brake simulation engine:

  This simulates vehicle deceleration when brake pressure applied.

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
