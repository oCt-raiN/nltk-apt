import React, { useState } from "react";
import Editor from "@monaco-editor/react";
import axios from "axios";

export default function App() {
  const [code, setCode] = useState("");
  const [ghost, setGhost] = useState("");

  const handleEditorChange = (value) => {
    setCode(value);
    // Call backend for suggestion
    axios
      .post("http://localhost:8000/predict", { code: value })
      .then((res) => setGhost(res.data.suggestion))
      .catch(() => setGhost(""));
  };

  return (
    <div style={{ height: "100vh", width: "100vw" }}>
      <h2>Code Ghost Suggest (Copilot-style)</h2>
      <div style={{ position: "relative" }}>
        <Editor
          height="60vh"
          defaultLanguage="python"
          value={code}
          onChange={handleEditorChange}
          options={{ fontSize: 16 }}
        />
        {/* Ghost text overlay */}
        {ghost && (
          <div
            style={{
              position: "absolute",
              top: 60,
              left: 60,
              color: "#aaa",
              pointerEvents: "none",
              fontFamily: "monospace",
              fontSize: 16,
              whiteSpace: "pre-wrap",
              opacity: 0.7,
            }}
          >
            {ghost.replace(code, "")}
          </div>
        )}
      </div>
    </div>
  );
}
