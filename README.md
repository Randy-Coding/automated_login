# automated_login
uses facial recognition to sign into 1password


This project intends to use facial recognition software to recognize your face, then automatically enter your master password into
1password.

Prerequisites:

1.  You need a few libraries for this code to work. You can install them all here.:
    pip install pywinauto keyring pyinstaller


2.  You need op.exe installed. You can install it by opening up windows powershell as an administrator and running this command:
    $arch = (Get-CimInstance Win32_OperatingSystem).OSArchitecture
    switch ($arch) {
        '64-bit' { $opArch = 'amd64'; break }
        '32-bit' { $opArch = '386'; break }
        Default { Write-Error "Sorry, your operating system architecture '$arch' is unsupported" -ErrorAction Stop }
    }
    $installDir = Join-Path -Path $env:ProgramFiles -ChildPath '1Password CLI'
    Invoke-WebRequest -Uri "https://cache.agilebits.com/dist/1P/op2/pkg/v2.26.0/op_windows_$($opArch)_v2.26.0.zip" -OutFile op.zip
    Expand-Archive -Path op.zip -DestinationPath $installDir -Force
    $envMachinePath = [System.Environment]::GetEnvironmentVariable('PATH','machine')
    if ($envMachinePath -split ';' -notcontains $installDir){
        [Environment]::SetEnvironmentVariable('PATH', "$envMachinePath;$installDir", 'Machine')
    }
    Remove-Item -Path op.zip

For more information go to https://developer.1password.com/docs/cli/get-started/

3.  You need to enable command line interface with 1password to be able to enter the password. 
    To do this you can go to settings, then to developer, then scroll down to "Command-Line Interface (CLI) and make sure "Integrate with 1Password CLI" is checked off.
