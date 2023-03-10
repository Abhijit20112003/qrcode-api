from flask import Flask, request, send_file
from io import BytesIO
import qrcode
import io
app = Flask(__name__)

def qr_code():
    url = request.args.get('url')
    img = qrcode.make(url)
# Save the QR code image
     buf = BytesIO()
     img.save(buf, 'PNG')
     buf.seek(0)
 # Send the QR code image as the API response
     return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
        app.run()
