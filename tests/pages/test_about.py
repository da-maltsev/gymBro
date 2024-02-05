def test_ok(client):
    got = client.get("/about")

    assert got.status_code == 200
    assert got.template.name == "about.html"
    assert "text/html" in got.headers["Content-Type"]
