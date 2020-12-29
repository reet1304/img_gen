#!usr/bin/env python3

from img_gen import insert_text_center
import os
import sys
import csv

if __name__ == '__main__':
    background_dir = sys.argv[1]
    assert os.path.isdir(background_dir)
    background_paths = [os.path.join(background_dir, path) for path in os.listdir(background_dir)]
    # for path in os.listdir(backs_dir):
    #     print(os.path.join(backs_dir ,path))

#    predictions = list(csv.reader(open("assets/2021_n.csv", 'r'), delimiter=';'))

    while True:
        prediction = input()
        for background in background_paths:
            print("show with background: ", background)
            insert_text_center(background, 'arial.ttf' ,prediction.replace('@', '\n')).show()

