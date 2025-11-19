# 🗂️ Agenda - App per Appunti

Questa piccola applicazione mostra un'Agenda desktop realizzata con Python e `pywebview`, con interfaccia HTML/CSS/JS. 
Il progetto è pensato per essere facilmente reso un `.exe` usando PyInstaller.

**Stato:** Funzionante. Tuttavia è un progetto che potrà subire ncora delle modifiche, perciò è da considerare inattendibile per un utilizzo costante.

**Linguaggi & tecnologie:**
- **Python**: logica dell'app (`main.py`, `API.py`, `ripristina.py`)
- **HTML / CSS / JavaScript**: interfaccia utente (`index.html`, `form.html`, `style.css`, `addNota.js`, `bottoni.js`, `graficaBacheca.js`)
- **CSV**: persistenza semplice (`agenda.csv`)
- **pywebview**: integrazione GUI webview
- **PyInstaller**: per creare l`.exe` standalone

**File principali**
- `main.py` : entry point dell'app
- `API.py`  : API JavaScript <-> Python
- `ripristina.py` : carica `agenda.csv` all'avvio
- `index.html`, `form.html`, `style.css`, `addNota.js`, `bottoni.js`, `graficaBacheca.js` : UI
- `agenda.csv` : file dati (può essere creato vuoto se mancante)

**Come creare un `.exe` (Windows - PowerShell)**

Installa le dipendenze necessarie:
```powershell
pip install pyinstaller pywebview
```

Costruisci l'eseguibile includendo i file statici:
```powershell
pyinstaller --onefile --windowed `
  --add-data "index.html;." `
  --add-data "form.html;." `
  --add-data "style.css;." `
  --add-data "addNota.js;." `
  --add-data "bottoni.js;." `
  --add-data "graficaBacheca.js;." `
  --add-data "agenda.csv;." `
  main.py
```

- Il `.exe` risultante sarà in `dist\main.exe`.
- Rimuovi `--windowed` se vuoi vedere la console per debug.

**Dipendenze principali**
- `pywebview`
- `pyinstaller` (solo per il packaging)

**Licenza & Contatti**
- Questo repository non contiene informazioni di licenza esplicite. Aggiungi una `LICENSE` se vuoi distribuirlo.
- Per domande o aiutocon la build, apri una issue o contattami direttamente.

Grazie e buon lavoro! 🚀
# lezione-python-compilazione
