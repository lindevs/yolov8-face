import argparse
import os
import shutil
import cv2


def process(images, labels, output):
    annotations = {}
    with open(labels, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip()
            if line.endswith('.jpg'):
                filename = os.path.splitext(os.path.basename(line))[0]
                annotations[filename] = []

                image_path = os.path.join(images, line)
                shutil.copy2(image_path, output)
                img = cv2.imread(image_path)
                height, width, _ = img.shape

                continue

            data = line.split(' ')
            if len(data) == 1:
                continue

            data = [max(0, int(x)) for x in line.split(' ')]
            if data[0] > width or data[1] > height or data[2] > width or data[3] > height:
                continue

            cx = (data[0] + data[2] / 2) / width
            cy = (data[1] + data[3] / 2) / height
            w = data[2] / width
            h = data[3] / height
            label = f'0 {cx} {cy} {w} {h}'
            if label not in annotations[filename]:
                annotations[filename].append(label)

    for filename in annotations:
        with open(os.path.join(output, filename) + '.txt', 'w') as file:
            for row in annotations[filename]:
                file.write(row + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-images', default='data/WIDER_train/images')
    parser.add_argument('--val-images', default='data/WIDER_val/images')
    parser.add_argument('--train-labels', default='data/wider_face_split/wider_face_train_bbx_gt.txt')
    parser.add_argument('--val-labels', default='data/wider_face_split/wider_face_val_bbx_gt.txt')
    parser.add_argument('--output', default='data/widerface')
    opt = parser.parse_args()

    train_output = os.path.join(opt.output, 'train')
    val_output = os.path.join(opt.output, 'val')

    if not os.path.exists(train_output):
        os.makedirs(train_output)
    if not os.path.exists(val_output):
        os.makedirs(val_output)

    process(opt.train_images, opt.train_labels, train_output)
    process(opt.val_images, opt.val_labels, val_output)
