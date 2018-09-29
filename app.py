from flask import Flask, render_template, Response
import picamera
import io
import time
    
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    """Video streaming ."""
    return render_template('index.html')

def gen(camera):
    while True:
        camera.capture('p.jpg')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               open('p.jpg').read().decode('utf-8') +
               b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    camera = picamera.PiCamera()
    camera.start_preview()
    time.sleep(1)
    
    app.run(debug=True, port=81, host='0.0.0.0',
            ssl_context=('cert.pem', 'key.pem'))
    
