#!/usr/bin/env python3
"""
AI Fitness Coach - Hugging Face Spaces Deployment Script
Automated deployment to Hugging Face Spaces
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, description=""):
    """Run a command and handle errors"""
    print(f"\n🔧 {description}")
    print(f"Running: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Success: {description}")
            if result.stdout:
                print(f"Output: {result.stdout}")
            return True
        else:
            print(f"❌ Error: {description}")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Exception: {description}")
        print(f"Exception: {str(e)}")
        return False

def check_prerequisites():
    """Check if all prerequisites are met"""
    print("🔍 Checking prerequisites...")
    
    # Check if huggingface_hub is installed
    try:
        import huggingface_hub
        print("✅ huggingface_hub is installed")
    except ImportError:
        print("❌ huggingface_hub not found")
        return False
    
    # Check if required files exist
    required_files = [
        "app.py",
        "requirements_hf.txt", 
        "packages.txt",
        "README.md",
        "app/streamlit_app.py",
        "env/models.py"
    ]
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            return False
    
    return True

def login_to_hf():
    """Login to Hugging Face"""
    print("\n🔐 Logging into Hugging Face...")
    
    # Try to get current login status
    if run_command("huggingface-cli whoami", "Checking current login status"):
        print("✅ Already logged in to Hugging Face")
        return True
    
    print("Please login to Hugging Face:")
    print("1. Get your access token from: https://huggingface.co/settings/tokens")
    print("2. Run: huggingface-cli login")
    print("3. Enter your token when prompted")
    
    input("Press Enter after you've logged in...")
    
    # Verify login
    if run_command("huggingface-cli whoami", "Verifying login"):
        print("✅ Successfully logged in to Hugging Face")
        return True
    else:
        print("❌ Login failed")
        return False

def create_space():
    """Create new Hugging Face Space"""
    print("\n🚀 Creating Hugging Face Space...")
    
    # Get username
    result = subprocess.run("huggingface-cli whoami", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ Cannot get username")
        return False
    
    username = result.stdout.strip()
    space_name = "ai-fitness-coach"
    space_repo = f"{username}/{space_name}"
    
    print(f"Creating space: {space_repo}")
    
    # Create space using CLI
    cmd = f"huggingface-cli create-space --name {space_name} --sdk streamlit --public --hardware cpu-basic"
    if run_command(cmd, f"Creating space {space_name}"):
        print(f"✅ Space created: https://huggingface.co/spaces/{space_repo}")
        return space_repo
    else:
        print("❌ Space creation failed, might already exist")
        return space_repo

def prepare_deployment_files():
    """Prepare files for deployment"""
    print("\n📦 Preparing deployment files...")
    
    # Copy requirements file
    if run_command("cp requirements_hf.txt requirements.txt", "Copying requirements for HF"):
        print("✅ Requirements file prepared")
    
    # Create .gitignore if not exists
    gitignore_content = """
venv/
__pycache__/
*.pyc
.env
.DS_Store
*.log
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content.strip())
    
    print("✅ .gitignore created")
    
    return True

def deploy_to_space(space_repo):
    """Deploy to Hugging Face Space"""
    print(f"\n🚀 Deploying to {space_repo}...")
    
    # Initialize git if not already
    if not Path(".git").exists():
        run_command("git init", "Initializing git repository")
        run_command('git config user.name "AI Fitness Coach"', "Setting git user name")
        run_command('git config user.email "ai@fitness.com"', "Setting git user email")
    
    # Add remote
    remote_url = f"https://huggingface.co/spaces/{space_repo}"
    run_command(f"git remote add origin {remote_url}", "Adding Hugging Face remote")
    
    # Add all files
    run_command("git add .", "Adding all files to git")
    
    # Commit
    run_command('git commit -m "Deploy AI Fitness Coach to Hugging Face Spaces"', "Committing changes")
    
    # Push to Hugging Face
    if run_command("git push origin main --force", "Pushing to Hugging Face"):
        print(f"✅ Successfully deployed to: https://huggingface.co/spaces/{space_repo}")
        return f"https://huggingface.co/spaces/{space_repo}"
    else:
        print("❌ Deployment failed")
        return None

def main():
    """Main deployment function"""
    print("🚀 AI Fitness Coach - Hugging Face Spaces Deployment")
    print("=" * 60)
    
    # Check prerequisites
    if not check_prerequisites():
        print("❌ Prerequisites not met. Please fix issues and try again.")
        return
    
    # Login to Hugging Face
    if not login_to_hf():
        print("❌ Cannot proceed without Hugging Face login.")
        return
    
    # Create space
    space_repo = create_space()
    if not space_repo:
        print("❌ Cannot create space.")
        return
    
    # Prepare files
    if not prepare_deployment_files():
        print("❌ Cannot prepare deployment files.")
        return
    
    # Deploy
    deploy_url = deploy_to_space(space_repo)
    
    if deploy_url:
        print("\n🎉 Deployment Successful!")
        print("=" * 60)
        print(f"🌐 Your AI Fitness Coach is live at:")
        print(f"   {deploy_url}")
        print("\n📋 Next Steps:")
        print("1. Visit the URL to verify deployment")
        print("2. Set environment variables in Space settings:")
        print("   - OPENAI_API_KEY")
        print("   - API_BASE_URL=https://api.openai.com/v1")
        print("   - MODEL_NAME=gpt-4o-mini")
        print("3. Test the application")
        print("4. Use this URL for hackathon submission")
    else:
        print("\n❌ Deployment failed. Check logs above.")

if __name__ == "__main__":
    main()
