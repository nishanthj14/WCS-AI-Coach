import { useState } from "react";

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    setLoading(true);
    setResult(null);

    try {
      const res = await fetch("http://localhost:8000/api/coach", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({ text })
      });

      const data = await res.json();
      setResult(data.response);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div style={styles.page}>

      <div style={styles.container}>
        <h1 style={styles.title}>WCS AI Coach</h1>
        <p style={styles.subtitle}>Get instant feedback on your dancing</p>

        <textarea
          style={styles.textarea}
          placeholder="Describe your issue... (e.g. I rush my anchor and lose connection)"
          onChange={(e)=>setText(e.target.value)}
        />

        <button style={styles.button} onClick={submit}>
          Analyze My Dancing
        </button>

        {loading && <Loader />}

        {result && (
          <div style={styles.grid}>
            <Card title="Issue Summary" items={[result.issue_summary]} />
            <Card title="Likely Causes" items={result.likely_causes} />
            <Card title="Coaching Cues" items={result.coaching_cues} />
            <Card title="Drills" items={result.drills} />
          </div>
        )}
      </div>
    </div>
  );
}

function Card({ title, items }) {
  const safeItems = Array.isArray(items) ? items : [];
  return (
    <div style={styles.card}>
      <h2 style={styles.cardTitle}>{title}</h2>

      <ul style={styles.list}>
        {safeItems.map((item, i) => (
          <li key={i}>
            {typeof item === "object"
              ? item.name || JSON.stringify(item)
              : item}
          </li>
        ))}
      </ul>
    </div>
  );
}

function Loader() {
  return (
    <div style={styles.loader}>
      Analyzing your movement...
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    backgroundColor: "#0b1220",
    color: "white",
    display: "flex",
    justifyContent: "center",
    padding: "40px"
  },
  container: {
    width: "100%",
    maxWidth: "900px"
  },
  title: {
    fontSize: "36px",
    fontWeight: "bold"
  },
  subtitle: {
    color: "#9ca3af",
    marginBottom: "20px"
  },
  textarea: {
    width: "100%",
    padding: "15px",
    borderRadius: "10px",
    border: "1px solid #374151",
    backgroundColor: "#111827",
    color: "white",
    marginBottom: "10px"
  },
  button: {
    padding: "10px 20px",
    backgroundColor: "#2563eb",
    border: "none",
    borderRadius: "10px",
    color: "white",
    cursor: "pointer",
    marginBottom: "20px"
  },
  loader: {
    marginTop: "20px",
    color: "#9ca3af"
  },
  grid: {
    display: "grid",
    gap: "15px",
    marginTop: "20px"
  },
  card: {
    backgroundColor: "#111827",
    padding: "20px",
    borderRadius: "12px",
    boxShadow: "0 4px 10px rgba(0,0,0,0.3)"
  },
  cardTitle: {
    color: "#60a5fa",
    marginBottom: "10px"
  },
  list: {
    paddingLeft: "20px"
  }
};