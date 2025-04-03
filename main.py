from fastapi import FastAPI, Request
import uvicorn

# Erstelle die FastAPI-Anwendung
app = FastAPI(title="Simple POST API")

@app.get("/")
@app.head("/")
async def root_get():
    """
    Einfacher Endpunkt zum Testen, ob die API läuft.
    Unterstützt sowohl GET als auch HEAD Anfragen.
    """
    return {"status": "running", "message": "API läuft. Verwende POST, um Daten zu senden."}

@app.post("/")
async def root_post(request: Request):
    """
    Endpunkt, der POST-Anfragen annimmt und die Daten in die Konsole ausgibt.
    """
    try:
        # Versuche, die Anfrage als JSON zu interpretieren
        body = await request.json()
        print("Empfangene POST-Daten:", body)
        return {"status": "success", "message": "Daten empfangen"}
    except Exception as e:
        # Falls keine JSON-Daten gesendet wurden, versuche den Text zu lesen
        body = await request.body()
        print("Empfangene POST-Daten (kein JSON):", body)
        return {"status": "success", "message": "Daten empfangen (kein JSON erkannt)"}

# Stelle sicher, dass die API auch direkt gestartet werden kann
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
