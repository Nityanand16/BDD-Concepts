# Example

Feature: Showing off behave

  Scenario: Run a simple test
     Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!
  Scenario: Run a simple test
     Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!

    Feature: To test the login functionality

    Scenario: verify the login with valid credentials
        Given I am on loginpage
        When I type my email
        And I type my password
        And I click on login button
        Then I should see welcome text
