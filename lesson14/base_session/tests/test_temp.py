import pytest

import asyncio


@pytest.mark.asyncio
async def test_get_weather(test_client):
   
    res = test_client.get("/temp", params={"lat" : 10, "lon" : 30})
    assert res.status_code == 200
    