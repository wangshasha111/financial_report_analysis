"""
AI Handler for OpenAI and Gemini integration
"""
import base64
import os
from typing import List, Dict, Any
import openai
import google.generativeai as genai
from PIL import Image
import io


class AIHandler:
    """Handles interactions with OpenAI and Gemini APIs."""
    
    def __init__(self, provider: str, model: str, api_key: str):
        """
        Initialize AI Handler.
        
        Args:
            provider: 'openai' or 'gemini'
            model: Model identifier
            api_key: API key for the service
        """
        self.provider = provider.lower()
        self.model = model
        self.api_key = api_key
        
        if self.provider == 'openai':
            openai.api_key = api_key
            self.client = openai.OpenAI(api_key=api_key)
        elif self.provider == 'gemini':
            genai.configure(api_key=api_key)
            # Pass the model name directly from config. The SDK handles the rest.
            self.client = genai.GenerativeModel(model)
        else:
            raise ValueError(f"Unsupported provider: {provider}")
    
    def encode_image(self, image_bytes: bytes) -> str:
        """Encode image to base64 string."""
        return base64.b64encode(image_bytes).decode('utf-8')
    
    def analyze_with_openai(self, images: List[bytes], prompt: str) -> str:
        """
        Analyze images using OpenAI's vision models.
        
        Args:
            images: List of image bytes
            prompt: Analysis prompt
            
        Returns:
            Analysis result as string
        """
        try:
            # Prepare messages with images
            content = [{"type": "text", "text": prompt}]
            
            for img_bytes in images:
                base64_image = self.encode_image(img_bytes)
                content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": "high"
                    }
                })
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": content
                    }
                ],
                max_tokens=4096,
                temperature=0.2
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            raise Exception(f"OpenAI API Error: {str(e)}")
    
    def analyze_with_gemini(self, images: List[bytes], prompt: str) -> str:
        """
        Analyze images using Google's Gemini models.
        
        Args:
            images: List of image bytes
            prompt: Analysis prompt
            
        Returns:
            Analysis result as string
        """
        try:
            # Prepare content with images
            content = [prompt]
            
            for img_bytes in images:
                # Convert bytes to PIL Image
                image = Image.open(io.BytesIO(img_bytes))
                content.append(image)
            
            # Generate response
            response = self.client.generate_content(
                content,
                generation_config={
                    "temperature": 0.2,
                    "max_output_tokens": 8192,
                }
            )
            
            return response.text
            
        except Exception as e:
            raise Exception(f"Gemini API Error: {str(e)}")
    
    def analyze(self, images: List[bytes], prompt: str, role: str = "Analyst") -> Dict[str, Any]:
        """
        Main analysis method that routes to appropriate provider.
        
        Args:
            images: List of image bytes
            prompt: Analysis prompt
            role: User role (for context)
            
        Returns:
            Dictionary containing analysis results and metadata
        """
        if not images:
            raise ValueError("No images provided for analysis")
        
        if not prompt:
            raise ValueError("No prompt provided for analysis")
        
        # Add role context to prompt
        enhanced_prompt = f"[User Role: {role}]\n\n{prompt}"
        
        # Route to appropriate provider
        if self.provider == 'openai':
            analysis_text = self.analyze_with_openai(images, enhanced_prompt)
        elif self.provider == 'gemini':
            analysis_text = self.analyze_with_gemini(images, enhanced_prompt)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")
        
        return {
            "analysis": analysis_text,
            "provider": self.provider,
            "model": self.model,
            "role": role,
            "image_count": len(images)
        }
