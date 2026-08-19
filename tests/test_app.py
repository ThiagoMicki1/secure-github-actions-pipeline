from app.app import create_app


def test_home_endpoint_returns_ok():
    client = create_app().test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_health_endpoint_returns_healthy():
    client = create_app().test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_security_controls_endpoint_lists_pipeline_controls():
    client = create_app().test_client()

    response = client.get("/security-controls")
    controls = response.get_json()["controls"]

    assert response.status_code == 200
    assert "secrets-scanning" in controls
    assert "container-scanning" in controls
