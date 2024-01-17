Feature: ATM

  As a bank customer
  I want to be able to use an ATM
  So that I can manage my funds

  Scenario: Check balance
    Given I have inserted my card
    And I have entered my correct pin
    When I choose to see my balance
    Then the ATM should display my current balance

  Scenario: Withdraw cash
    Given I have inserted my card
    And I have entered my correct pin
    And my account has sufficient funds
    When I choose to withdraw cash
    Then the ATM should dispense the requested amount
    And my account balance should be reduced by the withdrawn amount

  Scenario: Unsuccessful withdrawal due to insufficient funds
    Given I have inserted my card
    And I have entered my correct pin
    And my account has insufficient funds
    When I choose to withdraw cash
    Then the ATM should display an error message
    And no cash should be dispensed

  Scenario: Unsuccessful operation due to incorrect pin
    Given I have inserted my card
    And I have entered an incorrect pin
    When I choose to see my balance or withdraw cash
    Then the ATM should display an error message
    And no operation should be performed