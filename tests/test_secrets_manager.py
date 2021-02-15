import pytest
import secrets_manager


def test_read_secrets_has_api_key():
    path = '../alpha_vantage_secrets.json'
    secrets = secrets_manager.read_secrets(path)
    assert secrets.get("api_key") is not None
