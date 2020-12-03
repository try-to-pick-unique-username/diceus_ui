import yaml
import allure

from src.tools.logger import logger, log_exception

class ConfigurationReader:

    __config = 'config.yaml'

    @allure.step('The environment is {env}. Getting the configuration')
    def read(self, env):
        logger.info(f'The environment is {env}. Getting the configuration')
        with open(self.__config, 'r') as stream:
            return yaml.safe_load(stream).get(env, None)
