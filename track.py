
from ultralytics import YOLO

model = YOLO("best.pt")

model.track(
    source="test_video.mp4",
    tracker="bytetrack_custom.yaml",
    imgsz=960,
    conf=0.05,
    iou=0.5,
    persist=True,
    save=True
)
