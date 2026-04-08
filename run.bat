@echo off
REM AI Fitness Coach Project - Universal Hugging Face Version
echo ========================================
echo   AI Fitness Coach - Universal Launcher
echo   Works on all systems via Hugging Face
echo ========================================

REM Check if Docker is installed and running
echo Checking Docker installation...
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not installed or not in PATH
    echo Please install Docker Desktop first
    echo Download from: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

docker info >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker is not running
    echo Please start Docker Desktop
    pause
    exit /b 1
)

echo ✅ Docker is installed and running

REM Stop and remove any existing containers
echo Cleaning up existing containers...
docker stop ai-fitness-coach-universal >nul 2>&1
docker rm ai-fitness-coach-universal >nul 2>&1

REM Remove any existing images to ensure fresh build
echo Cleaning up old images...
docker rmi ai-fitness-coach:universal >nul 2>&1

REM Build fresh Docker image for universal compatibility
echo Building universal Docker image...
echo This may take a few minutes on first run...
docker build -t ai-fitness-coach:universal .

if errorlevel 1 (
    echo ❌ Failed to build Docker image
    echo Please check Dockerfile and requirements.txt
    pause
    exit /b 1
)

echo ✅ Universal Docker image built successfully

REM Run the Docker container with network access
echo Starting AI Fitness Coach in Docker...
docker run -d --name ai-fitness-coach-universal -p 8506:8501 --restart unless-stopped ai-fitness-coach:universal

if errorlevel 1 (
    echo ❌ Failed to start Docker container
    pause
    exit /b 1
)

echo ✅ Container started successfully

REM Wait for application to start
echo Waiting for application to initialize...
timeout /t 20 /nobreak >nul

REM Get container status
echo Checking container status...
docker ps --filter "name=ai-fitness-coach-universal" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

REM Get network information
echo.
echo ========================================
echo         ACCESS URLS
echo ========================================

REM Get local IP addresses
echo Local Access URLs:
echo   📍 Local: http://localhost:8506

for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do (
    echo   🏠 Network: http://%%a:8506
)

REM Get public IP with fast detection
echo.
echo Getting external IP address...
set PUBLIC_IP=Unknown

echo Checking external IP...
for /f %%a in ('powershell -Command "$ProgressPreference='SilentlyContinue'; try { (Invoke-WebRequest -Uri 'https://checkip.amazonaws.com' -UseBasicParsing -TimeoutSec 3).Content.Trim() } catch { 'Unknown' }"') do set PUBLIC_IP=%%a

if "%PUBLIC_IP%"=="Unknown" (
    for /f %%a in ('powershell -Command "$ProgressPreference='SilentlyContinue'; try { (Invoke-WebRequest -Uri 'https://api.ipify.org?format=text' -UseBasicParsing -TimeoutSec 3).Content.Trim() } catch { 'Unknown' }"') do set PUBLIC_IP=%%a
)

if not "%PUBLIC_IP%"=="Unknown" (
    echo   🌐 External: http://%PUBLIC_IP%:8506 ✅
) else (
    echo   🌐 External: Network restrictions detected
    echo   💡 Get your public IP from https://whatismyipaddress.com/
    echo   💡 Then use: http://YOUR_PUBLIC_IP:8506
)

echo.
echo ========================================
echo         IMPORTANT NOTES
echo ========================================
echo 1. ✅ Local URLs work immediately
echo 2. ✅ Network URLs work for devices on same network
echo 3. 🌐 External URL requires port forwarding setup
echo 4. 🐳 Container name: ai-fitness-coach-universal
echo 5. 🛑 To stop: docker stop ai-fitness-coach-universal

echo.
echo 🚀 AI Fitness Coach is ready!
echo.
echo Testing URLs:
echo ✅ Local: http://localhost:8506
echo ✅ Network: http://192.168.56.1:8506 (or your local IP)
echo.
echo Press any key to open in browser...
pause >nul

REM Open in default browser
start http://localhost:8506

echo.
echo To view container logs: docker logs ai-fitness-coach-universal
echo To stop container: docker stop ai-fitness-coach-universal
echo.
pause
