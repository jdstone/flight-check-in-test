from config import config
from flask import Flask
import logging
import os


def create_app(config_class=os.getenv('FLASK_ENV') or 'default'):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config[config_class])

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    ###################################################
    #### Register Blueprints
    ###################################################
    from . import confirm
    app.register_blueprint(confirm.bp, url_prefix='/')
    
    from . import review
    app.register_blueprint(review.bp, url_prefix='/')

    ###################################################
    #### Error Logging
    ###################################################
    logger = logging.getLogger(__name__)
    if not app.debug and not app.testing:
        logger.setLevel(logging.INFO)
    elif app.debug or app.testing:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.DEBUG)

    return app

