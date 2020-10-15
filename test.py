import cv2 as cv

"""
Mind :
cv.imread(filename)
cv.imwrite(filename, img)
cv.imshow('image', img)
cv.waitKey()
"""

def grey_to_ascii(image):
    tab_ascii = ['@','%','#','a','i',':','.']
    result = []
    for line in image:
        result_line = []
        for pixel in line:
            intensity = int(pixel*len(tab_ascii)/255)
            if intensity == len(tab_ascii):
                intensity -= 1
            result_line.append(tab_ascii[intensity])
        result.append(result_line)
    return result

# directory = input("access path of the image : ")
directory = 'aaa.jpg'
image_input = cv.imread(directory)
res = cv.cvtColor(image_input, cv.COLOR_BGR2GRAY)
# cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
# cv.imshow('image', res)
# cv.waitKey()
ascii = grey_to_ascii(res)
print(len(ascii), len(ascii[0]))
fichier = open("output.txt", "w")
for i in range(len(ascii)):
    for j in range(len(ascii[0])):
        fichier.write(ascii[i][j])
    fichier.write('\n')

fichier.close()
