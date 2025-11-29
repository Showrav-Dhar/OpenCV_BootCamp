## Demonstrating the difference between:
## - imshow() in Matplotlib (for visualization)
## - imshow() in OpenCV (for real-time computer vision)

import cv2
import matplotlib.pyplot as plt 

# Load images using OpenCV.
# Important: imread() loads images in BGR format.
bird_img = cv2.imread(r"G:\Showrav\1_SD_VScode\Open_CV_BootCamp\sample_Data\Colourful_Bird_image.png")
coke_img = cv2.imread(r"G:\Showrav\1_SD_VScode\Open_CV_BootCamp\sample_Data\coca-cola-logo.png")

# Always validate file loading. imread() returns None when it fails.
if bird_img is None or coke_img is None:
    print("Error: One or both images could not be loaded. Check file paths.")

# Convert the bird image from BGR → RGB for proper Matplotlib display.
# Matplotlib expects RGB; OpenCV stores images in BGR.
bird_rgb = cv2.cvtColor(bird_img, cv2.COLOR_BGR2RGB)

# ----------------------- MATPLOTLIB DISPLAY -----------------------

# Matplotlib renders the image inside a figure window or notebook.
# It is slower but excellent for analysis and plotting.
plt.imshow(bird_rgb)
plt.title("Showing image using matplotlib imshow")
plt.axis('off')  # removes axes for cleaner image display
plt.show()

# ----------------------- OPENCV DISPLAY (WINDOW 1) -----------------------

# Create an OpenCV window named "w1".
window1 = cv2.namedWindow("w1")

# Display the image. Note: OpenCV expects the image in BGR format.
# Using RGB will show correct colors only because bird_rgb is RGB.
cv2.imshow(window1, bird_rgb)

# Display the window for 5000 ms (5 seconds).
cv2.waitKey(5000)

# Destroy this specific window.
cv2.destroyWindow(window1)

# ----------------------- OPENCV DISPLAY (WINDOW 2) -----------------------

window2 = cv2.namedWindow("w2")
cv2.imshow(window2, coke_img)  # This image is still in BGR
cv2.waitKey(5000)
cv2.destroyWindow(window2)

# ----------------------- OPENCV DISPLAY (WINDOW 3) -----------------------

window3 = cv2.namedWindow("w3")

# Shows the image and waits indefinitely until any key is pressed.
cv2.imshow(window3, bird_rgb)
cv2.waitKey(0)
cv2.destroyWindow(window3)

# ----------------------- OPENCV DISPLAY (WINDOW 4) -----------------------

window4 = cv2.namedWindow("w4")

Alive = True
while Alive:
    # Refresh the window continuously.
    cv2.imshow(window4, coke_img)

    # waitKey(1) allows OpenCV to process window events (keyboard, close button)
    keypress = cv2.waitKey(1)

    # Window remains visible until user presses 'q'
    if keypress == ord('q'):
        Alive = False

cv2.destroyWindow(window4)

# Close all remaining OpenCV windows (safety cleanup)
cv2.destroyAllWindows()

stop = 1  # placeholder variable, not functionally required
