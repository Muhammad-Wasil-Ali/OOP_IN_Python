import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")

try:
    x = int(input("Enter a number: "))
    y = 10 / x
    logging.info(f"Result: {y}")
except ZeroDivisionError as e:
    logging.error("Division by zero attempted")
except ValueError as e:
    logging.error("Invalid input entered")

logging.info("Program ended")
