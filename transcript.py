import subprocess


def to_text(image_path):
    command = "tesseract '" + image_path + "' stdout " + \
        "--dpi 300 -c tessedit_pageseg_mode=3"
    result = subprocess.run(
        command, capture_output=True, text=True, shell=True)
    return result.stdout
