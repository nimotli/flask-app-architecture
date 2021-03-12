from werkzeug.security import check_password_hash

def test_register_valid_data(testClient,newUser):
    response = testClient.post('/auth/register', json=newUser.to_json())
    assert response.status_code == 200
    assert response.get_json()["username"] == newUser.username
    assert check_password_hash(response.get_json()["password"],newUser.password)
    assert response.get_json()["email"] == ""
    
