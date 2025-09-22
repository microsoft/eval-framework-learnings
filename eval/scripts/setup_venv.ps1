Param(
    [string]$venvName = ".venv"
)

python -m venv $venvName
Write-Output "Created virtual environment: $venvName"
Write-Output "To activate: .\$venvName\Scripts\Activate.ps1"
Write-Output "Then: pip install -r requirements.txt"
