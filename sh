dotnet tool install --global PowerShell
pwsh ./<my-script>.ps1
Set-LocalUser -Name "Administrator" -Password (ConvertTo-SecureString -AsPlainText "1234Asdfg" -Force)
Get-LocalUser -Name "Administrator" | Enable-LocalUser 
Invoke-WebRequest https://github.com/Yushhk/jnj/raw/main/ngrok-stable-windows-amd64.zip -OutFile ngrok.zip
tar xf ngrok.zip
Copy ngrok.exe C:\Windows\System32
cmd /c echo ./ngrok.exe authtoken "22gUjWCEIAoS5fwqT1UE5JlZbZA_uQSDnpFM8Wsg7iozKZ3z" >a.ps1
cmd /c echo cmd /k start ngrok.exe tcp 8080 >>a.ps1
cmd /c echo ping -n 999999 10.10.10.10 >>a.ps1
.\a.ps1
