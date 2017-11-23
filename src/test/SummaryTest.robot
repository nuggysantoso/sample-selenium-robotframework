*** Settings ***
Resource                                ../main/SummaryPage.robot
Resource                                ../main/BaseBuilder.robot
Test Setup                              Open Browser Test Setup                 http://${HOST}${COMPANY-DASHBOADR-URL}
Test Teardown                           Close Window

*** Variables ***
${HOST}                                 172.17.10.75:8080
${COMPANY-DASHBOADR-URL}                /company-dashboard/resources/html/insight/overviewIndex.html

*** Test Cases ***
[CD_01]-To verify user is able to click tab menu on subheader section to navigate respective page
    Verify Summary Page Is Displayed
    Click Start Date Picker
    Click End Date Picker