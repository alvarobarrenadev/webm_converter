### VP9 (más rápido, buena compresión):
``` bash
ffmpeg -i input.mp4 -c:v libvpx-vp9 -b:v 0 -crf 30 -c:a libopus output.webm
```
* **-crf 30:** controla la calidad. Menor = mejor calidad, mayor = más compresión.
* **-b:v 0:** bitrate variable (necesario con CRF en VP9).
* **libopus:** compresión eficiente de audio.

### AV1 (mejor compresión, más lento):
``` bash
ffmpeg -i input.mp4 -c:v libaom-av1 -crf 35 -b:v 0 -c:a libopus output.webm
```
* **libaom-av1:** códec AV1 (más lento).
* **-crf 35:** ajusta calidad. Entre 30–40 es óptimo para web.
* **Tarda bastante, pero el archivo final pesa mucho menos.**