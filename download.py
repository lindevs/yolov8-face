import argparse
import os
import sys
import time
import urllib.request
import zipfile

start_time = 0


def show_progress(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return

    duration = time.time() - start_time
    duration_sec = round(duration)
    progress_size = int(count * block_size)
    progress_size_mib = round(progress_size / (1024 * 1024))
    total_size_mib = round(total_size / (1024 * 1024))
    speed = round(progress_size / (1024 * 1024 * duration), 2)
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write(
        f'\r{progress_size_mib} MiB/{total_size_mib} MiB ({percent}%) - {speed} MiB/s - {duration_sec} seconds passed'
    )
    sys.stdout.flush()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='data')
    opt = parser.parse_args()

    files = {
        'WIDER_train.zip': 'https://huggingface.co/datasets/wider_face/resolve/main/data/WIDER_train.zip',
        'WIDER_val.zip': 'https://huggingface.co/datasets/wider_face/resolve/main/data/WIDER_val.zip',
        'wider_face_split.zip': 'https://huggingface.co/datasets/wider_face/resolve/main/data/wider_face_split.zip',
    }

    for filename in files:
        output = os.path.join(opt.output, filename)

        print(files[filename])
        urllib.request.urlretrieve(files[filename], output, show_progress)
        print()

        with zipfile.ZipFile(output, 'r') as zip_ref:
            zip_ref.extractall(opt.output)
