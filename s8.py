import cv2
path = 'numpy.jpg'
image = cv2.imread(path)
window_name = 'Image'
start_point = (1, 165)
end_point = (300, 1)
color = (0, 0, 0)
thickness = 5
image = cv2.line(image, start_point, end_point, color, thickness)
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
