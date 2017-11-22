*** Settings ***
Library             Selenium2Library

*** Variables ***
${SummaryPage}                              id=summary
${StartDatePickerInput}                     id=startDatePicker
${StartDatePickerImg}                       jquery=div.project-overview-start-date-container > img.ui-datepicker-trigger
${EndDatePickerInput}                       id=endDatePicker
${EndDatePickerImg}                         jquery=div.project-overview-end-date-container > img.ui-datepicker-trigger
${CalendarDiv}                              id=ui-datepicker-div
${FilterBtn}                                id=project-overview-filter-icon-button
${FilterCont}                               jquery=div.project-overview-filter-option-container
${ApplyBtn}                                 id=project-overview-filter-button
${ResetBtn}                                 id=project-overview-reset-button

*** Keywords ***
Verify Summary Page Is Displayed
    Wait Until Element Is Visible           ${SummaryPage}
    Element Should Be Visible               ${FilterBtn}
    Element Should Be Visible               ${StartDatePickerInput}
    Element Should Be Visible               ${EndDatePickerInput}
    Element Should Be Visible               ${FilterCont}
    Element Should Be Visible               ${ApplyBtn}
    Element Should Be Visible               ${ResetBtn}

Click Start Date Picker
    Click Element                           ${StartDatePickerImg}
    Wait Until Element Is Visible           ${CalendarDiv}
    Sleep                                   10s                         Look For Something

Click End Date Picker
    Click Element                           ${EndDatePickerImg}
    Wait Until Element Is Visible           ${CalendarDiv}
    Sleep                                   10s                         Look For Something