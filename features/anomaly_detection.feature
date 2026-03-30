Feature: Hybrid Anomaly Detection

  Scenario: Detect anomaly using absolute deviation
    Given data values 50, 55, 60, 120
    When anomaly detection is performed
    Then anomaly should be detected

  Scenario: Detect anomaly using z-score
    Given data values 50, 52, 53, 80
    When anomaly detection is performed with threshold 1.5
    Then anomaly should be detected

  Scenario: No anomaly in normal data
    Given data values 50, 52, 53, 54
    When anomaly detection is performed
    Then no anomaly should be detected

  Scenario: Handle empty data
    Given data values
    When anomaly detection is performed
    Then no anomaly should be detected

  Scenario: Handle single value
    Given data values 50
    When anomaly detection is performed
    Then no anomaly should be detected
