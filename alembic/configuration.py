from environs import Env
import os


def env_reader() -> Env:
    env = Env()
    local_path = ".env"
    cloud_path = "config/.env.cloud"

    if os.path.isfile(local_path):
        env.read_env(local_path)
    else:
        env.read_env(cloud_path)

    return env


env = env_reader()
