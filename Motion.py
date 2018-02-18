import cv2
import numpy as np

video = cv2.VideoCapture('ball.mp4')
mt = []
ot = np.zeros((720, 1280))
vt = np.zeros((720, 1280))
dt = np.zeros((720, 1280))
N = 3

while True:

    ret, frame = video.read()
    height, width = frame.shape[0], frame.shape[1]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 1)

    if mt==[]:
        mt = gray


    for i in range(height):
        for j in range(width):
            if mt[i][j] < gray[i][j]:
                mt[i][j]+=1
            elif mt[i][j] > gray[i][j]:
                mt[i][j]-=1

            ot[i][j] = abs(mt[i][j] - gray[i][j])

            if ot[i][j]!=0:
                if vt[i][j] < N*ot[i][j]:
                    vt[i][j]+=1
                elif vt[i][j] > N*ot[i][j]:
                    vt[i][j]-=1

            if ot[i][j] < vt[i][j]:
                dt[i][j] = 0
            else:
                dt[i][j] = 1

    cv2.imshow('motion', dt)


    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()