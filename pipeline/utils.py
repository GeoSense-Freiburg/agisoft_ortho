import os
import shutil
import logging
from datetime import datetime

def setup_logger(log_file):
    """
    Configures logging to both console and file.
    Args:
        log_file (str): Path to the log file.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def create_log_file(input_folder):
    """
    Creates a log file in the 'log-files' directory inside the input folder.
    Args:
        input_folder (str): Path to the input folder.
    
    Returns:
        str: Full path to the log file.
    """
    log_folder = os.path.join(input_folder, "log-files")
    os.makedirs(log_folder, exist_ok=True)  # Create log folder if it doesn't exist

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_name = f"log_{timestamp}.log"
    log_file_path = os.path.join(log_folder, log_file_name)

    return log_file_path

def move_file(source_path, destination_path):
    """
    Moves file from source to destination path.
    Args:
        source_path (str): Source file path.
        destination_path (str): Destination file path.
    """
    try:
        shutil.move(source_path, destination_path)
        logging.info(f"File moved successfully from {source_path} to {destination_path}")
    except Exception as e:
        logging.error(f"Error moving file: {e}")

def print_timestamp(previous_timestamp=None):
    """
    Logs the current timestamp and time elapsed since the previous timestamp.
    Args:
        previous_timestamp (datetime, optional): Previous timestamp. Defaults to None.
    
    Returns:
        datetime: Current timestamp.
    """
    now = datetime.now()
    formatted_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    if previous_timestamp:
        elapsed_time = now - previous_timestamp
        formatted_elapsed_time = str(elapsed_time)
    else:
        formatted_elapsed_time = "N/A"
    
    logging.info(f"Current Timestamp: {formatted_timestamp}")
    logging.info(f"Time elapsed: {formatted_elapsed_time}")
    
    return now
