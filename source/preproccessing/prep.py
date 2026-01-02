import zipfile
from pathlib import Path
import shutil

data_dir = Path("data")

with zipfile.ZipFile(str(data_dir / "dataset.zip"), 'r') as zip_ref:
    zip_ref.extractall(data_dir)

raw_dir = data_dir / "raw"
proc_dir = data_dir / "processed"
raw_dir.mkdir(exist_ok=True)
proc_dir.mkdir(exist_ok=True)

# move images/imges -> raw
for name in ("images", "imges"):
    src = data_dir / name
    if src.exists() and src.is_dir():
        for item in src.iterdir():
            shutil.move(str(item), str(raw_dir))
        try:
            src.rmdir()
        except OSError:
            print(f"Could not remove directory {src}")

# move resized -> processed
resized = data_dir / "resized"
if resized.exists() and resized.is_dir():
    for item in resized.iterdir():
        shutil.move(str(item), str(proc_dir))
    try:
        resized.rmdir()
    except OSError:
        print(f"Could not remove directory {resized}")