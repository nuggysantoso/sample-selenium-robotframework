*** Settings ***
Library                         Selenium2Library

*** Variables ***
${Browser}                      CHROME
${RESOURCES}                    /Users/nugroho_s/Project/RobotFramework/automation-company-dashboard-robot-framework/src/main

*** Keywords ***
Open Browser Test Setup         [Arguments]         ${URL}
    Open Browser                ${URL}              ${Browser}
    Set Window Size             ${1366}             ${768}