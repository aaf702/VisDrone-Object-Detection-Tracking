from ultralytics import YOLO

model = YOLO("best.pt")

model.predict(
    source="test_video.mp4",
    imgsz=960,
    conf=0.25,
    save=True
)
