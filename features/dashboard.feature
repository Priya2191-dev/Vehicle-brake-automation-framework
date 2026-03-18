Feature: Plot speed and pressure

  Scenario: Generate plot for speed and pressure
    Given dashboard speed values 10,20,30
    And dashboard pressure values 5,10,15
    When the plot is generated
    Then a plot file should be created
