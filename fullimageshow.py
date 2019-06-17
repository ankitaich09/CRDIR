import cv2


def imshow(imageg, height, width):
    img = imageg
    dim = (height, width)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()