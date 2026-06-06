import os

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "read_city",
    "use_unicode": True,
    "charset": "utf8mb4",
    "use_pure": True,
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(os.path.dirname(BASE_DIR), "resources")
PHOTOS_DIR = os.path.join(RESOURCES_DIR, "photos")
ICON_ICO = os.path.join(RESOURCES_DIR, "Icon.ico")
ICON_PNG = os.path.join(RESOURCES_DIR, "Icon.png")
PICTURE_PNG = os.path.join(RESOURCES_DIR, "picture.png")

COLOR_WHITE = "#FFFFFF"
COLOR_SECOND = "#ABCFCE"
COLOR_ACCENT = "#546F94"
COLOR_DISCOUNT_ROW = "#23E1EF"
COLOR_ZERO_STOCK = "#ABCFCE"