def test_ok(client):
    got = client.get("/posts/1")

    assert got.status_code == 200
    assert got.template.name == "post_detail.html"
    assert "text/html" in got.headers["Content-Type"]
