# Mesa247 — Lista de Espera Digital (Piloto)

Prototipo funcional del flujo mínimo de lista de espera: un comensal se registra en la cola,
el anfitrión la visualiza y llama al siguiente.

## Stack
- Backend: Python + FastAPI + SQLAlchemy + SQLite
- Frontend: React + TypeScript + Vite + Axios

## Qué incluye este corte
- Registro del comensal (nombre, teléfono, cantidad de personas)
- Persistencia en base de datos
- Vista del anfitrión con la cola ordenada por hora de ingreso
- Botón para llamar al siguiente comensal
- Tests de los endpoints principales

## Qué NO incluye (fuera de alcance para este piloto)
- Notificaciones por WhatsApp
- Posición en vivo con animación
- Reportes de fin de día
- Priorización de clientes frecuentes / reordenamiento manual
- Gestión de reservas

## Cómo levantarlo (5 minutos)

### Requisitos
- Python 3.10+
- Node.js 18+

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # En Mac/Linux: source venv/bin/activate
pip install fastapi uvicorn sqlalchemy pydantic pytest httpx
python models.py               # Genera la base de datos SQLite
uvicorn main:app --reload
```
El backend queda corriendo en `http://localhost:8000`.
Documentación interactiva (Swagger) en `http://localhost:8000/docs`.

### Frontend
En otra terminal:
```bash
cd frontend
npm install
npm run dev
```
El frontend queda corriendo en `http://localhost:5173`.

### Tests
```bash
cd backend
pytest
```

## Flujo de prueba
1. Abre `http://localhost:5173`
2. Llena el formulario "Unirse a la cola" y presiona el botón
3. El comensal aparece automáticamente en "Vista del anfitrión"
4. Presiona "Llamar" y confirma que el estado cambia a "llamado"

## Endpoints
- `POST /queue` — registra un comensal
- `GET /queue/{location_id}` — devuelve la cola de un local
- `PATCH /queue/{entry_id}/call` — marca a un comensal como llamado