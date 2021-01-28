# single_nologo_qrdecode
*Decode the content of a QR/barcode.*

### To be noted:
- Support multiple QRs/barcodes (images) at once
- Only one QR/barcode allowed in an image
- No logo or other decoration inside the QR code allowed
- Images are assumed to be well-positioned (not half-rotated or skewed etc)
- Supported image formats: (see in opencv's site)[https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56]

### Usage:
`python3 qrcode.py [image-1.jpg image-2.png ...]`
