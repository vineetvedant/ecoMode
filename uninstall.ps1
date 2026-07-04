param(
  [ValidateSet("codex", "claude", "vscode", "all")]
  [string]$Target = "codex"
)

$ErrorActionPreference = "Stop"

function Remove-EcoModePath {
  param([string]$Path)
  if (Test-Path -LiteralPath $Path) {
    Remove-Item -LiteralPath $Path -Recurse -Force
    Write-Host "removed: $Path"
  } else {
    Write-Host "not found: $Path"
  }
}

$CodexBase = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$ClaudeBase = if ($env:CLAUDE_HOME) { $env:CLAUDE_HOME } else { Join-Path $HOME ".claude" }

switch ($Target) {
  "codex" { Remove-EcoModePath (Join-Path $CodexBase "skills/ecomode") }
  "claude" { Remove-EcoModePath (Join-Path $ClaudeBase "skills/ecomode") }
  "vscode" { Remove-EcoModePath (Join-Path (Get-Location) ".github/skills/ecomode") }
  "all" {
    Remove-EcoModePath (Join-Path $CodexBase "skills/ecomode")
    Remove-EcoModePath (Join-Path $ClaudeBase "skills/ecomode")
    Remove-EcoModePath (Join-Path (Get-Location) ".github/skills/ecomode")
  }
}
