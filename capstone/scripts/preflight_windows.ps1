# Restored from PR #35; run the shared checker from any working directory.
$ErrorActionPreference = "Stop"
$PythonScript = Join-Path $PSScriptRoot "preflight_check.py"
$PythonArgs = @()

if (Get-Command python -ErrorAction SilentlyContinue) {
    $PythonCmd = "python"
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $PythonCmd = "python3"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $PythonCmd = "py"
    $PythonArgs = @("-3")
} else {
    Write-Error "Python 3.8+ is required and no Python interpreter is in PATH"
    exit 1
}

if (-not (Test-Path -LiteralPath $PythonScript -PathType Leaf)) {
    Write-Error "preflight_check.py not found at $PythonScript"
    exit 1
}

# No credentials or .env file are required.
& $PythonCmd @PythonArgs $PythonScript @args
exit $LASTEXITCODE

