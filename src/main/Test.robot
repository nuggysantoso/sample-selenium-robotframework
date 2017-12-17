*** Settings ***
Library             BaseDriverBuilder.py
Test Teardown       Close All Browser

*** Variables ***

*** Keywords ***
First Setup
    Set Browser Name        Chrome
    Open Window Browser     https://www.google.com

*** Test Case ***
Google 01
    First Setup
    Element Should Visible By Id     gb_200
    Click Element                    gb_70
    
