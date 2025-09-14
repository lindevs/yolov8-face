# YOLOv8-Face

The **YOLOv8-Face** repository provides pre-trained models designed specifically for face detection. The models have
been pre-trained by Lindevs from scratch.

## Similar Projects

Other pre-trained models by Lindevs that you might find interesting:

* [YOLOv9-Face](https://github.com/lindevs/yolov9-face)

## Release Notes

* **[2024-11-01]** Re-saved and re-uploaded PyTorch models to avoid the dill package usage warning.
* **[2023-12-09]** YOLOv8x-Face model has been added.
* **[2023-12-02]** YOLOv8n-Face, YOLOv8s-Face, YOLOv8m-Face and YOLOv8l-Face models has been added.

## Pre-trained Models

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
| YOLOv8n-Face | 6.0<br>11.7     | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8n-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8n-face-lindevs.onnx) | b038ca653b503453a94f6e12d76feca6840b2a97d7a1322b4498c5e922f29832<br>8d0bfb0c3383c5bd7a78dd24ef79a21e2aa456619b6ab5e53867092d1c7dc414 |
| YOLOv8s-Face | 21.5<br>42.7    | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8s-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8s-face-lindevs.onnx) | fa7e47fe9378255e4b52cb7abc4e387c0353dd26b0b8e6834045dc9dfbaaf69f<br>0a6d19f2f68d7f0cc8104ab5c9eaa54b63e298f91dcfefd4be897f94a1561d02 |
| YOLOv8m-Face | 49.6<br>98.8    | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8m-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8m-face-lindevs.onnx) | 303dcd997fb6ed446d1626b2bbd36f146894cdf600e33c4d563124f8c1b191c4<br>652f1ee6cd0291295de3d8fcaf9375ad62ef269055c0ada458bfdc4e7e6095da |
| YOLOv8l-Face | 83.6<br>166.6   | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8l-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8l-face-lindevs.onnx) | 29cc43b27c8b865859c66489a4399a10a3efd80ce68ded9815364117641706d5<br>52dc39e46a7316398c95d30dd669a641382c9fdd8b675ad32aa65585bf820ea0 |
| YOLOv8x-Face | 130.4<br>260.1  | [PyTorch](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8x-face-lindevs.pt)<br>[ONNX](https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8x-face-lindevs.onnx) | 117c587c79e75e68a83e70200549bf6c035fa45b30e02fb41699639aadcfa0e6<br>0ddad01728bc5f7d6c68c9b5567cfd1c8257f041af607c215ed865c5442f87fa |

* Training results:

| Name         | Training Time | Epochs | Batch Size | Non-default<br>parameters                        | Link                                                  |
|--------------|---------------|--------|------------|--------------------------------------------------|-------------------------------------------------------|
| YOLOv8n-Face | 2.75 hours    | 300    | 16         | -                                                | [results.txt](results/train/yolov8n-face/results.txt) |
| YOLOv8s-Face | 2.68 hours    | 200    | 16         | -                                                | [results.txt](results/train/yolov8s-face/results.txt) |
| YOLOv8m-Face | 3.01 hours    | 120    | 16         | -                                                | [results.txt](results/train/yolov8m-face/results.txt) |
| YOLOv8l-Face | 3.97 hours    | 110    | 16         | -                                                | [results.txt](results/train/yolov8l-face/results.txt) |
| YOLOv8x-Face | 13.65 hours   | 240    | 16         | optimizer='SGD'<br>lrf=1e-5<br>weight_decay=5e-3 | [results.txt](results/train/yolov8x-face/results.txt) |

* Evaluation results on WIDERFace dataset:

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

## Export

* Install package:

```shell
pip install onnx
```

* Export to ONNX format:

```shell
python export.py --weights weights/yolov8n-face-lindevs.pt
```

* Or export to ONNX format using dynamic axis:

```shell
python export.py --weights weights/yolov8n-face-lindevs.pt --dynamic
```

## Dataset Preparation

* Download WIDERFace dataset and annotations:

```shell
python download.py
```

* Convert annotations to YOLO format:

```shell
python annotations.py
```

* Copy `widerface.yaml.example` file to `widerface.yaml`:

```shell
python data_file.py
```

## Training

* Prepare dataset.
* Start training:

```shell
python train.py --weights yolov8n.pt --epochs 300 2>&1 | tee -a results.txt
python train.py --weights yolov8s.pt --epochs 200 2>&1 | tee -a results.txt
python train.py --weights yolov8m.pt --epochs 120 2>&1 | tee -a results.txt
python train.py --weights yolov8l.pt --epochs 110 2>&1 | tee -a results.txt
python train.py --weights yolov8x.pt --epochs 240 --optimizer SGD --lrf 1e-5 --weight-decay 5e-3 2>&1 | tee -a results.txt
```

* Or resume training:

```shell
python train.py --weights runs/detect/train/weights/last.pt --resume 2>&1 | tee -a results.txt
```

## Validation

* Prepare dataset.
* Start validation:

```shell
python validate.py --weights weights/yolov8n-face-lindevs.pt
```

## WIDERFace Evaluation

* Prepare dataset.
* Start prediction on validation set:

```shell
python widerface/predict.py --weights weights/yolov8n-face-lindevs.pt
```

* Install package:

```shell
pip install Cython
```

* Build extension:

```shell
cd widerface && python setup.py build_ext --inplace && cd ..
```

* Start evaluation:

```shell
python widerface/evaluate.py
```
