import React, { useEffect, useState } from "react";
import "./App.css";
import { v4 as uuid } from "uuid";

const client_id: string = uuid();
const ws: WebSocket = new WebSocket(`ws://127.0.0.1:8000/ws/${client_id}`);
type AllMsgType = string[];

interface TextPrinterProps {
  text: string;
}

const TextPrinter: React.FC<TextPrinterProps> = ({ text }) => {
  const [printedText, setPrintedText] = useState<String>("");

  useEffect(() => {
    console.log(text);
    const words = text.split(" ");
    console.log(words);

    let currentIndex = 0;
    const intervalId = setInterval(() => {
      setPrintedText((prevText) => prevText + " " + words[currentIndex]);
      currentIndex += 1;
      if (currentIndex === words.length - 1) {
        clearInterval(intervalId);
      }
    }, 300); // Adjust the delay (in milliseconds) as needed

    return () => clearInterval(intervalId); // Cleanup on component unmount
  }, [text]);

  return <div>{printedText}</div>;
};
function App() {
  const [msg, setMsg] = useState("");
  const [allMsg, setAllMsg] = useState<AllMsgType>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [recording, setRecording] = useState<boolean>(false);

  const submitHandler = async () => {
    await setAllMsg((prevAllMsg) => [...prevAllMsg, `You : ${msg}`]);
    await ws.send(`${msg}`);
    setLoading(true);
    setMsg("");
  };

  useEffect(() => {
    ws.onmessage = async function (event) {
      let parts = event.data.split(":");
      let toSpeak = parts.slice(1).join(":");
      const value: SpeechSynthesisUtterance = new SpeechSynthesisUtterance(
        toSpeak
      );
      window.speechSynthesis.speak(value);

      await setAllMsg((prevAllMsg) => [...prevAllMsg, event.data]);
      setLoading(false);
    };

    // Cleanup function if needed
    return () => {
      ws.onmessage = null;
    };
  }, [ws]);
  const speechHandler = () => {
    if ("SpeechRecognition" in window || "webkitSpeechRecognition" in window) {
      const recognition: any = new (window.SpeechRecognition ||
        window.webkitSpeechRecognition)();
      setRecording(true);
      recognition.lang = "en-US";
      recognition.interimResults = true;

      recognition.onstart = function () {
        console.log("Speech recognition started");
      };

      recognition.onresult = async function (event: any) {
        const result = event.results[event.resultIndex];
        const transcript = result[0].transcript;

        await setMsg(transcript); // Update the state with the recognized speech
      };

      recognition.onerror = function (event: any) {
        console.error("Speech recognition error:", event.error);
        setRecording(false);
        alert(
          "Speech recognition does not work with your browser.Chrome suggested"
        );
      };

      recognition.onend = async function () {
        console.log("Speech recognition ended");
        setRecording(false);
      };

      recognition.start();
    } else {
      alert(
        "Speech recognition is not supported in your browser. Please use a supported browser."
      );
    }
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          width: "50%",
          gap: "20px",
        }}
      >
        <div style={{ width: "100%" }}>
          {allMsg.map((data: string, index: number) => {
            return (
              <pre
                style={{
                  width: "80%",
                  whiteSpace: "pre-wrap",
                  color: `${index % 2 === 0 ? "black" : "gray"}`,
                }}
                key={index}
              >
                {index % 2 === 1 ? (
                  <>
                    <TextPrinter text={data} />{" "}
                  </>
                ) : (
                  <>{data}</>
                )}
              </pre>
            );
          })}
          {loading && <p>Loading...</p>}
        </div>
        <div
          style={{
            maxWidth: "700px",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            position: "absolute",
            left: "25%",
            right: 0,
            bottom: 5,
            gap: "10px",
          }}
        >
          <textarea
            value={msg}
            onChange={(e) => {
              setMsg(e.target.value);
            }}
            style={{
              height: "150px",
              width: "90%",
              outline: "none",
              fontSize: "15px",
            }}
          />
          <div
            style={{
              width: "90%",
              display: "flex",
              justifyContent: "space-between",
            }}
          >
            <button
              onClick={speechHandler}
              style={{
                width: "40%",
                padding: "10px",
                cursor: "pointer",
                background: "red",
                fontSize: "18px",
                color: "white",
                border: "none",
                borderRadius: "30px",
              }}
            >
              {recording ? (
                "Listening"
              ) : (
                <>
                  <i className="fa-solid fa-microphone"></i>
                </>
              )}
            </button>
            <button
              onClick={submitHandler}
              style={{
                width: "40%",
                padding: "10px",
                cursor: "pointer",
                background: "green",
                fontSize: "18px",
                color: "white",
                border: "none",
                borderRadius: "30px",
              }}
            >
              Send
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
