# pylint: disable=all
# mypy: ignore-errors
import ctypes
import os
from ctypes import wintypes

import win32api
import win32con
import win32gui
import win32ui
from PIL import Image

# Load the shell32.dll and user32.dll libraries
shell32 = ctypes.windll.shell32
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32  # Add this line


def save_icon(exe_file, out_file):
    ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
    ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

    large, small = win32gui.ExtractIconEx(exe_file, 0)
    win32gui.DestroyIcon(large[0])

    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_y)
    hdc_mem = hdc.CreateCompatibleDC()

    hdc_mem.SelectObject(hbmp)
    hdc_mem.DrawIcon((0, 0), small[0])
    hbmp.SaveBitmapFile(hdc_mem, out_file)


def extract_icon_from_shell(file_path, out_file):
    shell_dll = win32api.LoadLibraryEx("shell32.dll", 0, win32con.LOAD_LIBRARY_AS_DATAFILE)
    icon_index = 0  # Index of the icon within shell32.dll

    icon_handle = win32gui.ExtractIconEx(shell_dll, icon_index)
    if icon_handle:
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()

        ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
        ico_y = win32api.GetSystemMetrics(win32con.SM_CYICON)

        hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_y)
        hdc_mem = hdc.CreateCompatibleDC()

        hdc_mem.SelectObject(hbmp)
        hdc_mem.DrawIcon((0, 0), icon_handle[0])
        hbmp.SaveBitmapFile(hdc_mem, out_file)

        win32gui.DestroyIcon(icon_handle[0])


# Define the ICONINFO structure manually
class ICONINFO(ctypes.Structure):
    _fields_ = [
        ("fIcon", ctypes.c_bool),
        ("xHotspot", ctypes.c_uint),
        ("yHotspot", ctypes.c_uint),
        ("hbmMask", wintypes.HBITMAP),
        ("hbmColor", wintypes.HBITMAP),
    ]


# Define SHFILEINFOW structure manually
class SHFILEINFOW(ctypes.Structure):
    _fields_ = [
        ("hIcon", wintypes.HICON),
        ("iIcon", ctypes.c_int),
        ("dwAttributes", ctypes.c_uint),
        ("szDisplayName", ctypes.c_wchar_p),
        ("szTypeName", ctypes.c_wchar_p),
    ]


# Define constants manually
LR_LOADFROMFILE = 0x00000010

# Define constants manually
SHGFI_ICON = 0x000000100
SHGFI_USEFILEATTRIBUTES = 0x000000010


# Define the function to get the icon from shell32.dll
def get_file_extension_icon(file_path):
    _, file_extension = os.path.splitext(file_path)

    # Remove the leading dot from the extension
    file_extension = file_extension[1:].lower()

    # Create a SHFILEINFOW structure instance
    shinfo = SHFILEINFOW()
    flags = SHGFI_ICON | SHGFI_USEFILEATTRIBUTES

    # Get the icon index based on the file extension
    icon_index = shell32.SHGetFileInfoW(
        file_extension.encode("utf-16"), 0, ctypes.byref(shinfo), ctypes.sizeof(shinfo), flags
    )

    # Extract the icon handle from the structure
    icon_handle = shinfo.hIcon

    return icon_handle


# Usage example
# executable_path = "E:\\Games\\Steam\\steamapps\\common\\Left 4 Dead 2\\left4dead2.exe"
# executable_path = "D:\\Pictures\\Memes\\'would' cat.jpg"
# save_icon(executable_path, output_bitmap_path)
file_path = "E:\\Games\\Steam\\steamapps\\common\\Left 4 Dead 2\\left4dead2.exe"
# file_path = "D:\\Pictures\\Memes\\'would' cat.jpg"
output_bitmap_path = "output_bitmap.bmp"
# extract_icon_from_shell(file_path, output_bitmap_path)


# Example usage
# file_path = "C:\\path\\to\\your\\file.txt"  # Replace with your file path
icon_handle = get_file_extension_icon(file_path)


# Save the icon as an image file
output_bitmap_path = "icon.bmp"
if icon_handle:
    icon_info = ICONINFO()
    user32.GetIconInfo(icon_handle, ctypes.byref(icon_info))
    hbmColor = icon_info.hbmColor

    # Create a BITMAPINFOHEADER structure manually
    class BITMAPINFOHEADER(ctypes.Structure):
        _fields_ = [
            ("biSize", ctypes.c_uint32),
            ("biWidth", ctypes.c_long),
            ("biHeight", ctypes.c_long),
            ("biPlanes", ctypes.c_uint16),
            ("biBitCount", ctypes.c_uint16),
            ("biCompression", ctypes.c_uint32),
            ("biSizeImage", ctypes.c_uint32),
            ("biXPelsPerMeter", ctypes.c_long),
            ("biYPelsPerMeter", ctypes.c_long),
            ("biClrUsed", ctypes.c_uint32),
            ("biClrImportant", ctypes.c_uint32),
        ]

    bmp_info = BITMAPINFOHEADER()
    bmp_info.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    hdc = user32.GetDC(None)
    gdi32.GetDIBits(hdc, hbmColor, 0, 0, None, ctypes.byref(bmp_info), 0)
    bmp_data = ctypes.create_string_buffer(bmp_info.biSizeImage)
    gdi32.GetDIBits(hdc, hbmColor, 0, bmp_info.biHeight, bmp_data, ctypes.byref(bmp_info), 0)
    user32.ReleaseDC(None, hdc)

    with open(output_bitmap_path, "wb") as bmp_file:
        bmp_file.write(bmp_data)

# Display the icon using the icon_handle
if icon_handle:
    # Display the icon, or you can use it in your application
    # shell32.DestroyIcon(icon_handle)
    user32.DestroyIcon(icon_handle)
    print("yes")
else:
    print("no")
