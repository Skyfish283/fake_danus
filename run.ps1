# Launch a run described entirely by run_config.toml.
# The package must be invoked from its parent directory, which this handles.

Set-Location (Join-Path $PSScriptRoot '..')
python -m math_agent
exit $LASTEXITCODE
