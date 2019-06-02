# -*- coding: utf-8 -*-
from odoo import http
import json

class Esp8266(http.Controller):
    @http.route('/esp8266/', auth='public', website=True)
    def index(self):
        return "Hello, world"

    @http.route('/esp8266/json/', auth='public', website=True)
    def index(self, **kw):
        return json.dump({'hello':'there'})
