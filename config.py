"""
Configuration file untuk Care.ly
Berisi constants dan settings
"""
import os

# Get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File Paths - Using absolute paths
BUKU_FILE = os.path.join(BASE_DIR, "data", "buku.perpus.json")
USER_FILE = os.path.join(BASE_DIR, "data", "user.json")

# Admin Credentials (Hardcoded)
ADMIN_USN = "admin"
ADMIN_PW = "admin123"
