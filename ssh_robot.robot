*** Settings ***
Documentation          This example demonstrates executing a command on a remote machine
...                    and getting its output.
...
...                    Notice how connections are handled as part of the suite setup and
...                    teardown. This saves some time when executing several test cases.

Library                SSHLibrary
Suite Setup            Open Connection And Log In
Suite Teardown         Close All Connections

*** Variables ***
${HOST}                xxx.xx.xx.xxx
${USERNAME}            xxxxxx
${PASSWORD}            xxxxxxx


*** Test Cases ***
Execute Command And Verify Output
    [Documentation]    Execute Command can be used to run commands on the remote machine.
    ...                The keyword returns the standard output by default.
    ${output}=         Execute Command    echo Hello SSHLibrary!
    ${modtest}=         Execute Command   modetest -D a047035620.v_mix -s 41:3840x2160-30@BG24 &
    ${vcugst}=     Execute Command      /media/card/bin/gst_app /xxx/xxx/xxx/input.cfg
    Log Many           ${vcugst}
    Should Be Equal    ${output}          Hello SSHLibrary!

*** Keywords ***
Open Connection And Log In
   Open Connection     ${HOST}
   Login               ${USERNAME}        ${PASSWORD}

