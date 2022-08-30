*** Keywords ***
KEYWORD 1
    [Documentation]    One line documentation
    [Arguments]        ${ARG1}
    Log    message

KEYWORD 2
    [Documentation]    First line of documentation
    ...                Second line of documentation
    [Arguments]        ${ARG1}    ${ARG2}
    Log    message

KEYWORD 3
    [Documentation]
    [Arguments]
    Log    message

KEYWORD 4
    Log    message
    ...    test

KEYWORD 5
    [Documentation]    First line of documentation
    ...                Second line of documentation
    ...                Third line of documentation
    [Arguments]        ${ARG1}
    ...                ${ARG2}
    ...                ${ARG3}
    Log    message
    ...    test