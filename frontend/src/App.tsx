import RegistroComensal from "./RegistroComensal";
import VistaAnfitrion from "./VistaAnfitrion";

function App() {
  return (
    <div>
      <h2>Unirse a la cola</h2>
      <RegistroComensal locationId={1} />
      <h2>Vista del anfitrión</h2>
      <VistaAnfitrion locationId={1} />
    </div>
  );
}

export default App;