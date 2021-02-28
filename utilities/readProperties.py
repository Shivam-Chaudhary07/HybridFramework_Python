import configparser

config = configparser.ConfigParser()
config.read("..\\Configurations\\config.ini")
#config.read(r"C:\Users\dell\PycharmProjects\HybridFramework\Configurations\config.ini")
general_config = config['DEFAULT']

class ReadConfig:

    @staticmethod #we need not create class object, we can directly call class method using static
    def getAppURL():
        url = general_config.get('baseURL')
        return url


    @staticmethod
    def getUsername():
        user = config.get('common info', 'username')
        return user

    @staticmethod
    def getPassword():
        pswrd = config.get('common info', 'password')
        return pswrd
