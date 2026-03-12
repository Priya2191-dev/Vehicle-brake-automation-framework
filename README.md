# Vehicle Brake Automation Framework 🚗⚙️

## Overview

The Vehicle Brake Automation Framework is a scalable automation testing system designed to validate automotive braking systems using simulation, telemetry monitoring, and AI-based anomaly detection.

This project demonstrates how modern automotive QA engineers build automation frameworks to test critical safety components such as vehicle braking systems.

The framework combines:

• Behavior Driven Development (BDD) testing  
• Digital Twin vehicle simulation  
• Brake system physics simulation  
• Telemetry monitoring  
• AI anomaly detection  
• Automated CI/CD testing pipeline  

The project architecture simulates a real automotive validation environment used in automotive engineering.

---

# System Architecture

![Architecture](docs/architecture.png)

Architecture Flow:

BDD Test Scenarios  
↓  
Step Definitions  
↓  
Automation Testing Framework  
↓  
Brake Simulation Engine  
↓  
Digital Twin Vehicle Model  
↓  
CAN Bus Communication  
↓  
Telemetry Monitoring  
↓  
AI Anomaly Detection  
↓  
Dashboard Visualization

---

# Project Workflow

Step 1 — Test Scenario Creation

BDD scenarios are written inside the **features** folder.

---

Step 2 — Step Definitions

The **step_definitions** folder converts human readable BDD scenarios into executable Python automation scripts.

These scripts control the simulation and validate braking behaviour.

---

Step 3 — Brake Simulation Engine

The **simulation** folder contains the braking physics model.

It simulates:

• vehicle deceleration  
• brake pressure effect  
• speed reduction

---

Step 4 — Digital Twin Vehicle Model

The **digital_twin** folder creates a virtual representation of the vehicle.

It simulates:

• vehicle speed  
• mass  
• braking force  
• acceleration

This allows the automation framework to test braking logic without a real vehicle.

---

Step 5 — CAN Bus Communication

The **can_bus** module simulates automotive communication between vehicle components.

Example data signals:

• speed sensor data  
• brake pressure signal  
• ABS activation signal

---

Step 6 — Telemetry Monitoring

The **telemetry** folder records system data during simulation.

Collected telemetry data includes:

• vehicle speed  
• brake pressure  
• braking time  
• deceleration rate

This data is stored and used for analysis.

---

Step 7 — AI Anomaly Detection

The **ai_analysis** folder performs intelligent analysis of telemetry data.

It detects abnormal braking behaviour using statistical anomaly detection.

Example anomalies:

• sudden speed drops  
• brake failure patterns  
• unrealistic sensor readings

---

Step 8 — Dashboard Visualization

The **dashboards** folder generates visual graphs for braking performance.

Example visualization:

![Telemetry](docs/telemetry_dashboard.png)

Graphs show:

• speed vs time  
• brake pressure vs time  
• braking efficiency

---

Step 9 — Automation Testing

Automation test scripts validate braking system behaviour.

If braking fails to reduce speed → test fails.

---

Step 10 — Continuous Integration Pipeline

The project includes automated testing pipelines using GitHub automation.

Every time code is pushed:

1. environment is created  
2. dependencies are installed  
3. automation tests run  
4. simulation results are validated

This ensures continuous testing of the braking system.

---

Simulation Graph:

![Simulation](docs/simulation_graph.png)

This confirms that braking logic successfully reduces vehicle speed.

---

# Key Technologies

Python  
Automation Testing  
Behavior Driven Development (BDD)  
Simulation Modeling  
Telemetry Monitoring  
Data Visualization  
Continuous Integration

---

# Priyanka Lale

Automation Test Engineering Portfolio Project

Vehicle Brake Automation Framework

This project demonstrates advanced automation testing techniques used in modern automotive software validation.
