from fastapi import File, FastAPI, UploadFile
from fastapi.responses import JSONResponse
from models import Caption
import uvicorn

app = FastAPI()
captioner = Caption()

@app.post("/video_captioning")
async def video_captioning(file: UploadFile = File(...)):
    # интервалы по изменению hsv диаграммы
    # caption = captioner.shot_transit(file)
    # равномерные интервалы (12 интервалов)
    caption = captioner.shot_transit_uniform(file)
    return JSONResponse(content=caption)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)