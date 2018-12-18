import numpy as np
from .BoxBlur import BoxBlur_random
from .DefocusBlur import DefocusBlur_random
from .GaussianBlur import GaussianBlur_random
from .LinearMotionBlur import LinearMotionBlur_random
from .PsfBlur import PsfBlur_random


blurFunctions = {"0": BoxBlur_random, "1": DefocusBlur_random,
                 "2": GaussianBlur_random, "3": LinearMotionBlur_random, "4": PsfBlur_random}


def RandomizedBlur(img):
    choice = np.random.choice(len(blurFunctions), 1, p=[
                              0.00, 0.00, 0.3, 0.2, 0.5])[0]
    blurToApply = blurFunctions[str(choice)]
    return blurToApply(img)
