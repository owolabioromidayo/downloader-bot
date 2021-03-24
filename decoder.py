import base64, sys

def decode(filename):
    with open(filename, 'r') as f:
        base64_img = f.read()
        base64_img_bytes = base64_img.encode('utf-8')
        with open('decoded', 'wb') as savefile:
            decoded_image_data = base64.decodebytes(base64_img_bytes)
            savefile.write(decoded_image_data)

if __name__ == "__main__":
    decode(sys.argv[1])

