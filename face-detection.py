import cv2

# Load the cascade
fname = r'Z:/personal/-code-/learning-opencv/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(fname)

# Read the input image
img = cv2.imread('assets/woman-02.jpg')

# Convert into grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), ( x + w, y + h), (255, 255, 0), 3)

# Show final image
cv2.imshow('Face detection', img)

cv2.waitKey(0)
