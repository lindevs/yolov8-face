import argparse
import cv2
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', default='weights/yolov8n-face-lindevs.onnx', help='Weights path')
    parser.add_argument('--source', default='data/images/bus.jpg')
    parser.add_argument('--imgsz', type=int, default=640, help='Image size')
    parser.add_argument('--conf', type=float, default=0.75, help='Object confidence threshold for detection')
    parser.add_argument('--iou', type=float, default=0.7, help='Intersection over union (IoU) threshold for NMS')
    parser.add_argument('--device', default='0', help='CUDA device, i.e. 0 or 0,1,2,3 or cpu')
    opt = parser.parse_args()

    model = cv2.dnn.readNetFromONNX(opt.weights)

    img = cv2.imread(opt.source)

    height, width, _ = img.shape
    length = max((height, width))
    scale = length / opt.imgsz
    blob = np.zeros((length, length, 3), np.uint8)
    blob[0:height, 0:width] = img
    blob = cv2.dnn.blobFromImage(blob, scalefactor=1 / 255, size=(opt.imgsz, opt.imgsz), swapRB=True)

    model.setInput(blob)
    outputs = model.forward()

    outputs = cv2.transpose(outputs[0])

    boxes = []
    scores = []
    for i in range(outputs.shape[0]):
        max_score = float(np.amax(outputs[i][4:]))
        if max_score >= opt.conf:
            boxes.append(
                [
                    (outputs[i][0] - (0.5 * outputs[i][2])) * scale,
                    (outputs[i][1] - (0.5 * outputs[i][3])) * scale,
                    outputs[i][2] * scale,
                    outputs[i][3] * scale,
                ]
            )
            scores.append(max_score)

    results = cv2.dnn.NMSBoxes(boxes, scores, opt.conf, opt.iou)

    color = [0, 255, 0]
    for i in range(len(results)):
        idx = results[i]
        x = round(boxes[idx][0])
        y = round(boxes[idx][1])
        w = round(boxes[idx][2])
        h = round(boxes[idx][3])
        label = '%.2f' % scores[idx]

        cv2.rectangle(img, (x, y, w, h), color, 1, cv2.LINE_AA)
        cv2.putText(img, label, (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
