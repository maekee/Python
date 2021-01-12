# I am learning Django and thinking about calling PowerShell scripts behind the scenes, so its a POC for my self.
# Below are three different ways of executing PowerShell code.. these are:
# - Command only
# - Script
# - Script with arguments
# They all work the same.. just a list with elements in the right order

# example_script.ps1 just contains simple output based on optional parameters:
# param( [string]$UserName = "default_user", [string]$Title = "default_title", [string]$Tool = "default_tool" )
# "I am $UserName, working as `"$Title`" and primarily with $Tool"

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

# Also created a function in python that does this:

def get_userinformation(username=None, title=None, tool=None):
    """Function returns a custom message if (named) arguments are supplied

    Args:
        username (str): Optional UserName to be printed
        title (str): Optional Title to be printed
        tool (str): Optional favourite tool to be printed


    Returns:
        A string based on arguments to function

    Examples:
        >>> get_userinformation(username='Maekee')
        'I am Maekee, working as "default_title" and primarily with default_tool'

        >>> get_userinformation(username='Maekee', title='Technician', tool='PyCharm')
        'I am Maekee, working as "Technician" and primarily with PyCharm'

    Raises:
        TimeoutExpired: If called PowerShell script does not return stdout/stderr within 10 seconds
    """
    import subprocess

    powershell_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
    powershell_script_path = r'c:\powershell\example_script.ps1'
    powershell_exepolicy = 'Bypass'

    execute_powershell = [
        powershell_path,
        "-ExecutionPolicy",
        powershell_exepolicy,
        "-File",
        powershell_script_path,
    ]

    if username:
        execute_powershell.append('-UserName')
        execute_powershell.append(username)

    if title:
        execute_powershell.append('-Title')
        execute_powershell.append(title)

    if tool:
        execute_powershell.append('-Tool')
        execute_powershell.append(tool)

    result = subprocess.run(
        execute_powershell,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=10
    )
    if result.returncode == 0:
        return result.stdout.decode('utf-8').strip()
    else:
        return result.stderr.decode('utf-8').strip()

# If you want to make PowerShell script parameters mandatory, the Mandatory parameter attribute will cause PowerShell to interactively ask
# the user for the value and wait... this causes the Python function to stop responding. I added the timeout=10 (seconds) argument to subprocess
# to exit the script. But a better way if you can edit the PowerShell-script is to skip the Mandatory flag and instead use:
# [string]$UserName = $(throw "UserName is mandatory, please provide a value.'")
# this will cause PS to throw an exception and the Python will catch it.
