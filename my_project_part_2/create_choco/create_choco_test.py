import pytest


@pytest.mark.django_db
def test_create_choco(client):
    # TODO напишите Ваш тест здесь
    expected_response = {
        "name": "Choco"
    }

    data = {
        "name": "Choco",
        "description": "test",
        "price": 22
    }

    response = client.post("/choco_create/", data=data)
    assert response.status_code == 201
    assert response.data == expected_response

