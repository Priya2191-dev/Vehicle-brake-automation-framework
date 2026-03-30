Feature: Vehicle Dashboard Visualization

  Scenario: Generate plot for speed and pressure
    Given dashboard speed values 10,20,30
    And dashboard pressure values 5,10,15
    When the plot is generated
    Then a plot file should be created

  Scenario: Handle empty data
    Given dashboard speed values
    And dashboard pressure values
    When the plot is generated
    Then a plot file should be created

  Scenario: Invalid input lengths
    Given dashboard speed values 10,20
    And dashboard pressure values 5
    When the plot is generated with invalid data
    Then an error should be raised
