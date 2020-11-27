import numpy as np
import matplotlib.pyplot as plt
import os

if __name__ == '__main__':
    # npy 路径
    path = "C://Users//DELL//Desktop//smoke_detection//smoke_data//"
    npy_list = os.listdir(path)

    # 保存路径
    save_path = "C://Users//DELL//Desktop//smoke_detection//test_smoke_data_label//"
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    # 文件夹下每一个 npy 进行转换
    for i in range(0, len(npy_list)):
        npy_full_path = os.path.join(path, npy_list[i])

        # 加载标签集合
        label = np.load(npy_full_path)

        # txt 路径
        out_path = save_path + "label_" + str(i) + ".txt"

        # 创建 txt
        f = open(out_path, 'w')

        # 标签写入 txt
        for i in label:
            f.write(str(i[0]) + '\n')

        # 关闭 txt
        f.close()