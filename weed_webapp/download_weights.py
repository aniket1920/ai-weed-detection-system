import os
import gdown

weights_path = "best.pt"

if not os.path.exists(weights_path):
    print("Downloading model weights from Google Drive...")
    gdown.download_folder(
        "https://drive.google.com/drive/folders/1Wn5OxZ2hHjXUaXZhRHsvsjFjHkmfFt9M",
        quiet=False,
        output="."   # downloads into same folder as main.py → best.pt lands right here
    )
    print("Download complete!")
else:
    print("Weights already exist, skipping download.")