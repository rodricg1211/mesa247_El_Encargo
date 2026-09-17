from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_registro_sin_telefono_falla():
    r = client.post("/queue", json={"location_id": 1, "name": "Carla", "phone": "", "party_size": 2})
    assert r.status_code == 400

def test_registro_exitoso():
    r = client.post("/queue", json={"location_id": 1, "name": "Carla", "phone": "999", "party_size": 2})
    assert r.status_code == 200

def test_llamar_cambia_estado():
    r = client.post("/queue", json={"location_id": 1, "name": "Jorge", "phone": "888", "party_size": 1})
    id_creado = r.json()["id"]
    r2 = client.patch(f"/queue/{id_creado}/call")
    assert r2.json()["status"] == "llamado"