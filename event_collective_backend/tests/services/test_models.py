from app.services.service import create_service
from app.schemas.service import ServiceCreate

def test_create_service_logic():
    data = ServiceCreate(name="DJ", description="Club DJ", price=300.00)
    result = create_service(data)
    assert result.name == "DJ"
    assert hasattr(result, "id")
