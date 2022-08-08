import datetime
import random
import cv2
import mediapipe
import scipy.spatial

drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands
distanceModule = scipy.spatial.distance
print("Launching camera")

capture = cv2.VideoCapture(0)
print("You can play now..!")

frameWidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
finished = False
score = 0

while True:
    start_time = datetime.datetime.now()
    circleRadius = 40
    circleCenter = (round(random.randint(circleRadius, frameWidth)), round(random.randint(circleRadius, frameHeight)))
    bubble = False
    if finished:
        break
    with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7,
                           max_num_hands=1) as hands:
        while True:
            ret, frame = capture.read()
            if finished:
                break
            if not ret:
                continue
            frame = cv2.flip(frame, 1)
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            circleColor = (0, 0, 255)

            if results.multi_hand_landmarks != None:
                normalizedLandmark = results.multi_hand_landmarks[0].landmark[
                    handsModule.HandLandmark.WRIST]
                pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                          normalizedLandmark.y,
                                                                                          frameWidth,
                                                                                          frameHeight)

                cv2.circle(frame, pixelCoordinatesLandmark, 10, (0, 255, 0), -1)
                # print(circleCenter, circleRadius)
                try:
                    if distanceModule.euclidean(pixelCoordinatesLandmark, circleCenter) < circleRadius:
                        circleColor = (0, 255, 0)
                        score = score + 1
                        bubble = True
                        cv2.waitKey(200)
                    else:
                        circleColor = (0, 0, 255)
                except:
                    pass
            cv2.circle(frame, circleCenter, circleRadius, circleColor, -1)
            frame = cv2.resize(frame, (740, 560))  # Resize image
            cv2.putText(frame, 'Score : {}'.format(score), (250, 550),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 125), 3)

            cv2.imshow('RPA - Dot Game', frame)
            if bubble:
                circleCenter = (round(random.randint(circleRadius, frameWidth)), round(random.randint(circleRadius, frameHeight)))
                bubble = False
            if cv2.waitKey(1) == 27 & 0xFF == ord('q'):
                break
            if (datetime.datetime.now() - start_time).seconds == 60:
                finished = True
    cv2.destroyAllWindows()
    capture.release()


print("Congrats, Your score is {}".format(score))