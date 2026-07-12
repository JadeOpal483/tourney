#!/usr/bin/env python3
import json
import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

SNAPSHOT_FILE = "tornelo_snapshot.json"


class TorneloHostHandler(SimpleHTTPRequestHandler):
    def _empty_snapshot(self):
        return {
            "meta": {"name": "Chess64 Tournament", "tiebreak": "buchholz"},
            "players": [],
            "rounds": [],
            "currentRound": 0,
            "timer": None,
            "podium": False,
        }

    def _send_json(self, payload, status=200):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/snapshot":
            if not os.path.exists(SNAPSHOT_FILE):
                return self._send_json(self._empty_snapshot(), status=200)
            try:
                with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if not isinstance(data, dict):
                    data = self._empty_snapshot()
                return self._send_json(data, status=200)
            except Exception as exc:
                return self._send_json({"error": str(exc)}, status=500)
        return super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path
        if path != "/api/snapshot":
            return self._send_json({"error": "not_found"}, status=404)
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length)
            payload = json.loads(raw.decode("utf-8"))
            with open(SNAPSHOT_FILE, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False)
            return self._send_json({"ok": True}, status=200)
        except Exception as exc:
            return self._send_json({"error": str(exc)}, status=400)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    host = os.environ.get("HOST", "0.0.0.0")
    server = ThreadingHTTPServer((host, port), TorneloHostHandler)
    print(f"Tornelo host running on http://{host}:{port}")
    print("Serving files + /api/snapshot shared state")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
