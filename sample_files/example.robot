*** Setting *** 
Library    SeleniumLibrary 
Documentation    Simple documentation for test suite.
...              The only purpose is to test if test suite documentation is correctly added.

*** Variables *** 
${UserName}  amitb 
${Password}  amitb 

*** Keywords *** 
Keyword 1
    Pass Execution

Keyword 2
    Fail    message
    

*** Test Cases *** 
TestCase1
    [Documentation]    Multiline documentation part one.
    ...                Multiline documentation part two.
    ...                Multiline documentation part three.
    ...                Multiline documentation part four.
    Keyword 1

TestCase2
    [Documentation]    Multiline documentation part one.
    ...                \nMultiline documentation part two.
    ...                \nMultiline documentation part three.
    ...                \nMultiline documentation part four.
    Keyword 1

TestCase3
    [Documentation]    One line documentation.
    Keyword 1

TestCase4
    Keyword 1

