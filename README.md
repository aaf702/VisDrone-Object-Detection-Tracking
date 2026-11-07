
# VisDrone Object Detection and Tracking

## Project Overview
This project focuses on detecting and tracking objects in drone footage using the VisDrone2019 dataset.

The object detection model is YOLO11s, and ByteTrack is used for object tracking.

## Model Information
- Model: YOLO11s
- Dataset: VisDrone2019
- Number of classes: 11
- Training image size: 960
- Training epochs: 100
- Batch size: 8
- Optimizer: AdamW
- Tracking algorithm: ByteTrack

## Detection Classes
1. Pedestrian
2. People
3. Bicycle
4. Car
5. Van
6. Truck
7. Tricycle
8. Awning-tricycle
9. Bus
10. Motor
11. Others

## Training Results
The recorded model results:

- mAP50: 50.09%
- mAP50-95: 30.22%
- Precision: 60.23%
- Recall: 48.23%

These results are from the validation evaluation.

## Project Structure

```text
VisDrone-Object-Detection-Tracking/
├── weights/
│   └── best.pt
├── track_webcam.py
├── detect_video.py
├── train.py
├── requirements.txt
└── README.md
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run Webcam Tracking

```bash
python track_webcam.py
```

## Run Video Tracking

Place your video in the project directory as `test_video.mp4`, then run:

```bash
python detect_video.py
```

## Model Weights

The trained model is available in:

`weights/best.pt`

## Acknowledgment

Dataset: VisDrone2019
Model framework: Ultralytics YOLO
Tracking algorithm: ByteTrack
