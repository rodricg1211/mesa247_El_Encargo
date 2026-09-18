import { useEffect, useState } from "react";
import axios from "axios";

export default function VistaAnfitrion({ locationId }: { locationId: number }) {
  const [cola, setCola] = useState<any[]>([]);

  const cargarCola = async () => {
    const res = await axios.get(`http://localhost:8000/queue/${locationId}`);
    setCola(res.data);
  };

  useEffect(() => {
    cargarCola();
    const intervalo = setInterval(cargarCola, 8000);
    return () => clearInterval(intervalo);
  }, []);

  const llamar = async (id: number) => {
    await axios.patch(`http://localhost:8000/queue/${id}/call`);
    cargarCola();
  };

  return (
    <div>
      {cola.map(c => (
        <div key={c.id}>
          {c.name} — {c.party_size} pers. — {c.status}
          <button onClick={() => llamar(c.id)}>Llamar</button>
        </div>
      ))}
    </div>
  );
}