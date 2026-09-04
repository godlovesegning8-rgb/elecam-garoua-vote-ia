import os
from dotenv import load_dotenv

load_dotenv()

# Application Config
APP_NAME = "ELECAM GAROUA VOTE IA"
APP_VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "True") == "True"

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")
DATABASE_PATH = os.getenv("DATABASE_PATH", "./database.db")

# API Config
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))

# Security & Authentication
ADMIN_CODE = os.getenv("ADMIN_CODE", "GAROUA2025")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 480

# Face Recognition Thresholds
FACE_CONFIDENCE_THRESHOLD = 0.40  # DeepFace ArcFace threshold
FACE_RECOGNITION_THRESHOLD = 75   # Confiance minimum en %
MAX_FACE_DISTANCE = 0.40          # Distance cosine maximale
OCR_CONFIDENCE_MIN = 0.80         # Confiance OCR minimum

# Cameroon Colors
CAMEROON_GREEN = "#006400"
CAMEROON_YELLOW = "#FFD700"
CAMEROON_RED = "#CE1126"

# File Upload Config
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}

# QR Code Config
QR_BOX_SIZE = 10
QR_BORDER = 4

# Election Config
ELECTIONS = {
    "presidential": "Présidentielle",
    "legislative": "Législatives",
    "municipal": "Municipales"
}

# CNI Regex Pattern (9-12 digits)
CNI_PATTERN = r"\d{9,12}"

# CORS Config
CORS_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000"
]

# Logging Config
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_DIR = os.getenv("LOG_DIR", "./logs")

# Create necessary directories
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
