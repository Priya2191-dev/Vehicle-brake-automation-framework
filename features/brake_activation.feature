Feature: Brake Activation System

  Scenario: Normal braking reduces vehicle speed
    Given vehicle speed is 100 km/h
    When brake pedal is pressed with pressure 20
    Then vehicle speed should decrease

  Scenario: Strong braking reduces speed quickly
    Given vehicle speed is 120 km/h
    When brake pedal is pressed with pressure 40
    Then vehicle speed should decrease
