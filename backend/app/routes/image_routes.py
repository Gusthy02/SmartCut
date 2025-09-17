from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import Response
from app.services import image_processor

router = APIRouter()

@router.post("/process")
async def process_image(
    file: UploadFile = File(...),
    haircut: str | None = None
):
    try:
        image_bytes = await file.read()
        output_bytes = image_processor.process_image(
            image_bytes=image_bytes,
            haircut_filename=haircut
        )
        return Response(content=output_bytes, media_type="image/jpeg")
    except image_processor.ProcessingError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/haircuts")
async def list_haircuts():
    return {"haircuts": image_processor.list_available_haircuts()}
