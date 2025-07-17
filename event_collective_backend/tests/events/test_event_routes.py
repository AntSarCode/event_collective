import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_list_events(async_client: AsyncClient):
    response = await async_client.get("/api/events/")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
