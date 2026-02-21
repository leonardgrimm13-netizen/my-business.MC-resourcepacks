# Image/GIF moderation checker (offline + optional APIs)

This project scans **images and GIFs** and returns a simple verdict: **OK** or **NOT_OK**.

It combines:
- pHash allowlist/blocklist (fast cache; can auto-learn)
- OCR (offline, via Tesseract)
- NudeNet (offline)
- OpenNSFW2 (offline)
- YOLO weapons (offline)
- Optional APIs: OpenAI Moderation, Sightengine

## Quick start (Windows)

1) Create a venv

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies

```powershell
pip install -r requirements.txt
```

3) Configure

Copy `.env.example` to `.env` and fill in optional API keys.

4) Run

```powershell
python moderate_image.py "C:\path\to\image.png"
python moderate_image.py "C:\path\to\folder"
python moderate_image.py "https://example.com/image.jpg"
```

## OCR notes (Tesseract)

- Install Tesseract for Windows.
- If it isn't in PATH, set `TESSERACT_CMD` in `.env` to the full path.

## Folder scan output

At the end of a folder scan the script prints a summary list like:

```
file1.png: OK
file2.gif: NOT_OK
...
```

## Security

Do **NOT** commit or share your `.env` – it can contain API keys.


## Output control via .env

You can control how many scores are printed using `.env`:
- `SCORE_VERBOSE=1` prints all keys for all engines.
- `SCORE_MAX_KEYS=8` limits non-Sightengine keys.
- `SIGHTENGINE_SCORE_MODE=compact|full|keys` controls Sightengine output.
- `SIGHTENGINE_SCORE_KEYS=...` is used when mode=`keys`.
