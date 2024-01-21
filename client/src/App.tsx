import { useEffect, useState } from 'react';
import './App.css'

const ws:WebSocket = new WebSocket("ws://127.0.0.1:8000/ws");
type AllMsgType = string[];

function App() {
  const [msg, setMsg] = useState("")
  const [allMsg, setAllMsg] = useState<AllMsgType>([])
  const [loading,setLoading] = useState<boolean>(false)

  const submitHandler = async () => {
    await setAllMsg(prevAllMsg => [...prevAllMsg, `You : ${msg}`]);
    await ws.send(`${msg}`)
    setLoading(true)
  }
  useEffect(() => {
    ws.onmessage = async function (event) {
      console.log(event.data)
      await setAllMsg(prevAllMsg => [...prevAllMsg, event.data]);
      setLoading(false)
      
    };

    // Cleanup function if needed
    return () => {
      ws.onmessage = null;
    };
  }, [ws]);

  return (
    <>
      <div style={{display:'flex',flexDirection:'column',width:"20%",gap:"20px"}}>
      <textarea value={msg} onChange={(e)=>{setMsg(e.target.value)}}/>
      <button onClick={submitHandler}>Send</button>
      </div>
   
      {
        allMsg.map((data:String, index:number) => {
          return <pre style={{width:'20%',whiteSpace: "pre-wrap"}} key={index} >{data}</pre>
        })
      }
      {loading&&<p>Loading...</p>}
    </>
  )
}

export default App
