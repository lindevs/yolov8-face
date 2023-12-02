# YOLOv8-Face

The **YOLOv8-Face** repository provides pre-trained models designed specifically for face detection. The models have
been pre-trained by Lindevs from scratch.

## Release Notes

* **[2023-12-02]** YOLOv8n-Face, YOLOv8s-Face, YOLOv8m-Face and YOLOv8l-Face models has been added.

## Pre-trained models

The models have been trained on [WIDERFace](http://shuoyang1213.me/WIDERFACE/) dataset using NVIDIA RTX 4090.
[YOLOv8 models](https://github.com/ultralytics/ultralytics#models) were used as initial weights for training.

| Name         | Image Size<br>(pixels) | mAP<sup>val<br>50-95 | Params   | GFLOPs | Model Size (MB) | SHA-256                                                                                                                              | Link                                                                                                                                                                                                |
|--------------|------------------------|----------------------|----------|--------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| YOLOv8n-Face | 640                    | 37.5                 | 3005843  | 8.1    | 6.3<br>12.2     | a72e65818b9d61b15d6b5f58996b2391c827f4508c5725706cf61d05a9a70e49<br>3ebbeaddfe4fc51a9ab119a4c67cc6193b559b07a8104d029ba0e146fcaa2ad4 | [PyTorch](https://github.com/lindevs/model-hub/releases/latest/download/yolov8n-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/model-hub/releases/latest/download/yolov8n-face-lindevs.onnx) |
| YOLOv8s-Face | 640                    | 40.6                 | 11125971 | 28.4   | 22.5<br>44.7    | 3c9962b02c911b0ff6e4bb5d634f6e72d0d8ba24ca3442287f280ba50bfe2f73<br>0bf65e2576c05f25a5d5454b57b313d54d41495b044e94eae25bb1205e5d8d18 | [PyTorch](https://github.com/lindevs/model-hub/releases/latest/download/yolov8s-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/model-hub/releases/latest/download/yolov8s-face-lindevs.onnx) |
| YOLOv8m-Face | 640                    | 41.7                 | 25840339 | 78.7   | 52.0<br>103.6   | 2d96e2eac09fcac4a677664680beee1c210041d0eb7e2f6a434fb806d455b2dc<br>5c40fbed7e8c2328ccaca718eb9ce49e5d631ae622c275dbd569ef4feab70ebd | [PyTorch](https://github.com/lindevs/model-hub/releases/latest/download/yolov8m-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/model-hub/releases/latest/download/yolov8m-face-lindevs.onnx) |
| YOLOv8l-Face | 640                    | 42.8                 | 43607379 | 164.8  | 87.6<br>174.7   | a24036da36c2b8ce5e2985f70b3f8bc0bd1df3941f48e91ec84b48bdd73345b4<br>5037c8362da630935b35f32670b732d4d196bfcd6eff5052704bb9a568955e7f | [PyTorch](https://github.com/lindevs/model-hub/releases/latest/download/yolov8l-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/model-hub/releases/latest/download/yolov8l-face-lindevs.onnx) |

* Training results:

| Name         | Training Time | Epochs | Batch Size | Link                                                  |
|--------------|---------------|--------|------------|-------------------------------------------------------|
| YOLOv8n-Face | 2.75 hours    | 300    | 16         | [results.txt](results/train/yolov8n-face/results.txt) |
| YOLOv8s-Face | 2.68 hours    | 200    | 16         | [results.txt](results/train/yolov8s-face/results.txt) |
| YOLOv8m-Face | 3.01 hours    | 120    | 16         | [results.txt](results/train/yolov8m-face/results.txt) |
| YOLOv8l-Face | 3.97 hours    | 110    | 16         | [results.txt](results/train/yolov8l-face/results.txt) |

* Validation results on WIDERFace dataset:

| Name         | Easy  | Medium | Hard  |
|--------------|-------|--------|-------|
| YOLOv8n-Face | 93.79 | 91.82  | 79.38 |
| YOLOv8s-Face | 95.13 | 93.62  | 82.90 |
| YOLOv8m-Face | 95.73 | 94.47  | 84.55 |
| YOLOv8l-Face | 96.26 | 95.03  | 85.43 |
