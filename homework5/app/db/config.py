from pydantic import BaseSettings


class DatabaseConfig(BaseSettings):
    login: str = "admin"
    password: str = "admin"
    host: str = "localhost"
    port: str = "5432"
    database: str = "my_city"


config = DatabaseConfig()
