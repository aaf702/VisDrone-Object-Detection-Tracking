
from ultralytics import YOLO

model = YOLO("best.pt")

model.track(
    source="test_video.mp4",
    tracker="bytetrack.yaml",
    imgsz=960,
    conf=0.05,
    iou=0.5,
    max_det=300,
    persist=True,
    save=True
)
