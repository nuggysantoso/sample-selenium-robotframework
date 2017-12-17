*** Settings ***
# Library             BaseBuilderLibrary.py           Firefox
Library             Selenium2Library
*** Variables ***

*** Test Case ***
Set Browser Path
    Open Browser    https://www.google.com          Chrome
    Element Should Be Visible       id=gb200