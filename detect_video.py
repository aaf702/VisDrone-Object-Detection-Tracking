from ultralytics import YOLO

model = YOLO("weights/best.pt")

model.track(
    source="test_video.mp4",
    tracker="bytetrack.yaml",
    imgsz=640,
    conf=0.25,
    save=True,
    show=False
)
