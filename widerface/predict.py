import os
import argparse
from ultralytics import YOLO

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', default='weights/yolov8n-face-lindevs.pt', help='Weights path')
    parser.add_argument('--images', default='data/WIDER_val/images', help='Validation images path')
    parser.add_argument('--output', default='widerface/results', help='Results path')
    parser.add_argument('--imgsz', type=int, default=640, help='Image size')
    parser.add_argument('--conf', type=float, default=0.01, help='Object confidence threshold for detection')
    parser.add_argument('--iou', type=float, default=0.5, help='Intersection over union (IoU) threshold for NMS')
    parser.add_argument('--device', default='0', help='CUDA device, i.e. 0 or 0,1,2,3 or cpu')
    opt = parser.parse_args()

    model = YOLO(opt.weights)

    categories = os.listdir(opt.images)
    for category in categories:
        output = os.path.join(opt.output, category)
        if not os.path.isdir(output):
            os.makedirs(output)

        images_path = os.path.join(opt.images, category)
        images = os.listdir(images_path)
        for image in images:
            results = model.predict(
                os.path.join(images_path, image),
                imgsz=opt.imgsz,
                conf=opt.conf,
                iou=opt.iou,
                device=opt.device,
                verbose=False
            )

            filename = os.path.splitext(image)[0]
            content = filename + '\n' + str(results[0].boxes.shape[0]) + '\n'
            for box in results[0].boxes:
                xyxy = box.xyxy[0]
                x1 = int(xyxy[0] + 0.5)
                y1 = int(xyxy[1] + 0.5)
                x2 = int(xyxy[2] + 0.5)
                y2 = int(xyxy[3] + 0.5)
                content += '%d %d %d %d %.03f' % (x1, y1, x2 - x1, y2 - y1, box.conf[0]) + '\n'

            with open(os.path.join(output, filename + '.txt'), 'w') as file:
                file.write(content)
