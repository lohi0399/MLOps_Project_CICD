import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.path.join(os.getcwd(),"logs",LOG_FILE)) #getcwd is get current working directory, and in that is stores a file logsLOG_FILE
os.makedirs(logs_path,exist_ok=True) # Keeping appending in the same file

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
) # This the file structure within the file. logging.info takes the argument of logging.info("xyz")


# Testing

# if __name__=="__main__":
#     logging.info("Logging has started")