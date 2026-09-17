from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker
from models import engine, EntradaCola
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
Session = sessionmaker(bind=engine)

class NuevoComensal(BaseModel):
    location_id: int
    name: str
    phone: str
    party_size: int

@app.post("/queue")
def registrar(comensal: NuevoComensal):
    if not comensal.name or not comensal.phone or comensal.party_size < 1:
        raise HTTPException(400, "Faltan datos obligatorios")
    db = Session()
    nuevo = EntradaCola(**comensal.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    db.close()
    return {"id": nuevo.id, "status": nuevo.status}

@app.get("/queue/{location_id}")
def ver_cola(location_id: int):
    db = Session()
    cola = db.query(EntradaCola).filter(
        EntradaCola.location_id == location_id,
        EntradaCola.status.in_(["esperando", "llamado"])
    ).order_by(EntradaCola.joined_at).all()
    db.close()
    return cola

@app.patch("/queue/{entry_id}/call")
def llamar(entry_id: int):
    db = Session()
    entrada = db.query(EntradaCola).filter(EntradaCola.id == entry_id).first()
    if not entrada:
        db.close()
        raise HTTPException(404, "No encontrado")
    entrada.status = "llamado"
    entrada.called_at = datetime.utcnow()
    db.commit()
    db.close()
    return {"id": entry_id, "status": "llamado"}