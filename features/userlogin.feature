Feature: example user login

  Scenario Outline: user role "<role>"

    Given I login as a "<role>"
    Then I should be at "<page>"

  Examples:

    |   role     |  page            |
    |   admin    |  dashboard       |
    |   user     |  welcome to page |
    |   customer |  help section    |