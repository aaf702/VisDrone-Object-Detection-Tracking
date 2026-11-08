from ultralytics import YOLO

model = YOLO("best.pt")

results = model.track(
    source=r"....",
    tracker="bytetrack.yaml",
    imgsz=960,
    conf=0.45,
    iou=0.5,
    max_det=80,
    line_width=2,
    show_conf=False,
    save=True,
    show=False,
    device="cpu",
    project="Drone_Test_Results",
    name="YOLO11s_Clean",
    exist_ok=True
)

print("processing completed!")
