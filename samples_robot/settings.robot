*** Settings ***
# Documentation
Documentation     Sample documentation line 1.
...               Sample documentation line 2.

# Resource
Resource          ../libs/sample/sample.robot
Resource          full_sample.robot

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

# Test Setup
Test Setup    KEYWORD 1

# Test Teardown
Test Teardown    Run Keywords    KEYWORD1
...              And             KEYWORD2    ${ARG1}
...              And             KEYWORD3    ${ARG2}    ${ARG3}
