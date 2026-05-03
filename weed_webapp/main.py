from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import io
import time
from PIL import Image

#testing

app = FastAPI(title="AI-Based Weed Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Weed-Count", "X-Processing-Time-ms"]
)

model = YOLO("best.pt")

@app.get("/health")
def health_check():
    return {"status": "Weed Detection API Running Successfully"}


@app.post("/predict")
async def predict_image(
    file: UploadFile = File(...),
    conf: float = 0.25
):
    if not file.content_type.startswith("image/"):
        return {"error": "Please upload a valid image file"}

    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    start_time = time.time()

    results = model(image, conf=conf)
    result = results[0]

    weed_count = 0
    crop_count = 0

    weed_count = 0

    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        if class_name.lower() == "weed":
            weed_count += 1

    end_time = time.time()
    processing_time = round((end_time - start_time) * 1000, 2)

    plotted_image = result.plot()
    output_image = Image.fromarray(plotted_image)

    img_byte_arr = io.BytesIO()
    output_image.save(img_byte_arr, format="JPEG")
    img_byte_arr.seek(0)

    headers = {
        "X-Weed-Count": str(weed_count),
        "X-Processing-Time-ms": str(processing_time)
    }

    return StreamingResponse(
        img_byte_arr,
        media_type="image/jpeg",
        headers=headers
    )