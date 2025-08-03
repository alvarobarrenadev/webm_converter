import ffmpeg
import os

input_path = "clase_gratuita.mp4"
output_path = "clase_gratuita.webm"
use_av1 = True  # Cambia a True si quieres AV1

if use_av1:
    ffmpeg.input(input_path).output(
        output_path,
        vcodec='libaom-av1',
        crf=35,
        b='0',
        acodec='libopus'
    ).run()
    
else:
    ffmpeg.input(input_path).output(
        output_path,
        vcodec='libvpx-vp9',
        crf=30,
        b='0',
        acodec='libopus'
    ).run()