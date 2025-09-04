import requests

def test_get_user(api_base_url):
    response = requests.get(f"{api_base_url}/users")
    assert response.status_code == 200
    assert response.json()[0].get("name") == "Leanne Graham"
