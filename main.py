# main.py

from fastapi import FastAPI, Body
from typing import Any  # Um beliebige Datentypen im Body zu erlauben
import uvicorn

# 1. Initialisiere die FastAPI App
app = FastAPI(
    title="Simple Console Logger API",
    description="Eine sehr einfache API, die POST-Daten empfängt und in die Konsole loggt.",
    version="1.0.0",
)

# 2. Definiere den POST Endpunkt unter dem Pfad "/log"
@app.post("/log")
async def log_data_to_console(
    # Erwarte beliebige Daten im Request Body.
    # FastAPI parst automatisch JSON-Daten.
    # Body(...) bedeutet, dass der Body erforderlich ist.
    payload: Any = Body(...)
):
    """
    Nimmt beliebige Daten (vorzugsweise JSON) per POST auf /log entgegen
    und gibt diese in der Konsole aus, auf der der uvicorn Server läuft.
    """
    print("---------- POST Request auf /log empfangen ----------")
    print("Empfangene Daten:")
    print(payload)  # Gib den geparsten Body aus
    print("----------------------------------------------------")

    # 3. Gib eine einfache Bestätigung an den Client zurück
    return {"status": "success", "message": "Daten erfolgreich empfangen und in der Konsole geloggt."}

# 4. Optional: Ein einfacher GET Endpunkt auf der Wurzel ("/"), um zu testen, ob die API läuft
@app.get("/")
async def read_root():
    """
    Ein einfacher GET-Endpunkt zur Überprüfung, ob die API online ist.
    """
    return {"message": "Hallo! Die Simple Logger API ist bereit. Sende POST-Requests an /log."}

# Hinweis: Der folgende Block wird nur benötigt, wenn du die Datei direkt
# mit `python main.py` ausführen möchtest. Wenn du `uvicorn main:app` verwendest,
# ist dieser Block nicht notwendig, schadet aber auch nicht.
# if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)
