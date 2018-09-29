from flask import Flask, render_template, Response
import picamera
import io
import time
    
app = Flask(__name__, template_folder='templates')
camera = picamera.PiCamera()
camera.start_preview()
time.sleep(2)
stream = io.BytesIO()

@app.route('/')
def index():
    """Video streaming ."""
    return render_template('index.html')

def gen(camera):
    while True:
        for f in camera.capture_continuous(stream, 'jpeg',
                                           use_video_port=True):
            stream.seek(0)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' +
                   stream.read() +
                   b'\r\n')
            stream.seek(0)
            stream.truncate(0)
            
@app.route('/video_feed')
def video_feed():
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':    
    app.run(debug=False, port=5000, host='0.0.0.0',
            ssl_context=('cert.pem', 'key.pem'))
    
