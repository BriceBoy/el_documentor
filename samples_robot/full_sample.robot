*** Settings ***
# Documentation
Documentation     Sample documentation line 1.
...               Sample documentation line 2.

# Resource
Resource          ../libs/sample/sample.robot

# Library
Library           ../libs/sample/sample.py
Library           ../libs/sample/sample_with_name.py    WITH NAME    with_name
Library           Sample

# Suite Setup
Suite Setup       Run Keywords    KEYWORD1
...               And             KEYWORD2    ${ARG1}
...               And             KEYWORD3    ${ARG2}    ${ARG3}

# Suite Teardown
Suite Teardown    Run Keywords    KEYWORD1
...               And             KEYWORD2    ${ARG1}
...               And             KEYWORD3    ${ARG2}    ${ARG3}

*** Variables ***
# Variables

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
    Log    message    # Comment

KEYWORD 4
    Log    message
*** Test Cases ***
TEST 1
    [Documentation]    One line documentation
    [Tags]    Test
    [Setup]    Test_Setup
    [Teardown]    Test_Teardown
    Log    This
    Log    Is
    Log    TEST 1

TEST 2
    [Documentation]    Start of multiline documentation
    ...    Suite of multiline documentation
    ...    Last line of multiline documentation
    [Tags]    Test
    [Setup]    Test_Setup
    [Teardown]    Test_Teardown
    Log    This
    Log    Is
    Log    TEST 2