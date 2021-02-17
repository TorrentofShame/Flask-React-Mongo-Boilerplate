import json
from test.base import BaseTestCase
from server import app

BANNED_RULES = ["/spec/<filename>", "/apidocs/index.html", "/flasgger_static/<filename>", "/static/<filename>", "/apidocs/", "/apispec.json", "/static/", "/flasgger_static/<path:filename>", "/static/<path:filename>", "/auth"]

class TestFlasgger(BaseTestCase):

    def test_get_apidocs(self):
        """The GET on /apidocs should return 200"""
        res = self.client.get("/apidocs/")
        self.assertEqual(res.status_code, 200)

    def test_flasgger_is_not_empty(self):
        """The GET on /apispec_1.json should return a dict with a non-empty paths property"""
        res = self.client.get("/apispec.json")
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode())
        self.assertTrue(data["paths"])

    def test_flasgger_coverage(self):
        """Flasgger Coverage should be 100%"""

        res = self.client.get("apispec.json")
        data = json.loads(res.data.decode())
        flasgger_paths = data["paths"]

        flasgger_endpoint_count = sum(len(r) for r in flasgger_paths.values())

        flask_paths = app.url_map.iter_rules()
        flask_endpoint_count = sum(1 for r in flask_paths if r.rule not in BANNED_RULES)

        coverage = int(100 * flasgger_endpoint_count / flask_endpoint_count)

        self.assertEqual(coverage, 100)
