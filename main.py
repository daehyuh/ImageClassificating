import os
import cv2

for root, dirs, files in os.walk('obstacle'):
    for fname in files:
        full_fname = os.path.join(root, fname)
        image_nm, ext = os.path.splitext(full_fname)
        if "drive" not in full_fname and "stop" not in full_fname and "undecided" not in full_fname:
            img = cv2.imread(full_fname)
            cv2.putText(img, str(full_fname), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 3)
            cv2.imshow('Input image', img)
            result = cv2.waitKey(0)

            if result == 49:
                os.rename(full_fname, image_nm + '_drive' + ext)
            if result == 50:
                os.rename(full_fname, image_nm + '_stop' + ext)
            if result == 51:
                os.rename(full_fname, image_nm + '_undecided' + ext)
            if result == 52:
                os.remove(full_fname)
            if result == 53:
                pass