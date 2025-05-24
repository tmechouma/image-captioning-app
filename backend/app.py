"""
Flask-based Image Captioning API
This application provides a backend service that generates captions for images using
the Microsoft GIT-BASE-COCO (GenerativeImage2Text) model. It accepts image URLs and returns
descriptive captions in English.
"""

import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Enable Cross-Origin Resource Sharing
import logging
from datetime import datetime

# Import Hugging Face transformers for the captioning model
from transformers import AutoProcessor, AutoModelForCausalLM
import requests  # For fetching images from URLs
from PIL import Image  # For image processing

# Configure logging to track application events
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__, static_folder='../frontend/', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Application version (should be updated with each deployment)
APP_VERSION = "1.0.0"

@app.route("/")
def index():
    """Serve the main index.html file from the frontend directory"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/version")
def version():
    """Endpoint to check the current API version and server timestamp"""
    return jsonify({
        "version": APP_VERSION,
        "timestamp": datetime.now().isoformat()
    })

@app.route("/caption-url", methods=["POST"])
def caption_from_url():
    """
    Generate an image caption from a provided URL
    
    Expects JSON payload with format:
    {
        "image_url": "https://example.com/image.jpg"
    }
    
    Returns JSON response with format:
    {
        "caption": "A descriptive caption of the image"
    }
    or error message if unsuccessful
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()
        image_url = data.get("image_url")

        # Validate that an image URL was provided
        if not image_url:
            return jsonify({"error": "Missing image URL."}), 400

        logger.info(f"Received URL: {image_url}")

        # Initialize the image captioning model and processor
        # Using Microsoft's GIT model fine-tuned on COCO dataset
        processor = AutoProcessor.from_pretrained("microsoft/git-base-coco", use_fast=True)
        model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-coco")
        
        # Download and open the image from the URL
        image = Image.open(requests.get(image_url, stream=True).raw)
        
        # Process the image and generate caption
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
        generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        # Log the generated caption
        logger.info(f"Generated caption: {generated_caption}")

        # Return the caption in the response
        if generated_caption:
            return jsonify({"caption": generated_caption})
        else:
            return jsonify({"error": "No caption generated."}), 500

    except Exception as e:
        logger.error(f"Error during caption generation: {e}")
        return jsonify({"error": "Error generating image caption."}), 500

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files from the frontend directory"""
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    # Run the Flask development server
    # In production, this should be served through a WSGI server like Gunicorn
    app.run(debug=True, host='0.0.0.0', port=5000)
