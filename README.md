# YOLOv8-Face

The **YOLOv8-Face** repository provides pre-trained models designed specifically for face detection. The models have
been pre-trained by Lindevs from scratch.

## Release Notes

* **[2023-12-09]** YOLOv8x-Face model has been added.
* **[2023-12-02]** YOLOv8n-Face, YOLOv8s-Face, YOLOv8m-Face and YOLOv8l-Face models has been added.

## Pre-trained models

The models have been trained on [WIDERFace](http://shuoyang1213.me/WIDERFACE/) dataset using NVIDIA RTX 4090.
[YOLOv8 models](https://github.com/ultralytics/ultralytics#models) were used as initial weights for training.

| Name         | Image Size<br>(pixels) | mAP<sup>val<br>50-95 | Params   | GFLOPs |
|--------------|------------------------|----------------------|----------|--------|
| YOLOv8n-Face | 640                    | 37.5                 | 3005843  | 8.1    |
| YOLOv8s-Face | 640                    | 40.6                 | 11125971 | 28.4   |
| YOLOv8m-Face | 640                    | 41.7                 | 25840339 | 78.7   |
| YOLOv8l-Face | 640                    | 42.8                 | 43607379 | 164.8  |
| YOLOv8x-Face | 640                    | 43.3                 | 68124531 | 257.4  |

* Download links:

| Name         | Model Size (MB) | Link                                                                                                                                                                                                    | SHA-256                                                                                                                              |
|--------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| YOLOv8n-Face | 6.3<br>12.2     | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8n-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8n-face-lindevs.onnx) | a72e65818b9d61b15d6b5f58996b2391c827f4508c5725706cf61d05a9a70e49<br>3ebbeaddfe4fc51a9ab119a4c67cc6193b559b07a8104d029ba0e146fcaa2ad4 |
| YOLOv8s-Face | 22.5<br>44.7    | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8s-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8s-face-lindevs.onnx) | 3c9962b02c911b0ff6e4bb5d634f6e72d0d8ba24ca3442287f280ba50bfe2f73<br>0bf65e2576c05f25a5d5454b57b313d54d41495b044e94eae25bb1205e5d8d18 |
| YOLOv8m-Face | 52.0<br>103.6   | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8m-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8m-face-lindevs.onnx) | 2d96e2eac09fcac4a677664680beee1c210041d0eb7e2f6a434fb806d455b2dc<br>5c40fbed7e8c2328ccaca718eb9ce49e5d631ae622c275dbd569ef4feab70ebd |
| YOLOv8l-Face | 87.6<br>174.7   | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8l-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8l-face-lindevs.onnx) | a24036da36c2b8ce5e2985f70b3f8bc0bd1df3941f48e91ec84b48bdd73345b4<br>5037c8362da630935b35f32670b732d4d196bfcd6eff5052704bb9a568955e7f |
| YOLOv8x-Face | 136.7<br>272.7  | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8x-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8x-face-lindevs.onnx) | 1985c9b08ee443f0fff646cc0371dbff9825415fb5e33d33bd2dc14bd73a56d7<br>28d9e9a85e8e739f824f280b0f426cc77b0984ebac6dbc30817ae8e3336ac97e |

* Training results:

| Name         | Training Time | Epochs | Batch Size | Non-default<br>parameters                        | Link                                                  |
|--------------|---------------|--------|------------|--------------------------------------------------|-------------------------------------------------------|
| YOLOv8n-Face | 2.75 hours    | 300    | 16         | -                                                | [results.txt](results/train/yolov8n-face/results.txt) |
| YOLOv8s-Face | 2.68 hours    | 200    | 16         | -                                                | [results.txt](results/train/yolov8s-face/results.txt) |
| YOLOv8m-Face | 3.01 hours    | 120    | 16         | -                                                | [results.txt](results/train/yolov8m-face/results.txt) |
| YOLOv8l-Face | 3.97 hours    | 110    | 16         | -                                                | [results.txt](results/train/yolov8l-face/results.txt) |
| YOLOv8x-Face | 13.65 hours   | 240    | 16         | optimizer='SGD'<br>lrf=1e-5<br>weight_decay=5e-3 | [results.txt](results/train/yolov8x-face/results.txt) |

* Validation results on WIDERFace dataset:

| Name         | Easy  | Medium | Hard  |
|--------------|-------|--------|-------|
| YOLOv8n-Face | 93.79 | 91.82  | 79.38 |
| YOLOv8s-Face | 95.13 | 93.62  | 82.90 |
| YOLOv8m-Face | 95.73 | 94.47  | 84.55 |
| YOLOv8l-Face | 96.26 | 95.03  | 85.43 |
| YOLOv8x-Face | 96.33 | 95.16  | 85.80 |

## Instructions

## Installation

```shell
pip install -r requirements.txt
```

## Prediction

```shell
python predict.py --weights weights/yolov8n-face-lindevs.pt --source data/images/bus.jpg
```

* OpenCV DNN

```shell
python examples/opencv-dnn-python/main.py --weights weights/yolov8n-face-lindevs.onnx --source data/images/bus.jpg
```
