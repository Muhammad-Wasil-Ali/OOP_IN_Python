import logging


logging.basicConfig(filename="first.log",level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

print("Hello world")
logging.info("App started")
logging.error("Something broke")