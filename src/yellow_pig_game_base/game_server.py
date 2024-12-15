import os

from flask import Flask
from flask_restful import Api, Resource


class GameServer:

    def __init__(self):
        self.app = Flask(__name__, static_folder="static", static_url_path="/static")
        self.api = Api(self.app)

    def add_resource(self, game : Resource, path):
        self.api.add_resource(game, path)

    def start(self):
        self.app.run(debug=True, port=8080)