# 🚗 Vehicle Brake Automation Framework

## Objective

- To design and develop an automation framework for validating vehicle braking system using Python,   Pytest and BDD.
- To simulate real world braking scenarios including normal, edge and failure conditions.
- To ensure system reliability by validating brake response, safety thresholds, input handling.
- To integrate CI/CD for continuous testing and faster feedback on code changes.
- To generate automated test reports using allure.

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
  
  Implements automated braking logic based on distance.

- Brake simulation engine:

  This simulates vehicle deceleration when brake pressure applied.

- CAN Bus Simulation:
  
  Sends and validates ECU communication messages and verify signal integrity.

- Telemetry Monitoring:
  
  Logs speed and brake pressure, calculate average speed and handles invalid inputs.

- AI Anomaly Detection:
  
  Detects abnormal system behavior.

  Uses:

  Mean deviation

  Standard deviation (z-score method)

- Dashboard Visualization:
  
  Plot speed vs brake pressure. Graphs using Matplotlib. 

## Installations

git clone https://github.com/Priya2191-dev/Vehicle-brake-automation-framework.git

cd Vehicle-brake-automation-framework

pip install -r requirements.txt

## Tech Stack

- Language: Python
- Testing: Pytest, Behave(BDD)
- CI/CD: Github Actions
- Visualisation: Matplotlib
- Data Analysis: NumPy
- Reporting: Allure Reports

## Testing Strategy

- Unit Testing using Pytest
- Behavior-Driven Testing using Behave
- Edge Case Handling
- Input Validation Testing

## CI/CD Pipeline

- Runs on every push & pull request
- Executes:
  
  Pytest(Unit tests)
  
  Behave(BDD tests)
  
- Generates

  Allure reports

  Coverage reports

  Dashboard plots

## Reports & Outputs

- Allure Test Reports
- Behave Execution Logs
- Coverage Report
- Dashboard Plot(plot.png)

## Conclusion

The framework successfully automates validation of braking functionalities under various scenarios. CI/CD integration ensures consistent and reliable execution of tests.

## Author

Priyanka Lale
