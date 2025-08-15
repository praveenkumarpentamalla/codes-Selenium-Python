import logging


class BaseClass:
    def test_logging(self):

        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        logger.debug("A debug statement is executed")
        logger.info("Inforamation statement")
        logger.warning("Something is in warning mode")
        logger.error("A Major error has happened")
        logger.critical("Critical issue")
        return logger
