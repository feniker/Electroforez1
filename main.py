# import numpy as np
# import cv2 as cv


# imageName = 'images/Forez1.png'
# im = cv.imread(imageName)
# assert im is not None, "file could not be read, check with os.path.exists()"


# imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(imgray, 127, 255, 0)
# im2, contours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cv.rectangle(imgray, (25,40),(60,600), (0,255,255), 1)
# cv.rectangle(imgray, (65,40),(100,600), (0,255,255), 1)
# cv.imshow('GrayForez', imgray)
# cv.waitKey(0)

import sys
import numpy as np
import cv2 as cv

hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)

if __name__ == '__main__':
    fn = 'D:\Your files\Kolesnch_D\Documents\Python Scripts\Electroforez\images\Forez1.png' # имя файла, который будем анализировать
    img = cv.imread(fn)[:100,:]

    hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    _, contours0 = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    print(contours0)

    # # перебираем все найденные контуры в цикле
    # for cnt in contours0:
    #     rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
    #     box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
    #     box = np.int0(box) # округление координат
    #     cv.drawContours(img,[box],0,(255,0,0),2) # рисуем прямоугольник

    cv.imshow('contours', img) # вывод обработанного кадра в окно

    cv.waitKey()
    cv.destroyAllWindows()