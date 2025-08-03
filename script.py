import os
import subprocess

INPUT_DIR = "input"
OUTPUT_DIR = "output"
CRF = 32  # Ajusta esto si quieres más calidad (menor número) o más compresión (mayor número)

def convert_mp4_to_webm(input_path, output_path, crf=CRF):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "libvpx-vp9",
        "-b:v", "0",            # CRF mode
        "-crf", str(crf),
        "-c:a", "libopus",
        output_path
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ {os.path.basename(input_path)} → {os.path.basename(output_path)}")
    except subprocess.CalledProcessError:
        print(f"❌ Error converting {input_path}")

def batch_convert(input_dir=INPUT_DIR, output_dir=OUTPUT_DIR):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    mp4_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".mp4")]

    if not mp4_files:
        print("⚠️ No se encontraron archivos .mp4 en la carpeta de entrada.")
        return

    for file in mp4_files:
        input_path = os.path.join(input_dir, file)
        output_filename = os.path.splitext(file)[0] + ".webm"
        output_path = os.path.join(output_dir, output_filename)

        convert_mp4_to_webm(input_path, output_path)

if __name__ == "__main__":
    batch_convert()