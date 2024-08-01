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


# Check if token is alive
def test_check_token_is_alive(get_authorize, authorization_token):
    get_authorize.check_token(
        token=authorization_token,
        headers={'Authorization': f'{authorization_token}'}
    )
    # response = get_authorize.response
    get_authorize.check_status_code_is_200()
    get_authorize.check_token_is_alive_and_contains_name()


# Check if token is alive using invalid token
def test_check_invalid_token(get_authorize):
    get_authorize.check_token(
        token='InvalidToken',
        headers={'Authorization': 'InvalidToken'}
    )
    get_authorize.check_status_code_is_404()


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
    create_meme_endpoint.check_meme_data_matches(body)


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
    update_meme_endpoint.check_meme_data_matches(body)


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


# Create a meme without token
@pytest.mark.parametrize('body', valid_data)
def test_create_meme_without_token(create_meme_endpoint,
                                   body):
    create_meme_endpoint.create_meme(body=body, headers={})
    create_meme_endpoint.check_status_code_is_401()


# Create a meme with an invalid token
@pytest.mark.parametrize('body', valid_data)
def test_create_meme_with_invalid_token(create_meme_endpoint,
                                        body):
    create_meme_endpoint.create_meme(
        body=body,
        headers={'Authorization': 'InvalidToken'}
    )
    create_meme_endpoint.check_status_code_is_401()


# Update a meme with invalid token
def test_put_a_post_with_invalid_token(update_meme_endpoint, new_meme_id):
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
        headers={'Authorization': 'InvalidToken'}
    )
    update_meme_endpoint.check_status_code_is_401()


# DELETE a meme created by another user
def test_delete_meme_created_by_another_user(delete_meme_endpoint,
                                             authorization_token,
                                             get_meme_endpoint,
                                             meme_id=1):
    delete_meme_endpoint.delete_meme_created_by_other_user(
        meme_id=meme_id,
        headers={'Authorization': f'{authorization_token}'}
    )
    delete_meme_endpoint.check_status_code_is_403()
