import sys
from ascii_converter import *

if __name__ == "__main__":
    fp_in = "convert.jpeg"
    fp_out = "out.txt"
    width = 100

    if len(sys.argv) > 1:
        fp_in = sys.argv[1]
    if len(sys.argv) > 2:
        fp_out = sys.argv[2]
    if len(sys.argv) > 3:
        if not sys.argv[3].isdigit():
            print(f"FAIL: STATUS_CODE {INVALID_WIDTH}")
            quit(INVALID_WIDTH)
        width = int(sys.argv[3])

    welcome = f'''
********************************************
*             ASCII CONVERTER              *
********************************************

PICTURE_PATH    = {fp_in}
OUT_PATH        = {fp_out}

    '''

    print(welcome)
    status_code = convert_img_to_ascii(fp_in, fp_out, width)
    if status_code == 0:
        print("SUCCESS")

    else:
        print(f"FAIL: STATUS_CODE {status_code}")

    quit(status_code)
