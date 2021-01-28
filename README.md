# single_nologo_qrdecode
Decode the content of a QR/barcode.

To be noted:
- Support multiple QRs/barcodes (images) at once
- Only one QR/barcode allowed in an image
- No logo or other decoration inside the QR code allowed
- Images are assumed to be well-positioned (not half-rotated or skewed etc)

Usage:
python3 qrcode.py [image-1.jpg image-2.png ...]
