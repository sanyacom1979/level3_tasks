import pytest
from aioresponses import aioresponses
from fastapi.testclient import TestClient
from meteo_service.config import Config
from main import app


@pytest.fixture
def test_config() -> Config:
    return Config(open_meteo_api="http://test_meteo_api.com")


@pytest.fixture
def mocked():
    with aioresponses() as m:
        yield m


@pytest.fixture
def test_client():
    return TestClient(app)
