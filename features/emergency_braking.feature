Feature: Emergency Braking System

  Scenario: Automatic braking when obstacle detected
    Given vehicle speed is 80 km/h
    And obstacle distance is 5 meters
    When automated braking system activates
    Then brake pressure should increase
    And vehicle speed should decrease

  Scenario: No braking when safe distance
    Given vehicle speed is 80 km/h
    And obstacle distance is 30 meters
    When automated braking system activates
    Then brake pressure should remain zero
