import os


class DevConfig:

    MONGODB_SETTINGS = {
        "db": os.getenv("MONGODB_DB", "mydb"),
        "host": os.getenv("MONGODB_HOST", "localhost"),
        "username": os.getenv("MONGODB_USERNAME", "root"),
        "password": os.getenv("MONGODB_PASSWORD", "root"),
        "authentication_source": "admin",
    }


class ProdConfig:

    MONGODB_USER = os.getenv("MONGODB_USER")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_DB = os.getenv("MONGODB_DB")

    MONGODB_SETTINGS = {
        "host": "mongodb+srv://%s:%s@%s/%s?appName=FlaskAPI"
        % (MONGODB_USER, MONGODB_PASSWORD, MONGODB_HOST, MONGODB_DB)
    }


class MockConfig:

    MONGODB_SETTINGS = {"db": "users", "host": "mongomock://localhost"}
