import logging


def your_method():
    try:
        print("Congrats...")
        print("Your Package is workng fine")
    except Exception as e:
        logging.exception(e)
