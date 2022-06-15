import subprocess

def to_text(image_path):
    command = "tesseract '" + image_path + "' stdout"
    print(command)
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.split()



