*** Settings ***
Documentation     tutorial resource file

# import of RobotFramework AIO configuration managment
# coming soon: # Library    RobotFramework_TestsuitesManagement    WITH NAME    tm
Library    RobotFramework_Testsuites    WITH NAME    tm

# import of Python keyword library e.g. to support printing out further details about variables
Library    ./testlibrary.py


*** Variables ***

# --------------------------------------------------------------------------------------------------------------
# several scalars

${ABC}    ABC

${var_01}    ABC
${var_02}    "ABC"
${var_03}    ${ABC}
${var_04}    123
${var_05}    "123"
${var_06}    ${123}
${var_07}    4.56
${var_08}    "4.56"
${var_09}    ${4.56}
${var_10}    True
${var_11}    "True"
${var_12}    ${True}
${var_13}    False
${var_14}    "False"
${var_15}    ${False}
${var_16}    None
${var_17}    "None"
${var_18}    ${None}

# --------------------------------------------------------------------------------------------------------------
# a list

@{var_list}    ${var_01}
...            ${var_02}
...            ${var_03}
...            ${var_04}
...            ${var_05}
...            ${var_06}
...            ${var_07}
...            ${var_08}
...            ${var_09}
...            ${var_10}
...            ${var_11}
...            ${var_12}
...            ${var_13}
...            ${var_14}
...            ${var_15}
...            ${var_16}
...            ${var_17}
...            ${var_18}

# additional variables containing indices for accessing single elements of the list

${index_as_string}    5
${index_as_integer}   ${5}


# --------------------------------------------------------------------------------------------------------------
# a dictionary

&{var_dict}    key_01=${var_01}
...            key_02=${var_02}
...            key_03=${var_03}
...            key_04=${var_04}
...            key_05=${var_05}
...            key_06=${var_06}
...            key_07=${var_07}
...            key_08=${var_08}
...            key_09=${var_09}
...            key_10=${var_10}
...            key_11=${var_11}
...            key_12=${var_12}
...            key_13=${var_13}
...            key_14=${var_14}
...            key_15=${var_15}
...            key_16=${var_16}
...            key_17=${var_17}
...            key_18=${var_18}

# additional variable containing the name of a key

${key_as_string}    key_06

# --------------------------------------------------------------------------------------------------------------
# initialization of variables for command line tests in tutorial-04

${cmdline_var_1}    ${None}
${cmdline_var_2}    ${None}
${cmdline_var_3}    ${None}
${cmdline_var_4}    ${None}
${cmdline_var_5}    ${None}
${cmdline_var_6}    ${None}
${cmdline_var_7}    ${None}

