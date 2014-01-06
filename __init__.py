from flask import Flask

app = Flask(__name__)

import homeland.corelib.mako
import homeland.view
