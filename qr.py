from flask import Flask, request, send_file
from io import BytesIO
import qrcode
import io
app = Flask(__name__)

def qr_code():
