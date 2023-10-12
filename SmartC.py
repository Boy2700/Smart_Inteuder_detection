
import cv2  # Import OpenCV library
import time  # Import time library
import datetime  # Import datetime library
from pygame import mixer   # Import mixer from pygame library

mixer.init() # Initialize the mixer

mixer.music.load("alert.wav")  # Load the alert sound file

cap = cv2.VideoCapture(0)  # Initialize the video capture device (0 is the default camera)

# Initialize the face and body cascade classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False   # Initialize detection flag to False
detection_stopped_time = None  # Initialize detection stopped time to None
timer_started = False   # Initialize timer started flag to False
SECONDS_TO_RECORD_AFTER_DETECTION = 5   # Define seconds to record after detection
# Get the frame size from the capture device
frame_size = (int(cap.get(3)), int(cap.get(4)))
# Define the video codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")





while True:
    _, frame = cap.read() # Capture a frame from the video capture device

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect faces in the grayscale frame
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)# Detect bodies in the grayscale frame

    
   
    
    
 # Check if there are any faces or bodies detected in the frame
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(
                f"{current_time}.mp4", fourcc, 20, frame_size)
            for (x, y, width, height) in faces:  # Draw rectangles around the detected faces and bodies
                cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
                for (x, y, width, height) in bodies:
                    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
            mixer.music.play() # Play the alert sound
            print("Started Recording!")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()  # Release the output video file
                print('Stop Recording!')
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)# Write the frame to the output video file

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)# Draw a rectangle around the detected face

    cv2.imshow("Warehouse Camera", frame)  # Display the frame

    if cv2.waitKey(1) == ord('q'): # stop the frame when q is press
        break

out.release()
cap.release()
cv2.destroyAllWindows()
