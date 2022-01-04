Write-Output 'Costum PowerShell Profile in effect'
Add-Content -Path 'e:\praxis-academy\Remote-signed.ps1' -Value "[ZoneTransfer]`nZoneId=3" -Stream 'Zone.Identifier'
Clear-Content -Path 'e:\praxis-academy\Remote-signed.ps1' -Stream 'Zone.Identifier'
PowerShell.exe -Command "& {Start-Process PowerShell.exe -ArgumentList '-ExecutionPolicy Bypass -File ""Remote-signed.ps1""' -Verb RunAs}"
if (([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{Write-Output 'Running as Administrator!'}
else
{Write-Output 'Running Limited!'}
Pause