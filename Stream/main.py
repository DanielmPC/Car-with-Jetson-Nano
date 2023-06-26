
import cv2
import time
import threading
from flask import Response, Flask, render_template

global video_frame
video_frame = None

# Use locks for thread-safe viewing of frames in multiple browsers
global thread_lock 
thread_lock = threading.Lock()

# Object flask
app = Flask(__name__)

## Funcion reescale image
def rescale_frame(frame, width, heigth):
    wid = int(frame.shape[1] * width/ 100)
    hei = int(frame.shape[0] * heigth/ 100)
    dim = (wid, hei)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def captureFrames():
    global video_frame, thread_lock

    video_capture = cv2.VideoCapture(0, cv2.CAP_GSTREAMER)
    video_capture.set(cv2.CAP_PROP_FPS, 30)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    while True and video_capture.isOpened():
        return_key, frame75 = video_capture.read()
        #time.sleep(0.01)

        # Set percent of rezise
        frame = rescale_frame(frame75, width=115, heigth=90)
        if not return_key:
            break

        with thread_lock:
            video_frame = frame.copy()
        
        key = cv2.waitKey(30) & 0xff
        if key == 27:
            break

    video_capture.release()
        
def encodeFrame():
    global thread_lock
    while True:
        # Acquire thread_lock to access the global video_frame object
        with thread_lock:
            global video_frame
            if video_frame is None:
                continue
            return_key, encoded_image = cv2.imencode(".jpg", video_frame)
            if not return_key:
                continue

        # Output image as a byte array
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
            bytearray(encoded_image) + b'\r\n')

@app.route("/")
def index():
    return Response(encodeFrame(), mimetype = "multipart/x-mixed-replace; boundary=frame")

"""@app.route("/stream")
def VideoStream():
    return Response(encodeFrame(), 
    mimetype = "multipart/x-mixed-replace; boundary=frame")"""


# check to see if this is the main thread of execution
if __name__ == '__main__':

    # Create a thread and attach the method that captures the image frames, to it
    process_thread = threading.Thread(target=captureFrames)
    process_thread.daemon = True

    # Start the threadcuale
    process_thread.start()

    app.run(host="10.42.0.1", port=8080)