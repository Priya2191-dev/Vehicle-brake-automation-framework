Feature: Speed Anomaly Detection

  Scenario: Detect anomaly in speed values
    Given speed values 50, 55, 60, 120
    When anomaly detection is performed
    Then anomaly should be detected

  Scenario: No anomaly in normal speeds
    Given speed values 50, 55, 60, 58
    When anomaly detection is performed
    Then no anomaly should be detected

  Scenario: No anomaly when all speeds are equal
    Given speed values 50, 50, 50, 50
    When anomaly detection is performed
    Then no anomaly should be detected

  Scenario: Detect anomaly with custom threshold
    Given speed values 50, 55, 60, 70
    When anomaly detection is performed with threshold 1
    Then anomaly should be detected
