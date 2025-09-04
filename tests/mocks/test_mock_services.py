import responses
import requests

@responses.activate
def test_mocked_api():
    responses.add(
        responses.GET,
        "https://fakeapi.com/data",
        json={"key": "value"},
        status=200
    )

    response = requests.get("https://fakeapi.com/data")
    assert response.json() == {"key": "value"}