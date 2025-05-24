# image-captioning-app
Image-captioning Web Application based on Microsoft GIT-BASE-COCO (GenerativeImage2Text) model

# Image Captioning with GIT-BASE-COCO
An end-to-end application that generates descriptive captions for images using Microsoft's GIT (GenerativeImage2Text) model fine-tuned on the COCO dataset.
![Demo Screenshot](https://github.com/tmechouma/image-captioning-app/blob/main/captioning-image-ms.png) 



## Features

- 🖼️ Generate English captions for any image URL
- 🔍 Live image preview before processing
- 📋 Copy captions to clipboard with one click
- 🎲 Try with sample images
- 📱 Responsive design works on all devices

## Tech Stack

### Backend
- **Python** with **Flask** web framework
- **Hugging Face Transformers** for the GIT-BASE-COCO model
- REST API architecture
- CORS support for frontend integration

### Frontend
- Modern **HTML5** and **CSS3**
- **Tailwind CSS** for utility-first styling
- **Font Awesome** for icons
- Vanilla **JavaScript** for interactivity
- Responsive design with mobile support

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- Node.js (for frontend development)
- Git
- Pip package manager

## Installation

### Backend Setup

1. Clone the repository:
   
   git clone https://github.com/your-username/image-captioning-app.git
   cd image-captioning-app/backend
   
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   pip install -r requirements.txt

4. Download the ML model (this may take several minutes):
   python -c "from transformers import AutoProcessor, AutoModelForCausalLM; AutoProcessor.from_pretrained('microsoft/git-base-coco'); AutoModelForCausalLM.from_pretrained('microsoft/git-base-coco')"
   
 ### Frontend Setup
 The frontend is ready to use as-is. For development:
 
 1. Navigate to the frontend directory:
    cd ../frontend
 2. Install Tailwind CSS (if needed):
    npm install -D tailwindcss
    npx tailwindcss init
  ### Running the Application 
  1. Start the backend server (from backend directory):
     python app.py
  2. The API will be available at http://localhost:5000 

  ### Project Structure

   ```image-captioning-app/
   ├── backend/
   │   └── app.py                # Flask application
   ├── frontend/
   │   ├── index.html            # Main application page
   │   └── static/               # Static assets (CSS, JS, images)
   ├── requirements.txt          # Python dependencies
   └── README.md                 # Main project documentation    ```











