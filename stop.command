#!/bin/zsh
set -e
cd "/Users/ahmad/Documents/New project"

PID_FILE="tornelo_server.pid"
if [ ! -f "$PID_FILE" ]; then
  echo "No PID file found. Server may already be stopped."
  exit 0
fi

PID=$(cat "$PID_FILE" 2>/dev/null || true)
if [ -n "$PID" ] && kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  echo "Stopped server PID $PID"
else
  echo "Process not running. Cleaning PID file."
fi

rm -f "$PID_FILE"
