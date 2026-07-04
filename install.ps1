param(
  [ValidateSet("codex", "claude", "vscode", "all")]
  [string]$Target = "codex",
  [string]$Dest = "",
  [switch]$Force
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSCommandPath

function Copy-EcoModeSkill {
  param([string]$Destination)

  if ((Test-Path -LiteralPath $Destination) -and -not $Force) {
    Write-Host "exists: $Destination"
    Write-Host "Use -Force to overwrite."
    throw "Destination exists"
  }

  $Parent = Split-Path -Parent $Destination
  New-Item -ItemType Directory -Force -Path $Parent | Out-Null
  if (Test-Path -LiteralPath $Destination) {
    Remove-Item -LiteralPath $Destination -Recurse -Force
  }
  New-Item -ItemType Directory -Force -Path $Destination | Out-Null

  Get-ChildItem -LiteralPath $Root -Force |
    Where-Object { $_.Name -notin @(".git") -and $_.Extension -ne ".zip" } |
    Copy-Item -Destination $Destination -Recurse -Force

  Write-Host "installed: $Destination"
}

function Install-Codex {
  $Base = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
  $Destination = if ($Dest) { $Dest } else { Join-Path $Base "skills/ecomode" }
  Copy-EcoModeSkill -Destination $Destination
}

function Install-Claude {
  $Base = if ($env:CLAUDE_HOME) { $env:CLAUDE_HOME } else { Join-Path $HOME ".claude" }
  $Destination = if ($Dest) { $Dest } else { Join-Path $Base "skills/ecomode" }
  Copy-EcoModeSkill -Destination $Destination
}

function Install-VSCode {
  $Destination = if ($Dest) { $Dest } else { Join-Path (Get-Location) ".github/skills/ecomode" }
  Copy-EcoModeSkill -Destination $Destination
}

switch ($Target) {
  "codex" { Install-Codex }
  "claude" { Install-Claude }
  "vscode" { Install-VSCode }
  "all" {
    Install-Codex
    Install-Claude
    Install-VSCode
  }
}

Write-Host "Restart your agent so it reloads skills."
