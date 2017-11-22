*** Settings ***
Library                                 Selenium2Library
Test Setup                              Open Browser                        ${URL}                  ${BROWSER}
Test Teardown                           Close Window

*** Variables ***
${APP}                                  uftHelp
${URL}                                  http://172.17.10.75:8080/company-dashboard/resources/html/insight/overviewIndex.html
${BROWSER}                              CHROME

*** Keywords ***
Search Application On Google
    Input Text                          id=lst-ib                           ${APP}
    Press Key                           id=lst-ib                           \\13
Launch Application
    Wait Until Element Is Visible       link=User-Friendly Techy-Help       20 Seconds
    Click Element                       link=User-Friendly Techy-Help

*** Test Cases ***
[TC-001]-Launching the browser and search and launch the “uftHelp” Application on Google.com
    Search Application On Google
    Launch Application