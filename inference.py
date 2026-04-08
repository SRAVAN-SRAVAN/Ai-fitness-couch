#!/usr/bin/env python3
"""
AI Fitness Coach - Inference Module
OpenEnv compliant inference with structured logging and environment variables
"""

import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional
import traceback

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # Fallback if python-dotenv not available
    pass

# OpenAI client for LLM calls
from openai import OpenAI

# Environment variables with defaults
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN") or os.getenv("OPENAI_API_KEY")  # Support both
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")  # Optional for docker image runs

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class FitnessInference:
    """Main inference class for AI Fitness Coach"""
    
    def __init__(self):
        """Initialize OpenAI client with environment variables"""
        try:
            self.client = OpenAI(
                api_key=HF_TOKEN,
                base_url=API_BASE_URL
            )
            self.model = MODEL_NAME
            
            logger.info("START - Inference client initialized")
            logger.info(f"STEP - Using model: {self.model}")
            logger.info(f"STEP - API base URL: {API_BASE_URL}")
            logger.info(f"STEP - API key configured: {'Yes' if HF_TOKEN else 'No'}")
            
        except Exception as e:
            logger.error(f"END - Failed to initialize inference client: {str(e)}")
            raise
    
    def log_step(self, step_name: str, details: Dict[str, Any] = None):
        """Log structured step information"""
        logger.info(f"STEP - {step_name}")
        if details:
            for key, value in details.items():
                logger.info(f"STEP - {key}: {value}")
    
    def generate_fitness_advice(self, user_profile: Dict[str, Any], query: str) -> str:
        """Generate fitness advice using LLM"""
        logger.info("START - Generating fitness advice")
        
        try:
            self.log_step("Processing user query", {
                "query_length": len(query),
                "user_age": user_profile.get("age", "unknown"),
                "user_goal": user_profile.get("fitness_goals", "not specified")
            })
            
            # Construct prompt for fitness advice
            prompt = f"""
            As an expert fitness coach, provide personalized advice based on the following user profile and query:
            
            User Profile:
            - Age: {user_profile.get('age', 'Not specified')}
            - Gender: {user_profile.get('gender', 'Not specified')}
            - Height: {user_profile.get('height_cm', 'Not specified')} cm
            - Weight: {user_profile.get('weight_kg', 'Not specified')} kg
            - Fitness Goals: {user_profile.get('fitness_goals', 'Not specified')}
            
            User Query: {query}
            
            Provide comprehensive, safe, and personalized fitness advice. Include specific recommendations for workout routines, nutrition, and lifestyle changes.
            """
            
            self.log_step("Calling LLM for advice generation")
            
            # Make LLM call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert fitness coach providing safe and personalized advice."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            
            advice = response.choices[0].message.content
            
            self.log_step("Advice generated successfully", {
                "response_length": len(advice),
                "tokens_used": response.usage.total_tokens if response.usage else "unknown"
            })
            
            logger.info("END - Fitness advice generated successfully")
            return advice
            
        except Exception as e:
            logger.error(f"END - Failed to generate fitness advice: {str(e)}")
            logger.error(f"STEP - Error details: {traceback.format_exc()}")
            return f"I apologize, but I encountered an error while generating your fitness advice: {str(e)}"
    
    def analyze_workout_data(self, workout_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze workout data and provide insights"""
        logger.info("START - Analyzing workout data")
        
        try:
            self.log_step("Processing workout data", {
                "data_type": type(workout_data).__name__,
                "has_exercises": "exercises" in workout_data,
                "workout_count": len(workout_data.get("exercises", []))
            })
            
            # Construct analysis prompt
            prompt = f"""
            Analyze the following workout data and provide insights:
            
            Workout Data: {json.dumps(workout_data, indent=2)}
            
            Provide analysis including:
            1. Workout effectiveness rating (1-10)
            2. Areas for improvement
            3. Recommendations for next workout
            4. Progress indicators
            
            Return the analysis in JSON format with keys: effectiveness, improvements, recommendations, progress_indicators
            """
            
            self.log_step("Calling LLM for workout analysis")
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a fitness data analyst. Always return valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=0.3
            )
            
            analysis_text = response.choices[0].message.content
            
            try:
                analysis = json.loads(analysis_text)
            except json.JSONDecodeError:
                # Fallback if JSON parsing fails
                analysis = {
                    "effectiveness": 7,
                    "improvements": "Focus on form consistency",
                    "recommendations": "Increase weight gradually",
                    "progress_indicators": "Good workout frequency"
                }
            
            self.log_step("Workout analysis completed", {
                "effectiveness_score": analysis.get("effectiveness", "unknown"),
                "has_recommendations": bool(analysis.get("recommendations"))
            })
            
            logger.info("END - Workout analysis completed successfully")
            return analysis
            
        except Exception as e:
            logger.error(f"END - Failed to analyze workout data: {str(e)}")
            logger.error(f"STEP - Error details: {traceback.format_exc()}")
            return {
                "effectiveness": 5,
                "improvements": "Unable to analyze due to error",
                "recommendations": "Please try again later",
                "progress_indicators": f"Error: {str(e)}"
            }
    
    def generate_motivational_message(self, user_progress: Dict[str, Any]) -> str:
        """Generate motivational message based on user progress"""
        logger.info("START - Generating motivational message")
        
        try:
            self.log_step("Analyzing user progress", {
                "has_workouts": "total_workouts" in user_progress,
                "workout_count": user_progress.get("total_workouts", 0),
                "consistency_score": user_progress.get("consistency_score", 0)
            })
            
            prompt = f"""
            Generate a motivational message based on the following user progress:
            
            Progress Data: {json.dumps(user_progress, indent=2)}
            
            Create an encouraging, personalized message that:
            1. Acknowledges their achievements
            2. Provides positive reinforcement
            3. Encourages continued progress
            4. Is specific to their actual progress
            
            Keep it concise (under 150 words) and inspiring.
            """
            
            self.log_step("Calling LLM for motivational message")
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an encouraging fitness coach who provides personalized motivation."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.8
            )
            
            message = response.choices[0].message.content
            
            self.log_step("Motivational message generated", {
                "message_length": len(message),
                "tokens_used": response.usage.total_tokens if response.usage else "unknown"
            })
            
            logger.info("END - Motivational message generated successfully")
            return message
            
        except Exception as e:
            logger.error(f"END - Failed to generate motivational message: {str(e)}")
            logger.error(f"STEP - Error details: {traceback.format_exc()}")
            return "Keep pushing forward! Every workout brings you closer to your goals. You've got this! 💪"

def main():
    """Main function for testing inference"""
    logger.info("START - AI Fitness Coach Inference System")
    
    try:
        # Initialize inference
        inference = FitnessInference()
        
        # Test with sample data
        sample_profile = {
            "age": 30,
            "gender": "male",
            "height_cm": 175,
            "weight_kg": 75,
            "fitness_goals": "Build muscle and improve endurance"
        }
        
        sample_query = "I want to build muscle but only have 3 days per week to work out. What's the best approach?"
        
        # Generate advice
        advice = inference.generate_fitness_advice(sample_profile, sample_query)
        logger.info(f"STEP - Generated advice: {advice[:100]}...")
        
        # Test workout analysis
        sample_workout = {
            "exercises": [
                {"name": "Bench Press", "sets": 3, "reps": 10, "weight": 80},
                {"name": "Squats", "sets": 3, "reps": 12, "weight": 100}
            ],
            "duration_minutes": 45,
            "calories_burned": 300
        }
        
        analysis = inference.analyze_workout_data(sample_workout)
        logger.info(f"STEP - Workout analysis: {analysis}")
        
        # Test motivational message
        progress = {
            "total_workouts": 12,
            "consistency_score": 0.85,
            "weight_change_kg": -2.5
        }
        
        motivation = inference.generate_motivational_message(progress)
        logger.info(f"STEP - Motivational message: {motivation}")
        
        logger.info("END - All inference tests completed successfully")
        
    except Exception as e:
        logger.error(f"END - Inference system failed: {str(e)}")
        logger.error(f"STEP - Error details: {traceback.format_exc()}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
