import cv2
import numpy as np

# Load the image
image = cv2.imread('open_cv/image/cat.jpg')

# Check if image loaded successfully
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Set center and size of the star
center = (image.shape[1] // 2, image.shape[0] // 2)
size = 500

# Define 10 points of a 5-pointed star
angle = np.deg2rad(36)  # 360/10
points = []
for i in range(10):
    r = size if i % 2 == 0 else size // 2
    theta = i * angle - np.pi / 2  # Start pointing upward
    x = int(center[0] + r * np.cos(theta))
    y = int(center[1] + r * np.sin(theta))
    points.append((x, y))

# Convert to numpy array and draw the star
points = np.array(points, np.int32)
cv2.polylines(image, [points], isClosed=True, color=(0, 255, 255), thickness=200)

# Show the image
cv2.imshow("Image with Star", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save the image
# cv2.imwrite("star_output.jpg", image)
