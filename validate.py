import argparse
from ultralytics import YOLO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', default='weights/yolov8n-face-lindevs.pt', help='Weights path')
    parser.add_argument('--data', default='data/widerface.yaml', help='Path to data file')
    parser.add_argument('--device', default='0', help='CUDA device, i.e. 0 or 0,1,2,3 or cpu')
    opt = parser.parse_args()

    model = YOLO(opt.weights)
    metrics = model.val(data=opt.data, device=opt.device)

    print('map50-95: ' + str(metrics.box.map))
