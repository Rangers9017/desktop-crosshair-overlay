# Desktop Crosshair Overlay

A tiny desktop utility that draws a red dot at the center of the primary display.

## Features

- Transparent, always-on-top overlay
- Mouse clicks pass through the overlay
- A system tray menu provides a clean way to exit
- Uses the primary display

## Requirements

- Python 3.9+
- PyQt5

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

Run:

```bash
python cross.py
```

Right-click the tray icon and choose **Çıkış** to close it. If the system has no tray, stop the process from the terminal with `Ctrl+C`.

## Türkçe

Birincil ekranın ortasında kırmızı bir nokta gösteren küçük bir masaüstü aracıdır. Saydam pencere fare tıklamalarını alttaki uygulamalara geçirir. Kapatmak için sistem tepsisindeki simgeye sağ tıklayıp **Çıkış** seçeneğini kullanın.

## Notes

The overlay is centered on the primary display. It does not interact with game processes or automate input.
