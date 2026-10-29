from pydantic_settings import BaseSettings, SettingsConfigDict

class setting(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',extra='ignore')

    DB_CONNECTION:str

setting = setting()