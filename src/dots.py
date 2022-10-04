import cv2

clue_1 = cv2.imread('data/dot/CTC_1_Rotate.png', 0)
# clue_2 = cv2.imread('data/dot/CTC_2_Rotate.png', 0)
# clue_3 = cv2.imread('data/dot/CTC_3_Rotate.png', 0)
# clue_4 = cv2.imread('data/dot/CTC_4_Rotate.png', 0)

th, threshed = cv2.threshold(clue_1, 100, 255,
                             cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

cnts = cv2.findContours(threshed, cv2.RETR_LIST,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]

s1 = 3
s2 = 20
xcnts = []
for cnt in cnts:
    if s1<cv2.contourArea(cnt) <s2:
        xcnts.append(cnt)


print("\nDots number: {}".format(len(xcnts)))
