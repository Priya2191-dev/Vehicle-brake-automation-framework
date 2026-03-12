Feature: Brake System

Scenario: Emergency braking
  Given vehicle speed is 120 km/h
  When brake pedal is pressed
  Then vehicle speed should decrease
