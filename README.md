# QR Code API

The QR Code API is a simple RESTful API for generating QR Codes. With this API, you can easily generate QR codes for text, URLs, phone numbers, and more.

# Getting Started

To get started with the QR Code API, you will first need to sign up for an API key. Once you have an API key, you can start making requests to the API.

# Endpoints

The QR Code API has the following endpoints:

/qrcode: This endpoint is used to generate a QR code for a given payload (text, URL, phone number, etc.). The endpoint requires an api_key parameter, as well as a data parameter that contains the payload.

# Response

The QR code API will return a QR code image in PNG format. The response will also include a header Content-Type: image/png

# Error Handling

If there is an error with your request, the API will return a JSON object with an error message.

# Additional Parameters

size : This parameter can be used to set the size of the generated QR code. The default size is 300x300.
color : This parameter can be used to set the color of the QR code in hex format. The default color is black.

# Conclusion

The QR Code API makes it easy to generate QR codes for a variety of payloads. With a simple RESTful API, you can easily create QR codes for text, URLs, phone numbers, and more API is live on Rapid API.
