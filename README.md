# 🏃‍♂️ AI Fitness Coach

A comprehensive fitness tracking application powered by AI, featuring personalized workout plans, BMI calculation, calorie management, and an intelligent chatbot assistant.

## ✨ Features

- 🏃‍♂️ **User Profile Management** - Create and manage personal fitness profiles
- 📊 **BMI Calculator** - Track body mass index and health metrics
- 💪 **Workout Tracking** - Log and monitor daily workouts
- 🔥 **Calorie Management** - Track calorie intake and burn
- 📈 **Progress Reports** - Weekly and monthly progress analytics
- 🤖 **AI Chatbot** - Personalized fitness advice and motivation
- 👥 **Multi-User Support** - Google authentication and guest access

## 🚀 Quick Start

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) (Windows/Mac/Linux)

### Installation & Running

1. **Clone the repository**
   ```bash
   git clone https://huggingface.co/spaces/your-username/ai-fitness-coach
   cd ai-fitness-coach
   ```

2. **Run the application**
   ```bash
   # On Windows
   run.bat
   
   # On Linux/Mac
   chmod +x run.sh
   ./run.sh
   ```

3. **Access the application**
   - Local: http://localhost:8506
   - Network: http://YOUR_LOCAL_IP:8506
   - External: http://YOUR_PUBLIC_IP:8506 (with port forwarding)

## 🌐 Access URLs

After running the launcher, you'll see:

- **Local Access**: `http://localhost:8506` - Works immediately
- **Network Access**: `http://192.168.56.1:8506` - Same network devices
- **External Access**: `http://YOUR_PUBLIC_IP:8506` - Requires port forwarding

### External Access Setup

1. **Get Public IP**: Visit https://whatismyipaddress.com/
2. **Port Forwarding**: Forward port 8506 to your computer
3. **Firewall**: Allow port 8506 in Windows Firewall
4. **Test**: Access from mobile phone using different network

## 🐳 Docker Configuration

The application uses Docker for universal compatibility:

- **Image**: `ai-fitness-coach:universal`
- **Container**: `ai-fitness-coach-universal`
- **Port Mapping**: `8506:8501`
- **Restart Policy**: `unless-stopped`

### Docker Commands

```bash
# Check container status
docker ps

# View logs
docker logs ai-fitness-coach-universal

# Stop container
docker stop ai-fitness-coach-universal

# Restart container
docker restart ai-fitness-coach-universal

# Rebuild image
docker build -t ai-fitness-coach:universal .
```

## � Application Features

### User Authentication
- Google OAuth integration
- Guest access option
- Profile customization

### Health Tracking
- BMI calculation with health recommendations
- Calorie intake and burn tracking
- Weight management goals
- Progress visualization

### Workout Management
- Exercise logging
- Duration and intensity tracking
- Calorie burn estimation
- Weekly workout summaries

### AI Assistant
- Personalized fitness advice
- Workout recommendations
- Motivation and goal setting
- Health tips and guidance

## 🔧 Technical Stack

- **Backend**: Python with Streamlit
- **AI**: OpenAI GPT integration
- **Database**: Session state storage
- **Containerization**: Docker
- **Visualization**: Plotly charts
- **Authentication**: OAuth simulation

## 📁 Project Structure

```
ai-fitness-coach/
├── run.bat                 # Windows launcher
├── run.sh                  # Linux/Mac launcher
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── app/
│   ├── streamlit_app.py    # Main application
│   ├── chatbot.py          # AI chatbot
│   ├── bmi.py              # BMI calculator
│   └── calorie_engine.py   # Calorie management
├── env/                    # Environment and models
└── README.md               # This file
```

## 🛠️ Troubleshooting

### Docker Issues
- **Docker not running**: Start Docker Desktop
- **Build fails**: Check requirements.txt and Dockerfile
- **Port conflict**: Change port in run.bat

### Network Issues
- **Local IP not working**: Check firewall settings
- **External IP not working**: Configure port forwarding
- **Connection timeout**: Check router configuration

### Application Issues
- **App not loading**: Check Docker logs
- **Features not working**: Verify environment variables
- **Slow performance**: Check system resources

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support and questions:
- Check the troubleshooting section
- Review Docker logs for errors
- Ensure all prerequisites are installed

---

**🚀 AI Fitness Coach - Your personal fitness companion powered by AI!**
