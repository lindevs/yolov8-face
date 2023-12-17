import argparse
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', default='data/widerface.yaml.example')
    opt = parser.parse_args()

    filename = os.path.splitext(os.path.relpath(opt.example))[0]

    with open(opt.example, 'r') as fin:
        with open(filename, 'w') as fout:
            fout.write(fin.read().replace('PROJECT_DIR', os.getcwd()))
