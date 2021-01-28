import pyzbar.pyzbar as pyzbar
import cv2
from sys import argv, exit

if len(argv) < 2:
    print("Usage: qrcode.py <filename>. Try again")
    exit(1)
else:
    filenames = argv[1:]
    datas = []
    iserror = []
    for filename in filenames:
        im = cv2.imread(filename)
        data = pyzbar.decode(im)[0].data if im is not None else ""
        if im is None or not data:
            iserror.append(True)
        else:
            iserror.append(False)
        datas.append(data)
    for i in range(len(filenames)):
        if not iserror[i]:
            print("Decoded", filenames[i])
            print("\t", datas[i], "\n")
        else:
            print("Error", filenames[i])
            print("\tImage is unreadable or non-exist or in unsupported format.\n")
    errorcnt = sum(iserror)
    print(f"{errorcnt if errorcnt else 'No'} errors found.")
