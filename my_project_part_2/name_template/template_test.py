import pytest


@pytest.mark.django_db
def test_save_choco(client, name, status_code):
    # TODO напишите Ваш код здесь
    data = {
        "name": name,
        "description": "test address",
        "price": 100
    }

    response = client.post("/chocolate/create/", data=data)
    assert response.status_code == status_code
