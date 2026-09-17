import { useState } from "react";
import axios from "axios";

export default function RegistroComensal({ locationId }: { locationId: number }) {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [partySize, setPartySize] = useState(1);
  const [mensaje, setMensaje] = useState("");

  const enviar = async () => {
    try {
      await axios.post("http://localhost:8000/queue", {
        location_id: locationId, name, phone, party_size: partySize
      });
      setMensaje("¡Listo! Ya estás en la cola.");
      setName("");
      setPhone("");
      setPartySize(1);
    } catch {
      setMensaje("Revisa tus datos.");
    }
  };

  return (
    <div>
      <input placeholder="Nombre" value={name} onChange={e => setName(e.target.value)} />
      <input placeholder="Teléfono" value={phone} onChange={e => setPhone(e.target.value)} />
      <input type="number" value={partySize} onChange={e => setPartySize(Number(e.target.value))} />
      <button onClick={enviar}>Unirme a la cola</button>
      <p>{mensaje}</p>
    </div>
  );
}