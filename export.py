import argparse
from ultralytics import YOLO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', default='weights/yolov8n-face-lindevs.pt', help='Weights path')
    parser.add_argument('--imgsz', type=int, default=640, help='Image size')
    parser.add_argument('--device', default='0', help='CUDA device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--dynamic', action='store_true', default=False, help='Enable dynamic axis in ONNX model')
    opt = parser.parse_args()

    model = YOLO(opt.weights)
    model.export(
        format='onnx',
        imgsz=opt.imgsz,
        device=opt.device,
        dynamic=opt.dynamic
    )
