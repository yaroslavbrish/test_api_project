import pytest


valid_data = [
    {
        "text": "First Meme",
        "url": "http://example.com/first.jpg",
        "tags": ["first", "meme"],
        "info": {"brishar": "just_testing"}
    }
]

invalid_data = [
    {
        "text": 11111,
        "url": "http://example.com/first.jpg",
        "tags": ["first", "meme"],
        "info": {"brishar": "just_testing"}
    }
]


# GET all memes
def test_get_all_memes(get_meme_endpoint, authorization_token):
    get_meme_endpoint.get_all_memes(
        headers={'Authorization': f'{authorization_token}'}
    )
    get_meme_endpoint.check_status_code_is_200()


# GET a meme by ID
def test_get_meme_by_id(get_meme_endpoint, new_meme_id, authorization_token):
    get_meme_endpoint.get_one_meme(
        meme_id=new_meme_id,
        headers={'Authorization': f'{authorization_token}'}
    )
    get_meme_endpoint.check_response_id_is_correct(new_meme_id)
    get_meme_endpoint.check_status_code_is_200()


# POST a new meme with VALID DATA
@pytest.mark.parametrize('body', valid_data)
def test_create_mem_with_valid_data(create_meme_endpoint,
                                    body,
                                    authorization_token):
    create_meme_endpoint.create_meme(
        body=body,
        headers={'Authorization': f'{authorization_token}'}
    )
    create_meme_endpoint.check_status_code_is_200()


# POST a new meme with INVALID DATA
@pytest.mark.parametrize('body', invalid_data)
def test_create_mem_with_invalid_data(create_meme_endpoint,
                                      body,
                                      authorization_token):
    create_meme_endpoint.create_meme(
        body=body,
        headers={'Authorization': f'{authorization_token}'}
    )
    create_meme_endpoint.check_status_code_is_400()


# PUT - update a meme
def test_put_a_post(update_meme_endpoint, new_meme_id, authorization_token):
    body = {
        "id": new_meme_id,
        "text": "Updated Test Meme",
        "url": "http://example.com/updated.jpg",
        "tags": ["updated", "meme"],
        "info": {"brishar": "just_updating"}
    }
    update_meme_endpoint.put_update_meme(
        meme_id=new_meme_id,
        body=body,
        headers={'Authorization': f'{authorization_token}'}
    )
    update_meme_endpoint.check_status_code_is_200()
    update_meme_endpoint.check_response_id_is_correct(
        update_meme_endpoint.response.json()['id']
    )


# DELETE a meme
def test_delete_meme(delete_meme_endpoint,
                     new_meme_id,
                     authorization_token,
                     get_meme_endpoint):
    delete_meme_endpoint.delete_meme(
        new_meme_id,
        headers={'Authorization': f'{authorization_token}'}
    )
    delete_meme_endpoint.check_status_code_is_200()
    delete_meme_endpoint.check_deleted_meme_is_deleted(
        new_meme_id,
        headers={'Authorization': f'{authorization_token}'}
    )
