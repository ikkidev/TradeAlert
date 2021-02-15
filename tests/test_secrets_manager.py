import pytest
import secrets_manager


def test_read_secrets_has_api_key():
    path = '../alpha_vantage_secrets.json'
    secret = secrets_manager.get_secret(path)
    assert secret.get("api_key") is not None
