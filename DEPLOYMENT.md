# 🚀 AI Fitness Coach - Deployment Guide

## 📋 Deployment Overview

This guide covers deployment of the AI Fitness Coach application on various platforms including Hugging Face Spaces, local Docker, and cloud platforms.

## 🌐 Hugging Face Spaces Deployment

### Prerequisites
- Hugging Face account
- Git repository
- OpenAI API key

### Steps

1. **Create Hugging Face Space**
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose "Docker" template
   - Set space name (e.g., `ai-fitness-coach`)
   - Make it public or private as needed

2. **Push to Hugging Face**
   ```bash
   git clone https://huggingface.co/spaces/your-username/ai-fitness-coach
   cd ai-fitness-coach
   # Copy all project files
   cp -r /path/to/your/project/* .
   git add .
   git commit -m "Deploy AI Fitness Coach"
   git push
   ```

3. **Configure Environment Variables**
   - Go to Space Settings → Variables
   - Add `OPENAI_API_KEY`: Your OpenAI API key
   - Add `API_BASE_URL`: https://api.openai.com/v1
   - Add `MODEL_NAME`: gpt-4o-mini

4. **Access Your App**
   - Your app will be available at: `https://your-username-ai-fitness-coach.hf.space`

## 🐳 Local Docker Deployment

### Quick Start
```bash
# Clone repository
git clone https://huggingface.co/spaces/your-username/ai-fitness-coach
cd ai-fitness-coach

# Run with launcher (Windows)
run.bat

# Run with launcher (Linux/Mac)
chmod +x run.sh
./run.sh
```

### Manual Docker Commands
```bash
# Build image
docker build -t ai-fitness-coach:universal .

# Run container
docker run -d --name ai-fitness-coach-universal -p 8506:8501 --restart unless-stopped ai-fitness-coach:universal

# Check status
docker ps

# View logs
docker logs ai-fitness-coach-universal

# Stop container
docker stop ai-fitness-coach-universal
```

## ☁️ Cloud Platform Deployment

### AWS ECS

1. **Create ECR Repository**
   ```bash
   aws ecr create-repository --repository-name ai-fitness-coach
   ```

2. **Build and Push Image**
   ```bash
   # Get login token
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
   
   # Build and tag
   docker build -t ai-fitness-coach:universal .
   docker tag ai-fitness-coach:universal <account-id>.dkr.ecr.us-east-1.amazonaws.com/ai-fitness-coach:latest
   
   # Push
   docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/ai-fitness-coach:latest
   ```

3. **Deploy to ECS**
   - Create ECS cluster
   - Define task definition with your image
   - Create service with desired count
   - Configure load balancer and security groups

### Google Cloud Run

1. **Build and Deploy**
   ```bash
   # Configure gcloud
   gcloud auth login
   gcloud config set project your-project-id
   
   # Build and push
   gcloud builds submit --tag gcr.io/your-project-id/ai-fitness-coach
   
   # Deploy
   gcloud run deploy ai-fitness-coach --image gcr.io/your-project-id/ai-fitness-coach --platform managed
   ```

### Azure Container Instances

1. **Create Resource Group**
   ```bash
   az group create --name ai-fitness-rg --location eastus
   ```

2. **Deploy Container**
   ```bash
   az container create \
     --resource-group ai-fitness-rg \
     --name ai-fitness-coach \
     --image your-registry/ai-fitness-coach:latest \
     --dns-name-label your-unique-name \
     --ports 8501
   ```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | Required |
| `API_BASE_URL` | OpenAI API base URL | https://api.openai.com/v1 |
| `MODEL_NAME` | OpenAI model name | gpt-4o-mini |
| `STREAMLIT_SERVER_PORT` | Application port | 8501 |
| `STREAMLIT_SERVER_ADDRESS` | Server address | 0.0.0.0 |

### Port Configuration

- **Internal Port**: 8501 (Streamlit default)
- **External Port**: 8506 (Recommended for local deployment)
- **Protocol**: TCP

## 🔒 Security Considerations

### API Key Management
- Never expose API keys in client-side code
- Use environment variables or secret management
- Rotate API keys regularly

### Network Security
- Use HTTPS in production
- Configure firewalls appropriately
- Implement rate limiting

### Container Security
- Use non-root users
- Minimal base images
- Regular security updates

## 📊 Monitoring and Logging

### Application Monitoring
```bash
# View container logs
docker logs ai-fitness-coach-universal

# Monitor resource usage
docker stats ai-fitness-coach-universal
```

### Health Checks
- Application health endpoint: `/_stcore/health`
- Container health check configured in Dockerfile
- Automatic restart on failure

## � Performance Optimization

### Resource Allocation
- **Minimum RAM**: 512MB
- **Recommended RAM**: 1GB+
- **CPU**: 1 core minimum

### Scaling Strategies
- Horizontal scaling with load balancer
- Container orchestration (Kubernetes/ECS)
- CDN for static assets

## �️ Troubleshooting

### Common Issues

1. **Container Won't Start**
   - Check Docker logs
   - Verify port availability
   - Confirm environment variables

2. **API Connection Failed**
   - Validate OpenAI API key
   - Check network connectivity
   - Verify API rate limits

3. **Performance Issues**
   - Monitor resource usage
   - Check for memory leaks
   - Optimize database queries

### Debug Commands
```bash
# Container diagnostics
docker inspect ai-fitness-coach-universal

# Network connectivity
docker exec ai-fitness-coach-universal curl -I http://localhost:8501

# Environment variables
docker exec ai-fitness-coach-universal env | grep STREAMLIT
```

## 📱 Access URLs

### Local Development
- **Local**: http://localhost:8506
- **Network**: http://YOUR_LOCAL_IP:8506

### Production
- **Hugging Face**: https://your-username-ai-fitness-coach.hf.space
- **Custom Domain**: Configure DNS to point to your deployment

## 🔄 CI/CD Pipeline

### GitHub Actions Example
```yaml
name: Deploy AI Fitness Coach
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build Docker image
        run: docker build -t ai-fitness-coach .
      - name: Deploy to production
        run: # Your deployment commands
```

## 📞 Support

For deployment issues:
1. Check application logs
2. Verify environment configuration
3. Review network settings
4. Consult platform-specific documentation

---

**🚀 Ready to deploy your AI Fitness Coach!**
