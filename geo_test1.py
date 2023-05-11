import os
import shutil


new_path = "D:\\datasets\\coco128\\images\\train2017\\"
old_path = "D:\\datasets\\coco128\\images\\old_folder\\"


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)

            # 폴더면 들어가서 더 해
            if os.path.isdir(full_filename):
                # 진행도 확인
                search(full_filename)

            else:
                img_filename = f"{os.path.splitext(filename)[0]}.jpg"
                shutil.move(f"{old_path}{img_filename}", f"{new_path}{img_filename}")
                print(full_filename)

    except PermissionError:
        pass


search("D:\\datasets\\coco128\\labels\\train2017")
