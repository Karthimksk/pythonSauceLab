import os
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        URL = config.get('common info', 'baseURL')
        return URL

    @staticmethod
    def getUsername():
        UN = config.get('common info', 'User_Name')
        return UN

    @staticmethod
    def getPassword():
        PW = config.get('common info', 'Pass_Word')
        return PW

    @staticmethod
    def getProductName():
        PN = config.get('product to select', 'nameOfProduct')
        return  PN