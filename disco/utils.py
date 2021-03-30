import os

import cv2
import random
from datetime import datetime
from matplotlib import pyplot as plt

from core import settings


def non_blank_frame(video_path):
    ap = cv2.VideoCapture(video_path)
    memory = None
    while True:
        ret, frame = ap.read()
        if frame is not None:
            cv2.imshow('frame', frame)
            if frame.std() > 1:
                memory = frame

        if cv2.waitKey(2) == ord('q'):
            break
    if memory is not None:
        sol = random.random()
        date = datetime.now()
        new_path = f"{settings.MEDIA_ROOT}/{date.strftime('%Y')}/{date.strftime('%m')}/{date.strftime('%d')}/dicso"
        os.makedirs(os.path.join(f'{settings.MEDIA_ROOT}', new_path), exist_ok=True)
        plt.imsave(f"{new_path}/{sol}-last_non_blank_frame.jpg", memory)

    cv2.destroyAllWindows()
