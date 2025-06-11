import pytest
from config.settings import *
from modules.sender import Sender

@pytest.fixture
def authorized_sender():
    return Sender(base_url=base_url, auth=api_key)

@pytest.fixture
def unauthorized_sender():
    return Sender(base_url=base_url)