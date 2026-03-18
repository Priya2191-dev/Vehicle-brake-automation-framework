Feature: Automated Braking

Scenario: Emergency brake
  Given vehicle speed is 80
  And obstacle distance is 5
  When system evaluates braking
  Then brake pressure should be 40
