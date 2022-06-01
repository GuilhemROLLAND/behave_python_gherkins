Feature: showing off behave

    Scenario: run a simple test
        Given we have behave installed
        When we implement a test
        Then behave will test it for us!

    Scenario: calculator
        Given set x = 2
        And set y = 2
        When add x and y
        Then result must be equal to 4

    Scenario: table_calculator
        Given a set of values
            | x  | y |
            | 2  | 3 |
            | 12 | 4 |
            | -3 | 6 |
        When add the values
        Then result must be correct
            | result |
            | 5      |
            | 16     |
            | 3      |

