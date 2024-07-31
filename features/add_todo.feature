# language: en

Feature: Add a ToDo

    Scenario: Add a ToDo
        Given I create a new empty ToDo list
        When I add a ToDo "Comprar pan"
        Then I should see the ToDo in the list
