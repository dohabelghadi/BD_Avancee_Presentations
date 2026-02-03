@echo off
echo ======================================
echo Starting Raft Cluster (3 nodes)
echo ======================================

echo.
echo [1/3] Starting Node 1...
start "Raft-Node-1" cmd /k "cd /d C:\Users\HP\Desktop\CFT-Paxos-Raft && .venv\Scripts\activate && python raft\raft_server.py 1"

echo Waiting 2 seconds...
timeout /t 2 /nobreak

echo [2/3] Starting Node 2...
start "Raft-Node-2" cmd /k "cd /d C:\Users\HP\Desktop\CFT-Paxos-Raft && .venv\Scripts\activate && python raft\raft_server.py 2"

echo Waiting 1 second...
timeout /t 1 /nobreak

echo [3/3] Starting Node 3...
start "Raft-Node-3" cmd /k "cd /d C:\Users\HP\Desktop\CFT-Paxos-Raft && .venv\Scripts\activate && python raft\raft_server.py 3"

echo.
echo ======================================
echo All Raft nodes are starting!
echo ======================================
echo.
echo Check the 3 terminal windows.
echo A leader should be elected in 2-5 seconds.
echo.
echo Press any key to close this window...
pause