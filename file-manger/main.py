from flask import Flask , render_template , request , redirect , url_for , send_from_directory
import os
import qrcode
import webbrowser
import socket

def make_qr_code():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(ip)
    ip = (s.getsockname()[0])
    url = f"http://{ip}/"
    qr = qrcode.QRCode(version = 1,
                    box_size = 100,
                    border = 5)
    qr.add_data(url)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'red',
                        back_color = 'white')
    img.save('url_qr.png')
app = Flask(__name__ )
app.config.from_object(__name__)
def kir_to_flask(file_name):
    with open(str(file_name),"rb") as f1:
        with open(f"static/{file_name}","wb") as f2:
            f2.write(f1.read())
            pass
    os.remove(f"./{file_name}")
        
@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        file_name = request.files["file_name"]
        if not file_name in os.listdir("."):
            file_name.save(file_name.filename)
            kir_to_flask(file_name.filename)
            print(0)
        print(1)
        return redirect(url_for("home"))
    else:
        return render_template("index.html")
@app.route("/lib")
def library():
    return render_template("library.html" , files = [ str(file) for file in os.listdir("./static")])
@app.route("/show/<path:path>")
def show(path):
    return send_from_directory("static",path)
make_qr_code()
webbrowser.open_new("url_qr.png")
app.run(host="0.0.0.0",port=80,debug=False)