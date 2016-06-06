# somelib.py

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# Example function (for testing)
def func():
    log.critical("A Critical Error!")
    log.debug("A debug message")

if __name__=="__main__":
    # func()
    import logging
    logging.basicConfig()
    func()