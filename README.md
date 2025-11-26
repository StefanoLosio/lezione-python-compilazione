# 🗂️ Agenda - App per Appunti

Questa piccola applicazione mostra un'Agenda desktop realizzata con Python e `pywebview`, con interfaccia HTML/CSS/JS. 
Il progetto è pensato per essere facilmente reso un `.exe` usando PyInstaller.

**Stato:** Funzionante. Tuttavia è un progetto che potrà subire ancora delle modifiche, perciò è da considerare inattendibile per un utilizzo costante.

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

## ⚖️ Licenza

Distribuito sotto licenza **[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it)**  
> È consentito condividere il progetto con attribuzione, ma **non è consentito modificarlo o usarlo a fini commerciali**.

## 📬 Contatti

Per qualsiasi domanda o segnalazione:  
- ✉️ **mail@gabrielecocchetti.it**  
- ✉️ **stefanolosio2008@gmail.com**
- ✉️ **michelequaini016@gmail.com**
  

## ⚠️ Avvertenza

Come precedentemente specificato,
questo progetto è **in costante sviluppo**.  
Tutti i contenuti sono da considerarsi **non definitivi** e **non destinati a un riutilizzo personale o professionale**.