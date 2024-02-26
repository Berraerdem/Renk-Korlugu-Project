import cv2
import numpy as np

resim = cv2.imread("normallego.png")
"""cv2.imshow('everest', resim)
cv2.waitKey(0)"""


"""def apply_invert(resim):
    return cv2.bitwise_not(resim)"""

def verify_alpha_channel(resim):
    try:
        resim.shape[3]
    except IndexError:
        resim = cv2.cvtColor(resim, cv2.COLOR_BGR2BGRA)
    return resim

def apply_color_overlay(resim,intensity=0.2,blue=0,green=0,red=0):
    resim = verify_alpha_channel(resim)
    resim_h, resim_w, resim_c = resim.shape
    color_bgra = (blue,green,red,1)
    overlay = np.full((resim_h,resim_w, 4), color_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, resim, 1.0, 0, resim)
    resim = cv2.cvtColor(resim,cv2.COLOR_BGRA2BGR)
    return resim

def apply_sepia(resim, intensity=0.5):
    blue = 20
    green = 66
    red = 112
    resim = apply_color_overlay(resim, intensity=intensity, blue=blue, green=green, red=red)
    return resim


cv2.imshow('resim',resim)

sepia = apply_sepia(resim.copy())
cv2.imshow('sepia', sepia)

redish_color = apply_color_overlay(resim.copy(), intensity=5, red=230, blue=10)
cv2.imshow('redish_color', redish_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
