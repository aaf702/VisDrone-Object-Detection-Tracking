
# VisDrone Object Detection, Tracking and IBVS

## Project Overview

This project focuses on computer vision and visual control for autonomous drone applications using the VisDrone2019 dataset.

The project contains three main algorithms:

1. YOLO11s for Object Detection.
2. ByteTrack for Multi-Object Tracking.
3. Image-Based Visual Servoing (IBVS) for visual target-following control.

The objective is to detect objects in aerial images, track them across video frames, and calculate motion commands based on the selected target's position in the camera image.

---

## 1. Object Detection - YOLO11s

YOLO11s is used to detect objects in aerial images and videos.

### Model Information

- Model: YOLO11s
- Dataset: VisDrone2019
- Number of classes: 11
- Training image size: 960
- Training epochs: 100
- Batch size: 8
- Optimizer: AdamW

### Detection Classes

| ID | Class |
|---|---|
| 0 | Pedestrian |
| 1 | People |
| 2 | Bicycle |
| 3 | Car |
| 4 | Van |
| 5 | Truck |
| 6 | Tricycle |
| 7 | Awning-tricycle |
| 8 | Bus |
| 9 | Motor |
| 10 | Others |

### Model Weights

The trained model is provided as:

`best.pt`

---

## 2. Multi-Object Tracking - ByteTrack

ByteTrack is used to associate detected objects across consecutive video frames.

It assigns tracking IDs to detected objects and attempts to maintain their identities over time.

### Main Features

- Multi-object tracking.
- Persistent object IDs.
- Association of detections between frames.
- Customizable tracking thresholds.

### Configuration

The custom tracking parameters are stored in:

`bytetrack_custom.yaml`

The tracking implementation uses YOLO11s detections as input to ByteTrack.

---

## 3. Image-Based Visual Servoing - IBVS

IBVS is used to calculate camera-relative motion commands based on image features.

The algorithm uses the selected target's bounding box to calculate:

- Horizontal image position.
- Vertical image position.
- Apparent target size.
- Image feature error.

An interaction matrix is then used to calculate motion commands that aim to reduce the image-space error.

### IBVS Inputs

- Target bounding box.
- Image width and height.
- Camera field of view.
- Desired target area.
- Control gain.
- Reference distance.

### IBVS Outputs

The function returns three project-specific motion command components:

- `r`: First motion component.
- `f`: Forward motion component.
- `u`: Vertical motion component.

The IBVS implementation is provided independently in:

`ibvs.py`

It calculates motion commands but does not directly control a physical drone by itself.

---

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
├── ibvs.py
└── requirements.txt
```

---

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## Running the Algorithms

### Object Detection

```bash
python detect.py
```

### Object Tracking

```bash
python track.py
```

Make sure the input video path is configured in the corresponding script.

### IBVS

Example:

```python
from ibvs import ibvs

target = {
    "box": [400, 200, 560, 360]
}

config = {
    "fov": 60.0,
    "area": 0.02,
    "z": 25.0,
    "lam": 0.8,
    "theta": 55.0
}

commands, error = ibvs(
    target,
    image_width=960,
    image_height=540,
    cfg=config
)

print(commands)
```

---

## Dataset

The project uses the VisDrone2019 dataset.

The dataset is not included in this repository because of its size.

The dataset must be prepared in YOLO format before training.

Expected dataset structure:

```text
VisDrone-YOLO/
│
├── images/
│   ├── train/
│   └── val/
│
└── labels/
    ├── train/
    └── val/
```

Update the dataset path in `data.yaml` according to your local dataset location.

---

## Reported Detection Results

The current project README records the following validation metrics:

| Metric | Result |
|---|---:|
| Precision | 60.23% |
| Recall | 48.23% |
| mAP50 | 50.09% |
| mAP50-95 | 30.22% |

These are the results reported for the trained YOLO11s model.

---

## Technologies Used

- Python
- Ultralytics YOLO11s
- ByteTrack
- NumPy
- OpenCV
- Image-Based Visual Servoing (IBVS)

---

## Acknowledgments

- VisDrone2019 Dataset
- Ultralytics YOLO Framework
- ByteTrack Multi-Object Tracking
