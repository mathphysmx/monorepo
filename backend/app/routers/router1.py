from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_status() -> dict:
    """Return the current status of the router1 service."""
    return {"status": "ok", "router": "router1"}


@router.get("/items/{item_id}")
async def get_item(item_id: int) -> dict:
    """Return an item by its ID."""
    return {"item_id": item_id, "name": f"Item {item_id}"}
