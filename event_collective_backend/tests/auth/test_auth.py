import pytest
from httpx import AsyncClient
from fastapi import status
from main import app  # noqa: F401

@pytest.mark.asyncio
async def test_login_success(async_client: AsyncClient):
    response = await async_client.post("/api/auth/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.asyncio
async def test_login_failure(async_client: AsyncClient):
    response = await async_client.post("/api/auth/login", json={"username": "wrong", "password": "wrong"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
