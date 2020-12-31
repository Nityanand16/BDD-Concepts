Feature: To test the login functionality

    Scenario: verify the login with valid credentials
        Given I am on loginpage
        When I type my email
        And I type my password
        And I click on login button
        Then I should see welcome text