Param(
    [string]$venvName = ".venv"
)

& .\$venvName\Scripts\Activate.ps1
pip install -r requirements.txt
