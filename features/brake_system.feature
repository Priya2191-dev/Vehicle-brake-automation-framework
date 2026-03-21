Feature: Vehicle Brake Validation

  Scenario: Normal braking condition
    Given brake system speed values 10,20,30
    And brake system pressure values 5,10,15
    When the brake validation is performed
    Then braking performance should be valid

  Scenario: Edge case - Zero speed
    Given brake system speed values 0,0,0
    And brake system pressure values 0,0,0
    When the brake validation is performed
    Then braking performance should be valid

  Scenario: Edge case - Maximum speed
    Given brake system speed values 120,150,180
    And brake system pressure values 50,70,90
    When the brake validation is performed
    Then braking performance should be valid

  Scenario: Failure case - Low brake pressure
    Given brake system speed values 40,60,80
    And brake system pressure values 5,10,15
    When the brake validation is performed
    Then braking performance should be invalid

  Scenario: Failure case - Negative values
    Given brake system speed values -10,20,30
    And brake system pressure values 5,15,25
    When the brake validation is performed
    Then braking performance should be invalid

  Scenario: Failure case - Mismatched data
    Given brake system speed values 10,20,30
    And brake system pressure values 5,10
    When the brake validation is performed
    Then braking performance should be invalid
