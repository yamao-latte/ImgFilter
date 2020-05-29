# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:46:11 2020

@author: okuyama.takahiro
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

from django.conf import settings


def filter2d(src, kernel):
    # カーネルサイズ
    m, n = kernel.shape

    # 畳み込み演算をしない領域の幅
    d = int((m - 1) / 2)
    h, w = src.shape[0], src.shape[1]

    # 出力画像用の配列（要素は全て0）
    dst = np.zeros((h, w))

    for y in range(d, h - d):
        for x in range(d, w - d):
            # 畳み込み演算
            dst[y][x] = np.sum(src[y - d:y + d + 1, x - d:x + d + 1] * kernel)

    return dst


def convl(src, kernel):
    # カーネルサイズを取得する
    print(kernel)
    k_height, k_width = kernel.shape
    dim = int((k_height - 1) / 2)

    src_heghit, src_width = src.shape[0], src.shape[1]

    dst = np.zeros((src_heghit, src_width))
    # dst=np.ones((src_heghit,src_width))

    # print(dst)
    # print('zeros')

    for y in range(dim, src_heghit - dim):
        for x in range(dim, src_width - dim):
            # 畳み込み演算
            dst[y][x] = np.sum(src[y - dim:y + dim + 1, x - dim:x + dim + 1] * kernel)
    # print(dst)
    return dst


def conv_sum(src, kernel):
    # カーネルサイズを取得する
    k_height, k_width = kernel.shape

    # カーネルサイズから辺の半分の長さを求める
    x_dim = int((k_width) / 2)
    y_dim = int((k_height) / 2)

    # 画像サイズを求める
    src_height, src_width = src.shape[0], src.shape[1]
    # 出力データを用意する
    dst = np.zeros((src_height, src_width))

    # 上から下に走査して、畳み込み処理をする
    for y in range(0, src_height - y_dim):
        for x in range(0, src_width - x_dim):
            dst[y + y_dim][x + x_dim] = np.sum(src[y: y + y_dim * 2 - 1, x: x + x_dim * 2 - 1] * kernel)
    '''
                for m in range(0, k_height):
                a=0
                for n  in range(0, k_width):
                    a += np.sum(src[y+k_height][x+k_width]*kernel)
                print(a)
                dst[y+y_dim][x+x_dim]=a 

    '''
    # 畳み込み結果を返す
    return dst


def gaussian_kernel(n: int) -> np.ndarray:
    '''(n,n)のガウス行列を作る'''

    # [nC0, nC1, ..., nCn]を作成
    combs = [1]
    for i in range(1, n):
        ratio = (n - i) / (i)
        combs.append(combs[-1] * ratio)
    combs = np.array(combs).reshape(1, n) / (2 ** (n - 1))

    # 縦ベクトルと横ベクトルの積でガウス行列を作る
    result = combs.T.dot(combs)
    return result


def convolution_run(srcname, kernel):

    try:
        # 入力画像をグレースケールで読み込み
        gray = cv2.imread(srcname, 0)

    except:
        gray = []

    dst1 = convl(gray, kernel)
    # dst1 = conv_sum(gray, kernel)
    # 結果を出力
    cv2.imwrite(settings.BASE_DIR+"/static/media/output.png", dst1)
    return gray


def horizontal_kernel(n) -> np.ndarray:
    kernel = np.ones([n, n])
    if n == 3:
        kernel = np.array([
            [-3, -10, -3],
            [0, 0, 0],
            [3, 10, 3]], np.float32)
    elif n == 5:
        kernel = np.array([
            [5, 5, 5, 5, 5],
            [3, 3, 3, 3, 3],
            [0, 0, 0, 0, 0],
            [-3, -3, -3, -3, -3],
            [-5, -5, -5, -5, -5]], np.float32)

    return kernel


def vertical_kernel(n) -> np.ndarray:
    kernel = np.ones([n, n])
    if n == 3:
        kernel = np.array([
            [-3, 0, 3],
            [-10, 0, 10],
            [-3, 0, 3]], np.float32)
    elif n == 5:
        kernel = np.array([
            [5, 3, 0, -3, -5],
            [5, 3, 0, -3, -5],
            [5, 3, 0, -3, -5],
            [5, 3, 0, -3, -5],
            [5, 3, 0, -3, -5]], np.float32)

    return kernel


def laplacian_kernel(n) -> np.ndarray:
    kernel = np.ones([n, n])
    if n == 3:
        kernel = np.array([
                             [0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0] ], np.float32)
    elif n == 5:
        kernel = np.array([
                            [-1, -3, -4, -3, -1],
                            [-3,  0,  6,  0, -3],
                            [-4,  6, 20,  6, -4],
                            [-3,  0,  6,  0, -3],
                            [-1, -3, -4, -3, -1] ], np.float32)
    return kernel


def blur_filter(n) -> np.ndarray:
    kernel = np.ones([n, n]) / (n * n)
    return kernel


def motion_filter(n) -> np.ndarray:
    kernel = np.ones([n, n]) / (n * n)
    if n == 3:
        kernel = np.array([
                             [1/3, 0, 0],
                             [0, 1/3, 0],
                             [0, 0, 1/3]], np.float32)
    elif n == 5:
        kernel = np.array([
                            [1/5, 0, 0, 0, 0],
                            [0, 1/5, 0, 0, 0],
                            [0, 0, 1/5, 0, 0],
                            [0, 0, 0, 1/5, 0],
                            [0, 0, 0, 0, 1/5]], np.float32)
    return kernel


def handler(func, *args):
    return func(*args)


def main():
    imgname = "kousi.png"
    from PIL import Image

    # open image file
    # input_img
    try:
        # 入力画像をグレースケールで読み込み
        gray = cv2.imread(imgname, 0)
    except:
        print('faild to load %s' % imgname)
        # quit()

    if gray is None:
        print('faild to load %s' % imgname)
        # quit()

    img = gray
    img2 = gray
    print(gray)
    # img2 =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # img = cv2.resize(rgb,(28, 28), cv2.INTER_CUBIC)
    # img = mpimg.imread("kousi.png")
    # RGBフォーマットからグレースケール,二値化
    # ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    # カーネル　エッジとかぼかしとか配列の形で検出できる
    kernel = np.array([[2, 0, -2],
                       [3, 0, -3],
                       [2, 0, -2]])

    #    kernel = np.array( [[2, 3, 2],
    #                        [0, 0, 0],
    #                        [-2, -3, -2]])

    kernel = np.ones((3, 3)) / 9
    kernel = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]])

    # [-1, 0, 1],[-2, 0, 2],[-1, 0, 1]]
    # [[2, 0, -2],[3, 0, -3],[2, 0, -2]]
    # kernel = gaussian_kernel(3)
    dst2 = filter2d(img2, kernel)
    print("filter2d")
    print(dst2)
    dst1 = convl(img2, kernel)
    # 結果を出力
    cv2.imwrite("kousi5.png", dst1)

    # dst2=conv_sum(img2,kernel)
    # cv2.imwrite("output2.jpg", dst2)
    print("filter2d")
    print(dst2)

    # plt.imshow(img)
    print('dst')
    print(dst1)
    print("responsed")
    # plt.imshow(dst1)
    plt.subplot(1, 3, 1)
    plt.imshow(img, 'gray')
    plt.subplot(1, 3, 2)
    plt.imshow(dst1, 'gray')
    res = cv2.imread("kousi5.png", 0)
    plt.subplot(1, 3, 3)
    plt.imshow(res, 'gray')
    print(res)
    # cv2.imwrite("ku.png", dst2)
    # res=cv2.imread("kousi5.png", 0)

    plt.show()

    # plt.subplot(2,3,3)
    # plt.imshow(dst2,'gray')
    # plt.show()


if __name__ == '__main__':
    main()


