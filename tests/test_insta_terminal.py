from simple_package import insta_terminal


def test_get_user_info():
    user = "instagram"
    info = insta_terminal.get_user_info(user)
    assert info is not None
    assert info["username"] == user
    assert "followers" in info
