from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
import PIL.ImageGrab
from time import sleep

client = OpenRGBClient()
motherboard = client.get_devices_by_type(DeviceType.MOTHERBOARD)[0]


def get_screen():
    im = PIL.ImageGrab.grab()
    return im


def set_colors(rgb_color):
    for zone in motherboard.zones:
        zone.set_color(rgb_color)


def find_dominant_color(pil_img):
    img = pil_img.copy()
    img.convert("RGB")
    img = img.resize((1, 1), resample=0)
    dominant_color = img.getpixel((0, 0))
    return dominant_color


while True:
    dc = find_dominant_color(get_screen())
    set_colors(RGBColor(dc[0], dc[1], dc[2]))
    sleep(0.001)
