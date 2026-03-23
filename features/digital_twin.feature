Feature: Vehicle behavior

  Scenario: Accelerate the vehicle
    Given a vehicle
    When the vehicle accelerates by 50
    Then vehicle speed should be 50

  Scenario: Apply brake reduces speed
    Given a vehicle with initial speed 100
    When vehicle brake is applied with pressure 20
    Then vehicle speed should be 96
    And digital twin brake pressure should be 20
