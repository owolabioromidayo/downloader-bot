import os, requests, smtplib, ssl, base64
from flask import Flask, request


def download_raw_bytes(url):
    r = requests.get(url, stream=True)
    print(r)
    with open('download', 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
                f.write(chunk)


    with open('download', 'rb') as binary_file:
        binary_file_data  = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')
        return base64_message


app = Flask(__name__)

@app.route('/video', methods=["POST"])
def download_video():
        req = request.get_json()
        print(req)
        base64_message = download_raw_bytes(req['url'])	
        print(base64_message)
        send_mail(req['mail'], base64_message)
        
        
        return "done", 200


def check_mail():
	pass

def send_mail(receiver, message):
    
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
   
    print(MAIL_USERNAME, MAIL_PASSWORD)
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.sendmail(MAIL_USERNAME, receiver, message)


if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8000, debug=False)
