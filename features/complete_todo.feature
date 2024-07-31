# language: en

Feature: Complete a ToDo

    Scenario: Complete a ToDo
        Given I have a ToDo "Buy milk"
        When I complete the ToDo
        Then the ToDo is marked as complete
