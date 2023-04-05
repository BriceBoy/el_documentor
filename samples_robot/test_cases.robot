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

TEST WITHOUT DOCUMENTATION
    [Tags]    Test
    [Setup]    Test_Setup
    [Teardown]    Test_Teardown
    Log    This
    Log    Is
    Log    TEST 2

TEST WITHOUT TAGS
    [Documentation]    Start of multiline documentation
    ...    Suite of multiline documentation
    ...    Last line of multiline documentation
    [Setup]    Test_Setup
    [Teardown]    Test_Teardown
    Log    This
    Log    Is
    Log    TEST 2

TEST WITHOUT SETUP
    [Documentation]    Start of multiline documentation
    ...    Suite of multiline documentation
    ...    Last line of multiline documentation
    [Tags]    Test
    [Teardown]    Test_Teardown
    Log    This
    Log    Is
    Log    TEST 2

TEST WITHOUT TEARDOWN
    [Documentation]    Start of multiline documentation
    ...    Suite of multiline documentation
    ...    Last line of multiline documentation
    [Tags]    Test
    [Setup]    Test_Setup
    Log    This
    Log    Is
    Log    TEST 2

TEST WITH NOTHING
    Log    This
    Log    Is
    Log    TEST 2