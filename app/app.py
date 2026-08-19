from __future__ import annotations

import os
from datetime import datetime, timezone

from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["APP_NAME"] = "Secure GitHub Actions Pipeline"
    app.config["APP_VERSION"] = os.getenv("APP_VERSION", "1.0.0")

    @app.get("/")
    def index():
        return jsonify(
            {
                "app": app.config["APP_NAME"],
                "message": "Secure CI/CD learning lab",
                "status": "ok",
            }
        )

    @app.get("/health")
    def health():
        return jsonify(
            {
                "status": "healthy",
                "checked_at": datetime.now(timezone.utc).isoformat(),
            }
        )

    @app.get("/security-controls")
    def security_controls():
        return jsonify(
            {
                "controls": [
                    "unit-tests",
                    "secrets-scanning",
                    "sast",
                    "dependency-review",
                    "dependabot",
                    "container-scanning",
                    "least-privilege-actions",
                ]
            }
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
