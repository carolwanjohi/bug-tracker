import os
from os.path import join, dirname
from dotenv import load_dotenv

class Config:
    '''
    General configuration parent class
    '''
    # Get env file where the Pivotal token is
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    API_TOKEN = os.getenv('PIVOTAL_TOKEN')

    PIVOTAL_BASE_URL = 'https://www.pivotaltracker.com/services/v5/{}'

class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}