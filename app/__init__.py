from flask import Flask, render_template, request

app = Flask(__name__)

from app.controls.defalt import *