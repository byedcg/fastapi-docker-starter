from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Awesome API"  # will be overwriteen by .env file

    class Config:
        env_file = ".env"
