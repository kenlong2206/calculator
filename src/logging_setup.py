import logging
import os

# Configure the logger
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LOG_DIR = os.path.join(PROJECT_ROOT, 'calculator', 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'calculator_log.txt')

def setup_logging(file=LOG_FILE, level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level)

    # Check if any handlers already exist, and remove them
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Debugging: print paths
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Log directory: {LOG_DIR}")
    print(f"Log file: {LOG_FILE}")
    print(f"Directory exists: {os.path.exists(LOG_DIR)}")
    print(f"File exists: {os.path.exists(LOG_FILE)}")

    # Ensure the log directory exists
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
        print(f"Created directory: {LOG_DIR}")

    # Ensure the log file exists
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()
        print(f"Created file: {LOG_FILE}")

    # Add a file handler
    file_handler = logging.FileHandler(file)
    file_handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s:: %(name)s:: %(levelname)s:: %(funcName)s:: %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

