"""Tests for the router1 endpoints."""

import pytest
import httpx
from httpx import ASGITransport

from app.main import app


@pytest.fixture
async def client():
    """Async HTTP client wired to the FastAPI application."""
    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class TestGetStatus:
    """Tests for GET /router1/ status endpoint."""

    async def test_returns_ok_status(self, client: httpx.AsyncClient):
        """Verify the status endpoint returns 200 with expected payload."""
        # Arrange — client is ready via fixture

        # Act
        response = await client.get("/router1/")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["router"] == "router1"


class TestGetItem:
    """Tests for GET /router1/items/{item_id} endpoint."""

    @pytest.mark.parametrize(
        "item_id, expected_name",
        [
            (1, "Item 1"),
            (42, "Item 42"),
            (999, "Item 999"),
        ],
        ids=["item-1", "item-42", "item-999"],
    )
    async def test_returns_item_by_id(
        self, client: httpx.AsyncClient, item_id: int, expected_name: str
    ):
        """Verify the items endpoint returns the correct item for a given ID."""
        # Arrange — parameters provided via parametrize

        # Act
        response = await client.get(f"/router1/items/{item_id}")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["item_id"] == item_id
        assert data["name"] == expected_name
