#!/usr/bin/env bash
set -euo pipefail

for tool in gitleaks semgrep docker trivy; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "Missing required tool: $tool"
    echo "Install it first, or run the matching GitHub Actions workflow after pushing."
    exit 1
  fi
done

mkdir -p reports/local

echo "Running Gitleaks..."
gitleaks dir . \
  --config .gitleaks.toml \
  --redact \
  --report-format json \
  --report-path reports/local/gitleaks-report.json

echo "Running Semgrep..."
semgrep scan \
  --config p/python \
  --config p/flask \
  --config p/secrets \
  --error \
  --json \
  --output reports/local/semgrep-report.json

echo "Building Docker image..."
docker build -t secure-actions-demo:local .

echo "Running Trivy image scan..."
trivy image \
  --scanners vuln \
  --pkg-types os \
  --severity HIGH,CRITICAL \
  --ignore-unfixed \
  --exit-code 1 \
  --format json \
  --output reports/local/trivy-report.json \
  secure-actions-demo:local

echo "Local security scans completed."
