import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=r"C:\Users\dell\PycharmProjects\HybridFramework\Logs\autologs.log", format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logging.info("Logs Check")
        return logger

if __name__ == '__main__':
    LogGen.loggen()

