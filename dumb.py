import cv2



# Set up mouse callback
def update_for_save(event, x, y, flags, params):
    global image, window_name

    # On left mouse button down (i.e. when the focus goes to the window), update global variables
    if event == cv2.EVENT_LBUTTONDOWN:
        image = params[1]
        window_name = params[0]


# Images
src = cv2.imread('path/to/some/image.png')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Window params
image = None
window_name = None

# Create windows, add mouse callbacks
cv2.imshow('pic1', src)
cv2.imshow('pic2', hsv)
cv2.imshow('pic3', gray)
cv2.setMouseCallback('pic1', update_for_save, ['pic1', src])
cv2.setMouseCallback('pic2', update_for_save, ['pic2', hsv])
cv2.setMouseCallback('pic3', update_for_save, ['pic3', gray])

while True:
    key = cv2.waitKey(1) & 0xFF

    # If s key is pressed, save image specified by global variables
    if key == ord('s'):
        cv2.imwrite(window_name + '.png', image)

    # If q key is pressed, close all windows
    elif key == ord('q'):
        cv2.destroyAllWindows()
