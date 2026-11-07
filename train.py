from ultralytics import YOLO

model = YOLO("yolo11s.pt")

model.train(
    data="/content/data_colab.yaml",
    epochs=100,
    imgsz=960,
    batch=8,
    device=0,
    workers=4,
    optimizer="AdamW",
    patience=20,
    amp=True,
    seed=42,
    project="/content/drive/MyDrive/Drone-Project/Results",
    name="YOLO11s",
    save=True,
    save_period=10,
    plots=True
)
