import settings
from logging.config import fileConfig
from starlette.applications import Starlette
from router import Router

LOGGER = settings.LOGGER
fileConfig('config/logging_config.ini', defaults={'app_name': f'VozAtivaSystemMessage-{settings.ENVIRONMENT}'})

def main():
    LOGGER.debug("### VozAtiva - System Message Initialized ###")
    return get_app()

def get_app():
    app = Starlette(routes=Router.get_routes())
    return app
