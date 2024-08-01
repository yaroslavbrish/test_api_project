import pytest
from endpoints.authorize import Authorize
from endpoints.get_meme import GetMeme
from endpoints.add_meme import AddMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture()
def get_authorize():
    return Authorize()


@pytest.fixture
def get_meme_endpoint():
    return GetMeme()


@pytest.fixture
def create_meme_endpoint():
    return AddMeme()


@pytest.fixture
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def authorization_token(get_authorize):
    body = {
        "name": "brishar"
    }
    get_authorize.create_token(body=body)
    yield get_authorize.token


@pytest.fixture
def new_meme_id(create_meme_endpoint,
                authorization_token,
                delete_meme_endpoint):
    payload = {
        "text": "Test Mem",
        "url": "http://example.com/test.jpg",
        "tags": ["tag1", "tag2", "tag3"],
        "info": {
            "lol": 1,
            "lmao": 2,
            "rofl": 3,
            "omg": 4
        }
    }
    # Creating a new meme
    create_meme_endpoint.create_meme(
        body=payload,
        headers={'Authorization': f'{authorization_token}'}
    )
    meme_id = create_meme_endpoint.response.json()["id"]
    # Returning meme ID for using it in tests
    yield meme_id
    # Deleting meme after test execution is finished
    delete_meme_endpoint.delete_meme(
        meme_id,
        headers={'Authorization': f'{authorization_token}'}
    )
