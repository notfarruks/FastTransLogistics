# ============================================================
#  download_images.ps1
#  Fetches all site images into static\img so the site is
#  fully self-hosted (no hotlinking to Pexels / flagcdn).
#  HOW TO RUN (from the project folder):
#     powershell -ExecutionPolicy Bypass -File .\download_images.ps1
#  Then commit & push.
# ============================================================
$ErrorActionPreference = "Continue"
$root   = Split-Path -Parent $MyInvocation.MyCommand.Path
$photos = Join-Path $root "static\img\photos"
$flags  = Join-Path $root "static\img\flags"
New-Item -ItemType Directory -Force -Path $photos | Out-Null
New-Item -ItemType Directory -Force -Path $flags  | Out-Null

function Get-Img($url, $dest) {
  $name = [System.IO.Path]::GetFileName($dest)
  try {
    Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing -TimeoutSec 60
    Write-Host "  ok   $name"
  } catch {
    Write-Host "  FAIL $name  ->  $($_.Exception.Message)"
  }
}

$px = "https://images.pexels.com/photos"
$photoMap = [ordered]@{
  "hero.jpg"      = "$px/9195241/pexels-photo-9195241.jpeg?auto=compress&cs=tinysrgb&w=1600"
  "service-1.jpg" = "$px/2199293/pexels-photo-2199293.jpeg?auto=compress&cs=tinysrgb&w=900"
  "service-2.jpg" = "$px/10963747/pexels-photo-10963747.jpeg?auto=compress&cs=tinysrgb&w=900"
  "service-3.jpg" = "$px/9831438/pexels-photo-9831438.jpeg?auto=compress&cs=tinysrgb&w=900"
  "service-4.jpg" = "$px/16241422/pexels-photo-16241422.jpeg?auto=compress&cs=tinysrgb&w=900"
  "gallery-1.jpg" = "$px/14005602/pexels-photo-14005602.jpeg?auto=compress&cs=tinysrgb&w=900"
  "gallery-2.jpg" = "$px/16180668/pexels-photo-16180668.jpeg?auto=compress&cs=tinysrgb&w=900"
  "gallery-3.jpg" = "$px/5213882/pexels-photo-5213882.jpeg?auto=compress&cs=tinysrgb&w=900"
  "gallery-4.jpg" = "$px/12069485/pexels-photo-12069485.jpeg?auto=compress&cs=tinysrgb&w=900"
  "gallery-5.jpg" = "$px/17229385/pexels-photo-17229385.jpeg?auto=compress&cs=tinysrgb&w=900"
  "gallery-6.jpg" = "$px/9195241/pexels-photo-9195241.jpeg?auto=compress&cs=tinysrgb&w=900"
}

Write-Host "Downloading photos -> static\img\photos"
foreach ($k in $photoMap.Keys) { Get-Img $photoMap[$k] (Join-Path $photos $k) }

$codes = @("az","ge","ru","tr","by","eu","rs","cn")
Write-Host "Downloading flags -> static\img\flags"
foreach ($c in $codes) { Get-Img "https://flagcdn.com/w320/$c.png" (Join-Path $flags "$c.png") }

Write-Host ""
Write-Host "Done. Review the images, then: git add -A; git commit -m 'Self-host images'; git push"
