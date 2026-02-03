@echo off
echo ======================================
echo Stopping All Services
echo ======================================

echo.
echo [1/2] Stopping MongoDB...
cd docker
docker-compose down
cd ..

echo.
echo [2/2] Stopping Python processes...
taskkill /F /IM python.exe /T 2>nul

echo.
echo ======================================
echo All services stopped successfully!
echo ======================================
echo.
pause