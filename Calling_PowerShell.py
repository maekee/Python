# I am learning Django and thinking about calling PowerShell scripts behind the scenes, so its a POC for my self.
# Below are three different ways of executing PowerShell code.. these are:
# - Command only
# - Script
# - Script with arguments
# They all work the same.. just a list with elements in the right order

# example_script.ps1 just contains simple output based on optional parameters:
# param( [string]$UserName = "default_user", [string]$Title = "default_title", [string]$Tool = "default_tool" )
# "I am $GivenName, working as `"$Title`" and primarily with $Tool"

import subprocess

arg_username = "Maekee"
arg_title = "Python Padawan"
arg_tool = "PyCharm"

powershell_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
powershell_script_path = r'c:\powershell\example_script.ps1'
powershell_exepolicy = 'Bypass'
powershell_command_to_run = r'Write-Host "Hello Hejsan from Sweden"'

# Code example 1: Call PowerShell with Command

execute_powershell = [
    powershell_path,
    "-ExecutionPolicy",
    powershell_exepolicy,
    "-Command",
    powershell_command_to_run
]

result = subprocess.run(execute_powershell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout.decode('utf-8'))

# Code example 2: Call PowerShell script without parameters (using the defaults):

execute_powershell = [
    powershell_path,
    "-ExecutionPolicy",
    powershell_exepolicy,
    "-File",
    powershell_script_path
]

result = subprocess.run(execute_powershell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout.decode('utf-8'))

# Code example 3: Call PowerShell script with two out of three parameters:

execute_powershell = [
    powershell_path,
    "-ExecutionPolicy",
    powershell_exepolicy,
    "-File",
    powershell_script_path,
    "-UserName",
    arg_username,
    "-Title",
    arg_title
]

result = subprocess.run(execute_powershell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout.decode('utf-8'))


# As you see.. the same method, just different PowerShell parameter (Command vs File) with other parameters supplied in the list.
