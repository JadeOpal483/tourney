#!/bin/zsh
set -e
cd "/Users/ahmad/Documents/New project"

PORT=8000
LOG_FILE="tornelo_server.log"
PID_FILE="tornelo_server.pid"

if [ -f "$PID_FILE" ]; then
  OLD_PID=$(cat "$PID_FILE" 2>/dev/null || true)
  if [ -n "$OLD_PID" ] && kill -0 "$OLD_PID" 2>/dev/null; then
    echo "Server already running (PID $OLD_PID)"
  else
    rm -f "$PID_FILE"
  fi
fi

if [ ! -f "$PID_FILE" ]; then
  nohup python3 server.py > "$LOG_FILE" 2>&1 &
  echo $! > "$PID_FILE"
  sleep 1
fi

IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "localhost")
BASE="http://${IP}:${PORT}"

echo "Server: $BASE"
echo "Display: ${BASE}/display.html"
echo "Player Card: ${BASE}/player-card.html"
echo "QR: ${BASE}/player-qr.html"

open "${BASE}/display.html"
open "${BASE}/player-qr.html"
