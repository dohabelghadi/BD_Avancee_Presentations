@echo off
echo ======================================
echo Starting Paxos Cluster (3 nodes)
echo ======================================

echo.
echo [1/3] Starting Node 1...
start "Paxos-Node-1" cmd /k "cd /d C:\Users\HP\Desktop\CFT-Paxos-Raft && .venv\Scripts\activate && python paxos\paxos_server.py 1"

echo Waiting 2 seconds...
timeout /t 2 /nobreak

echo [2/3] Starting Node 2...
start "Paxos-Node-2" cmd /k "cd /d C:\Users\HP\Desktop\CFT-Paxos-Raft && .venv\Scripts\activate && python paxos\paxos_server.py 2"

echo Waiting 1 second...
timeout /t 1 /nobreak

echo [3/3] Starting Node 3...
start "Paxos-Node-3" cmd /k "cd /d C:\Users\HP\Desktop\CFT-Paxos-Raft && .venv\Scripts\activate && python paxos\paxos_server.py 3"

echo.
echo ======================================
echo All Paxos nodes are starting!
echo ======================================
echo.
echo Check the 3 terminal windows.
echo.
echo Press any key to close this window...
pause