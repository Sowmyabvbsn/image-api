from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get("/")
async def generate_image(
    prompt: str = Query(None),
    model: str = Query("default")
):
    try:
        if not prompt:
            raise HTTPException(status_code=400, detail="Missing prompt")

        # Encode prompt for URL
        encoded_prompt = requests.utils.quote(prompt)

        # Free image generation API (stable)
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

        return JSONResponse(content={
            "prompt": prompt,
            "model": model,
            "image_url": image_url
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))