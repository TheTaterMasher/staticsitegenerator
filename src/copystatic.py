import os
import shutil

def copy_dir(src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    
    for item in os.listdir(src_dir):
        item_src = os.path.join(src_dir, item)
        item_dst = os.path.join(dst_dir, item)
        if os.path.isfile(item_src):
            shutil.copy(item_src, item_dst)
        else:
            copy_dir(item_src, item_dst)