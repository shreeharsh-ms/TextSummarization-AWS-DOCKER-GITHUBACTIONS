import os
from pathlib import Path
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(levelname)s - %(message)s - line: %(lineno)d',
    level=logging.INFO,
)

project_name = "TextSummarization-AWS-DOCKER-GITHUBACTIONS"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configration.py",
    f"{project_name}/pipelines/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "setup.py",
    "research/trials.ipynb",
    "Dockerfile",
    "requirements.txt",
    "app.py",
    "main.py",
]

def create_files():
    for file_path in list_of_files:
        filePath = Path(file_path)
        fileDir, fileName = filePath.parent, filePath.name
        if not fileDir.exists():
            logging.info(f"Creating directory: {fileDir}")
            fileDir.mkdir(parents=True, exist_ok=True)
        if ((not filePath.exists()) or (os.path.getsize(filePath) == 0)):
        # if ((not filePath.exists()) or (filePath.stat().st_size == 0)):
            logging.info(f"Creating file: {filePath}")
            filePath.touch()
        else:
            logging.info(f"File already exists: {filePath}")

if __name__ == "__main__":
    logging.info("Starting file creation process...")
    create_files()
    logging.info("File creation process completed.")
    logging.info(f"Log file created at: {LOG_FILE_PATH}")
