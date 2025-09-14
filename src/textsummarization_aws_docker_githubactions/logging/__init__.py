import os
import logging
import sys

logging_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(module)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
LOG_FILE_PATH = os.path.join(log_dir, "running_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format=logging_string,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("text_summarization_logger")
logger.info("Logger has been configured.")