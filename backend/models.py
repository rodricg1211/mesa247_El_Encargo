from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Localizacion(Base):
    __tablename__ = "localizacion"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    city = Column(String(100))
    qr_code = Column(String(100), unique=True)

class EntradaCola(Base):
    __tablename__ = "entrada_cola"
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer)
    name = Column(String(100))
    phone = Column(String(20))
    party_size = Column(Integer)
    status = Column(String(20), default="esperando")
    joined_at = Column(DateTime, default=datetime.utcnow)
    called_at = Column(DateTime, nullable=True)

engine = create_engine("sqlite:///./cola.db")
Base.metadata.create_all(engine)