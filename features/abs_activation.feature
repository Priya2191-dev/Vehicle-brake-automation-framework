Feature: ABS Braking System

  Scenario: ABS activates during sudden braking
    Given vehicle speed is 110 km/h
    When brake pedal is pressed suddenly
    Then ABS system should activate

  Scenario: ABS prevents wheel lock
    Given vehicle speed is 90 km/h
    When sudden brake is applied
    Then wheels should not lock
