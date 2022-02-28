from flask import Blueprints

main = Blueprints('main',__name__)

from .import views,errors