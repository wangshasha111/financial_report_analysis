"""
Image processing utilities
"""
from PIL import Image
import io
from typing import List, Tuple


def validate_image(image_bytes: bytes, max_size_mb: int = 10) -> Tuple[bool, str]:
    """
    Validate image file.
    
    Args:
        image_bytes: Image file bytes
        max_size_mb: Maximum allowed file size in MB
        
    Returns:
        Tuple of (is_valid: bool, message: str)
    """
    try:
        # Check file size
        size_mb = len(image_bytes) / (1024 * 1024)
        if size_mb > max_size_mb:
            return False, f"File size ({size_mb:.2f}MB) exceeds maximum allowed size ({max_size_mb}MB)"
        
        # Try to open image
        image = Image.open(io.BytesIO(image_bytes))
        
        # Verify it's a valid image
        image.verify()
        
        return True, "Valid image"
        
    except Exception as e:
        return False, f"Invalid image file: {str(e)}"


def resize_image_if_needed(image_bytes: bytes, max_dimension: int = 2048) -> bytes:
    """
    Resize image if it exceeds maximum dimensions.
    
    Args:
        image_bytes: Original image bytes
        max_dimension: Maximum width or height
        
    Returns:
        Resized image bytes (or original if no resize needed)
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        
        # Check if resize needed
        if image.width <= max_dimension and image.height <= max_dimension:
            return image_bytes
        
        # Calculate new dimensions
        ratio = min(max_dimension / image.width, max_dimension / image.height)
        new_size = (int(image.width * ratio), int(image.height * ratio))
        
        # Resize image
        resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
        
        # Convert back to bytes
        output = io.BytesIO()
        resized_image.save(output, format=image.format or 'PNG')
        return output.getvalue()
        
    except Exception as e:
        # If resize fails, return original
        return image_bytes


def get_image_info(image_bytes: bytes) -> dict:
    """
    Get information about an image.
    
    Args:
        image_bytes: Image file bytes
        
    Returns:
        Dictionary with image information
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        
        return {
            'format': image.format,
            'mode': image.mode,
            'size': image.size,
            'width': image.width,
            'height': image.height,
            'file_size_mb': len(image_bytes) / (1024 * 1024)
        }
    except Exception as e:
        return {'error': str(e)}
