Feature: Automated Braking System

  Scenario: Evaluate braking under different conditions
    Given vehicle speed is <speed>
    And obstacle distance is <distance>
    When system evaluates braking
    Then brake pressure should be <pressure>

    Examples:
      | speed | distance | pressure |
      | 80    | 5        | 40       |
      | 100   | 3        | 80       |
      | 60    | 15       | 20       |
      | 80    | 30       | 0        |
      | 0     | 5        | 0        |
