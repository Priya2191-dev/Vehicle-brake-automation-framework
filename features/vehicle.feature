Feature: Vehicle behavior

  Scenario: Accelerate the vehicle
    Given a vehicle
    When the vehicle accelerates by 50
    Then the speed should be 50

  Scenario: Apply brake reduces speed
    Given a vehicle with initial speed 100
    When brake is applied with pressure 20
    Then the speed should be 96
    And brake pressure should be 20
