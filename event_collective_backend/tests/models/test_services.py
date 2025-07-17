from app.models.service import Service

def test_service_model_fields():
    service = Service(id=1, name="Photography", description="Pro service", price=150.00)
    assert service.name == "Photography"
    assert service.price == 150.00
