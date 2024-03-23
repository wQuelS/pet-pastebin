# import os

# from pydantic_settings import BaseSettings

# from .dev_config import Settings as DevSettings
# from .main_config import Settings as MainSettings

# setting_mapper = {
#     "dev": DevSettings,
#     "prod": MainSettings
# }

# settings_class: BaseSettings = setting_mapper.get(os.getenv("ENV_CODE", "dev"), DevSettings)
# settings = settings_class()
