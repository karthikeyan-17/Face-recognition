import cv2
import dlib
from scipy.spatial import distance

cap = cv2.VideoCapture(0)

def get_opt(val, path):
    if val == 1:
        _, frame = cap.read()
    else:
        frame = cv2.imread(path, cv2.IMREAD_COLOR)
    return frame


def get_ratio(val, path):
    hog_face_detector = dlib.get_frontal_face_detector()
    dlib_facelandmark = dlib.shape_predictor("shape_predictor_81_face_landmarks.dat")

    while True:
        frame = get_opt(val, path)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = hog_face_detector(gray)
        for face in faces:

            face_landmarks = dlib_facelandmark(gray, face)
            a = []
            for n in [71, 8]:
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y

                a.append((x, y))
                cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
            length = distance.euclidean(a[0], a[1])

            b = []
            for n in [1, 15]:
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y

                b.append((x, y))
                cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
            breadth = distance.euclidean(b[0], b[1])

            #################################

            c = []
            for n in [36, 45]:
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y

                c.append((x, y))
                cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
            l1 = distance.euclidean(c[0], c[1])

            d = []
            for n in [48, 54]:
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y

                d.append((x, y))
                cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
            l2 = distance.euclidean(d[0], d[1])

            ########################

            e = []
            for n in [31, 8]:
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y

                e.append((x, y))
                cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
            n1 = distance.euclidean(e[0], e[1])

            f = []
            for n in [55, 9]:
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y

                f.append((x, y))
                cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
            n2 = distance.euclidean(f[0], f[1])

            ########################

            g = []
            for n in [33, 66]:
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y

                g.append((x, y))
                cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
            m1 = distance.euclidean(g[0], g[1])

            h = []
            for n in [66, 8]:
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y

                h.append((x, y))
                cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
            m2 = distance.euclidean(h[0], h[1])

            ########################

            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            image = cv2.putText(frame, 'Ratio A ' + str("{:.2f}".format(l1/l2)), (30, 30), font,
                                fontScale, color, thickness, cv2.LINE_AA)
            image = cv2.putText(frame, 'Ratio B ' + str("{:.2f}".format(length/breadth)), (30,60), font,
                                fontScale, color, thickness, cv2.LINE_AA)
            image = cv2.putText(frame, 'Ratio C ' + str("{:.2f}".format(n1/n2)), (30, 90), font,
                                fontScale, color, thickness, cv2.LINE_AA)
            image = cv2.putText(frame, 'Ratio D ' + str("{:.2f}".format(m2 / m1)), (30, 120), font,
                                fontScale, color, thickness, cv2.LINE_AA)

        cv2.imshow("Face Landmarks", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
