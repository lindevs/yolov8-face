import argparse
import cv2
import numpy as np


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='weights/yolov8n-face-lindevs.onnx', help='Weights path')
    parser.add_argument('--source', type=str, default='data/images/bus.jpg')
    parser.add_argument('--imgsz', type=int, default=640, help='Image size')
    parser.add_argument('--conf', type=float, default=0.75, help='Object confidence threshold for detection')
    parser.add_argument('--iou', type=float, default=0.7, help='Intersection over union (IoU) threshold for NMS')
    parser.add_argument('--device', type=str, default='0', help='CUDA device, i.e. 0 or 0,1,2,3 or cpu')
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

    outputs = np.array([cv2.transpose(outputs[0])])

    bboxes = []
    scores = []
    for i in range(outputs.shape[1]):
        _, max_score, _, _ = cv2.minMaxLoc(outputs[0][i][4:])
        if max_score >= opt.conf:
            bbox = [
                outputs[0][i][0] - (0.5 * outputs[0][i][2]),
                outputs[0][i][1] - (0.5 * outputs[0][i][3]),
                outputs[0][i][2],
                outputs[0][i][3],
            ]
            bboxes.append(bbox)
            scores.append(max_score)

    results = cv2.dnn.NMSBoxes(bboxes, scores, opt.conf, opt.iou)

    color = [0, 255, 0]
    for i in range(len(results)):
        idx = results[i]
        x1 = round(bboxes[idx][0] * scale)
        y1 = round(bboxes[idx][1] * scale)
        w = round(bboxes[idx][2] * scale)
        h = round(bboxes[idx][3] * scale)
        label = '%.2f' % scores[idx]

        cv2.rectangle(img, (x1, y1, w, h), color, 1, cv2.LINE_AA)
        cv2.putText(img, label, (x1 - 5, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
