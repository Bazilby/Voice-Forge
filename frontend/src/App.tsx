import { useEffect, useState } from "react";
import Panel from "../components/Panel";
import ToggleSwitch from  "../components/ToggleSwitch"
import ScriptTerminal from "../components/ScriptTerminal"


function App() {

  const [status, setStatus] = useState(null);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/status")
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setStatus(data);
      })
      .catch(error => {
        console.error("Backend connection failed:", error);
      });

  }, []);

  return (
    <div className="h-screen bg-black text-white p-6">

      <header className="mb-6">
        <h1 className="text-3xl font-bold tracking-widest">
          VOICE FORGE
        </h1>
      </header>

      <main className="grid grid-cols-12 gap-4">

        <Panel title="Script Terminal" className="col-span-12">

          <ScriptTerminal status={status}/>

          <button
            className="
              mt-4
              px-8
              py-3
              uppercase
              tracking-widest
              bg-zinc-800
              border
              border-zinc-600
              rounded-md
              hover-bg-zinc-700
            "
          >
            Forge
          </button>
        </Panel>
        

        <Panel title="Voice Matrix" className="col-span-4">
          Empty
        </Panel>

        <Panel title="Signal Processor" className="col-span-4">
          <ToggleSwitch label="Reverb" />
          <ToggleSwitch label="Tunnel" />
          <ToggleSwitch label="Radio" />
          <ToggleSwitch label="Equalizer" />
        </Panel>

        <Panel title="Monitor" className="col-span-4">
          Empty
        </Panel>

      </main>

    </div>
  );
}

export default App;

// import { useEffect, useState } from "react";
// import ScriptTerminal from "../components/ScriptTerminal";

// function App() {

//     const [status, setStatus] = useState("CONNECTING...");

//     useEffect(() => {

//         fetch("http://127.0.0.1:8000/status")
//             .then(response => response.json())
//             .then(data => {
//                 setStatus(JSON.stringify(data, null, 2));
//             })
//             .catch(error => {
//                 setStatus("BACKEND CONNECTION FAILED");
//                 console.error(error);
//             });

//     }, []);


//     return (
//         <div>

//             <ScriptTerminal />

//             <pre>
//                 {status}
//             </pre>

//         </div>
//     );
// }

// export default App;