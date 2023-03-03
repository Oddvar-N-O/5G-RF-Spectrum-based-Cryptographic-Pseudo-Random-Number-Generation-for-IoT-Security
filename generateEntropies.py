import pickle
from os.path import exists
from tqdm.auto import tqdm
import numpy as np
import matplotlib.pyplot as plt
import bitstring
import cv2
from glob import glob

files = glob('GeneratedData/NR*.png')

num_of_files = len(files)

def get_entropy_spectrum(c, k, sel_img_idx, rng):
    sel_img = files[sel_img_idx]
    img = cv2.imread(sel_img)
    start_x = rng.integers(img.shape[0] - c)
    start_y = rng.integers(img.shape[1] - k)

    selected_spectogram = img[start_x:start_x+c, start_y:start_y+k, :].flatten()
    random_bits = bitstring.BitArray(float=selected_spectogram[0], length=32)

    for i in range(1,selected_spectogram.shape[0]):
        tmp = bitstring.BitArray(float=selected_spectogram[i], length=32)
        random_bits = random_bits ^ tmp # xor
        random_bits = random_bits ^ random_bits << 13
        random_bits = random_bits ^ random_bits >> 17
        random_bits = random_bits ^ random_bits << 5
    return random_bits.uintle

rng = np.random.default_rng(12345)
entropies = []
for c in tqdm(range(1,30)):
    for k in tqdm(range(1,30)):
        temp = []
        for s in range(num_of_files):
            temp.append(get_entropy_spectrum(c,k,s, rng))
        entropies.append(temp)
file2 = open("entropies.txt", "w")
for entropy in tqdm(entropies):
  file2.write(str(entropy))
file2.close()