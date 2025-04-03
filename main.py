from flask import Flask, request
import json # Optional, um JSON hübscher auszugeben

# Erstellt eine Flask-App-Instanz
app = Flask(__name__)

# Definiert eine Route für den Endpunkt '/api'
# Diese Route akzeptiert nur POST-Anfragen ('methods=['POST']')
@app.route('/api', methods=['POST'])
def handle_post_request():
    """
    Diese Funktion wird aufgerufen, wenn eine POST-Anfrage an /api gesendet wird.
    Sie gibt die empfangenen Daten in der Konsole aus.
    """
    print("-------------------------------------------")
    print("POST-Anfrage empfangen auf /api")

    # Holt die Rohdaten aus dem Body der Anfrage
    data = request.get_data()

    # Versucht, die Daten als Text (UTF-8) zu dekodieren und auszugeben
    try:
        data_str = data.decode('utf-8')
        print("Empfangene Daten (als Text dekodiert):")
        print(data_str)

        # Optional: Versuchen, als JSON zu parsen und formatiert auszugeben
        try:
            parsed_json = json.loads(data_str)
            print("\nDaten (als JSON geparst und formatiert):")
            # json.dumps mit indent=2 sorgt für eine lesbare Ausgabe
            print(json.dumps(parsed_json, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print("\n(Daten waren kein gültiges JSON)")

    except UnicodeDecodeError:
        # Falls es kein UTF-8 Text ist, gib die rohen Bytes aus
        print("Empfangene Daten (konnten nicht als UTF-8 dekodiert werden, rohe Bytes):")
        print(data)

    print("-------------------------------------------")

    # Sendet eine einfache Erfolgsantwort an den Client zurück
    # Der Statuscode 200 bedeutet "OK"
    return "Daten empfangen und in der Konsole geloggt.", 200

# Standard Python-Einstiegspunkt: Führt den Code nur aus,
# wenn das Skript direkt gestartet wird (nicht wenn es importiert wird)
if __name__ == '__main__':
    print("Flask Server wird gestartet...")
    # Startet den Entwicklungs-Webserver
    # host='0.0.0.0' macht den Server im lokalen Netzwerk erreichbar
    # port=5000 ist der Standard-Port für Flask
    # debug=True aktiviert den Debug-Modus (automatische Neu-Ladung bei Änderungen, detailliertere Fehler)
    # ACHTUNG: debug=True NICHT in einer produktiven Umgebung verwenden!
    app.run(host='0.0.0.0', port=5000, debug=True)
