import numpy as np
import scipy.misc
import cv2
import matplotlib.pyplot as plt
import os

if __name__ == '__main__':
    # npy 路径
    path = "C://Users//DELL//Desktop//smoke_detection//smoke_data//"
    npy_list = os.listdir(path)

    # 保存路径
    save_path = "C://Users//DELL//Desktop//smoke_detection//test_smoke_data_pic//"
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    # 文件夹下每一个 npy 进行转换
    for i in range(0, len(npy_list)):
        npy_full_path = os.path.join(path, npy_list[i])

        # 加载图片集合
        img = np.load(npy_full_path)

        # 对每一个 npy 下的每一张图片进行保存
        for i in range(0, 10617):
            # 获得第 i 张图片
            arr = img[i, :, :, :]

            # 保存图片
            plt.imsave(os.path.join(save_path, "{}_disp.png".format(i)), arr, cmap='plasma')


