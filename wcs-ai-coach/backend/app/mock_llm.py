import os
import requests
import json

# Ollama endpoint (works in Docker + local Windows)
OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://host.docker.internal:11434"
)

MODEL_NAME = "llama3.2:1b"


def call_ollama(query, context):
    context_text = "\n".join(
        [f"- {c['topic']}: {c['content']}" for c in context]
    )

    prompt = f"""
    You are an expert WEST COAST SWING technical coach.

    CRITICAL RULES:
    - Only give West Coast Swing specific technical advice
    - Always prioritize CONNECTION, COMPRESSION, and TIMING
    - Do NOT give generic dance or fitness advice (no posture, no core, no heels unless WCS relevant)
    - Use provided context as PRIMARY source of truth
    - If context is weak, still stay within WCS concepts only
    
    YOU MUST FOLLOW THIS EXACT OUTPUT FORMAT.
    - All fields must exist
    - No field can be empty
    - All lists must have at least 1 item
    - No nested objects
    - No JSON inside strings
    - No extra text outside JSON
    

    Return ONLY valid JSON:

    {{
      "issue_summary": "",
      "likely_causes": [],
      "coaching_cues": [],
      "drills": []
    }}

    Context:
    {context_text}

    User issue:
    {query}

    Focus specifically on WEST COAST SWING mechanics.
    """

    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    raw = response.json()["response"]

    try:
        return {"response": json.loads(raw)}
    except:
        # fallback if model doesn't return perfect JSON
        return {
            "response": {
                "issue_summary": raw,
                "likely_causes": [],
                "coaching_cues": [],
                "drills": []
            }
        }


def mock_response(query, context):
    print("MOCK LLM USED")
    return {
        "response": {
            "issue_summary": "Mock: timing and connection inconsistency detected",
            "likely_causes": [
                "Rushing anchor step",
                "Loss of stretch in transition"
            ],
            "coaching_cues": [
                "Slow down 5&6",
                "Wait for compression before redirect"
            ],
            "drills": [
                "Anchor timing drill",
                "Compression drill",
                "Slot walking drill"
            ]
        }
    }

def clean_output(data):
    for key in ["coaching_cues", "drills", "likely_causes"]:
        if key in data:
            cleaned = []
            for item in data[key]:
                if isinstance(item, str):
                    # remove accidental JSON strings
                    if item.startswith("{") and item.endswith("}"):
                        continue
                    cleaned.append(item)
            data[key] = cleaned
    return data

def enforce_schema(data):
    return {
        "issue_summary": data.get("issue_summary", "") or "No summary generated",
        "likely_causes": data.get("likely_causes") or ["Not enough context"],
        "coaching_cues": data.get("coaching_cues") or ["Focus on connection and timing"],
        "drills": data.get("drills") or ["Basic connection drill"]
    }

def generate_response(query, context):
    try:
        result = call_ollama(query, context)
        parsed = result.get("response", result)
        parsed = clean_output(parsed)
        parsed = enforce_schema(parsed)
        return {"response": parsed}

    except Exception as e:
        print("OLLAMA ERROR:", e)

        fallback = mock_response(query, context)
        parsed = fallback.get("response", fallback)
        parsed = clean_output(parsed)
        parsed = enforce_schema(parsed)
        return {"response": parsed}