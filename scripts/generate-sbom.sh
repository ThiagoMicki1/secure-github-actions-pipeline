#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="${1:-secure-actions-demo:local}"
OUTPUT_PATH="${2:-reports/secure-actions-demo-sbom.cdx.json}"

mkdir -p "$(dirname "$OUTPUT_PATH")"

trivy image \
  --no-progress \
  --format cyclonedx \
  --output "$OUTPUT_PATH" \
  "$IMAGE_NAME"

echo "SBOM written to: $OUTPUT_PATH"
