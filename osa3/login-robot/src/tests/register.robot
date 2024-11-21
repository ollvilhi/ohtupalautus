*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials   uusikalle  uusikalle123
    Output Should Contain   New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain   User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials   iy  yeah5839
    Output Should Contain   Username should be at least three characters between a-z

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  joe89  okpw4312
    Output Should Contain    Username should be at least three characters between a-z

Register With Valid Username And Too Short Password
    Input Credentials  hyvakalle  ok
    Output Should Contain    Password should be at least 8 characters and not only letters between a-z

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials   hyvakalle  onlyletters
    Output Should Contain   Password should be at least 8 characters and not only letters between a-z

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User    kalle   kalle123