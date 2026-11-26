
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug("This is a debug message")
logging.info("System started successfully")
logging.warning("Low disk space")
logging.error("File not found")
logging.critical("System failure")
