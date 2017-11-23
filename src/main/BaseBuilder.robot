*** Settings ***
Library                         Selenium2Library

*** Variables ***
${Browser}                      CHROME
${RESOURCES}                    /src/main

*** Keywords ***
Open Browser Test Setup         [Arguments]         ${URL}
    Open Browser                ${URL}              ${Browser}
    Set Window Size             ${1366}             ${768}