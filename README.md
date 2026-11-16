# VisDrone Object Detection, Tracking and IBVS

## Project Overview

This project explores three computer vision and control techniques for drone applications using the VisDrone2019 dataset:

1. **YOLO11s:** Object detection in aerial images and videos.
2. **ByteTrack:** Multi-object tracking across consecutive video frames.
3. **IBVS:** Image-based visual servoing for calculating target-following motion commands.

## 1. YOLO11s – Object Detection

YOLO11s is trained on the VisDrone2019 dataset to detect 11 object classes in aerial imagery.

**Training Configuration**

| Parameter | Value |
|---|---|
| Model | YOLO11s |
| Image Size | 960 |
| Epochs | 100 |
| Batch Size | 8 |
| Optimizer | AdamW |
| Number of Classes | 11 |

**Detection Classes:** Pedestrian, People, Bicycle, Car, Van, Truck, Tricycle, Awning-tricycle, Bus, Motor, and Others.

The trained model weights are provided in `best.pt`.

**Reported Validation Results**

| Metric | Result |
|---|---:|
| Precision | 60.23% |
| Recall | 48.23% |
| mAP50 | 50.09% |
| mAP50-95 | 30.22% |

## 2. ByteTrack – Multi-Object Tracking

ByteTrack is used with YOLO11s detections to associate objects across consecutive frames.

It assigns tracking IDs and maintains object identities over time, including through some low-confidence detections.

Tracking parameters are configured in `bytetrack_custom.yaml`.

## 3. IBVS – Image-Based Visual Servoing

IBVS calculates drone motion commands using visual information extracted from the target's bounding box.

The implementation uses three image features:

- Horizontal target position.
- Vertical target position.
- Apparent target size.

An interaction matrix is used to calculate motion commands that reduce the image-space error between the current and desired target features.

The implementation uses a simplified translational IBVS model and returns three project-specific motion components: `r`, `f`, and `u`.

## Repository Structure

```text
VisDrone-Object-Detection-Tracking/
│
├── README.md
├── best.pt
├── data.yaml
├── train.py
├── detect.py
├── track.py
├── bytetrack_custom.yaml
└── ibvs.py
```

## Dataset

The project uses the VisDrone2019 dataset.

The dataset is not included in this repository due to its size.

## 🎥 Project Demo

Watch the project demonstration video:

[▶️ Watch Project Demo](https://drive.google.com/file/d/1UE5Uap--_7_yeaEwG-Sv6xtPFhWmS7fs/view?usp=sharing)

