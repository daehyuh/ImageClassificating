import json
import os
import cv2


for root, dirs, files in os.walk('1/obstacle_old'):
    for fname in files:
        full_fname = os.path.join(root, fname)
        image_nm, ext = os.path.splitext(full_fname)
        if "png" in ext:
            print(full_fname)
            img = cv2.imread(full_fname)
            h, w, c = img.shape
            cv2.putText(img, str(full_fname), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            cv2.imshow('Input image', img)

            if "drive" not in full_fname and "stop" not in full_fname and "undecided" not in full_fname:
                img = cv2.resize(img, (int(w / 2), int(h / 2)))
                cv2.imshow('Input image', img)
                result = cv2.waitKey(0)

                # print(result)
                if result == 49:  # 1 KEY
                    os.rename(full_fname, image_nm + '_drive' + ext)
                if result == 50:  # 2 KEY
                    os.rename(full_fname, image_nm + '_stop' + ext)
                if result == 51:  # 3 KEY
                    os.rename(full_fname, image_nm + '_undecided' + ext)
                if result == 52:  # 4 KEY
                    pass
                if result == 24:  # ctrl+x
                    print(image_nm + ext)
                    os.remove(image_nm + ext)
            else:
                if os.path.isfile(image_nm + ".json"):
                    file = open(image_nm + ".json")
                    jsonString = json.load(file)
                    p1, p2 = jsonString.get("shapes")[0]['points']
                    cv2.rectangle(img, (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1])), (255, 0, 255), 3)
                    if p1[0] < p2[0]:
                        ptx1 = p1[0]
                        ptx2 = p2[0]
                    else:
                        ptx1 = p2[0]
                        ptx2 = p1[0]

                    if p1[1] < p2[1]:
                        pty1 = p2[1]
                        pty2 = p2[1]
                    else:
                        pty1 = p1[1]
                        pty2 = p1[1]

                    cv2.line(img, (int(ptx1), int(pty1)), (0, h), (255, 255, 255), 3)
                    cv2.line(img, (int(ptx2), int(pty2)), (w, h), (255, 255, 255), 3)
                    cv2.line(img, (0, h), (w, h), (255, 255, 255), 5)
                img = cv2.resize(img, (int(w / 2), int(h / 2)))
                cv2.imshow('Input image', img)
                result = cv2.waitKey(0)

            if result == 27:  # ESC KEY
                cv2.destroyAllWindows()
                exit()
