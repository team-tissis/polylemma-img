import os
from path import Path
import shutil

if __name__ == '__main__':
    base_dir = Path(os.path.dirname(os.path.abspath(__file__)))
    img_dir = base_dir / "images"

    img_filenames = sorted(base_dir.files("*.png"))
    existed_files = len(img_dir.files("*.png"))

    for i, img_filename in enumerate(img_filenames):
        idx = i + existed_files
        shutil.move(img_filename, img_dir / ("%s.png" % idx))
