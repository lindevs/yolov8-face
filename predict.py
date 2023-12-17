import argparse
from ultralytics import YOLO
from PIL import Image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', default='weights/yolov8n-face-lindevs.pt', help='Weights path')
    parser.add_argument('--source', default='data/images/bus.jpg')
    parser.add_argument('--imgsz', type=int, default=640, help='Image size')
    parser.add_argument('--conf', type=float, default=0.75, help='Object confidence threshold for detection')
    parser.add_argument('--iou', type=float, default=0.7, help='Intersection over union (IoU) threshold for NMS')
    parser.add_argument('--device', default='0', help='CUDA device, i.e. 0 or 0,1,2,3 or cpu')
    opt = parser.parse_args()

    model = YOLO(opt.weights)
    results = model.predict(
        opt.source,
        imgsz=opt.imgsz,
        conf=opt.conf,
        iou=opt.iou,
        device=opt.device,
        verbose=False
    )

    img = results[0].plot()
    img = Image.fromarray(img[..., ::-1])
    img.show()
