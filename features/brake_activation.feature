Feature: Vehicle Brake System

Scenario: Emergency braking
  Given vehicle speed is 120 km/h
  When driver applies emergency brake
  Then vehicle speed should reduce rapidly
