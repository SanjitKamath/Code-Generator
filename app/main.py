import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


import logging
from dotenv import load_dotenv
import traceback
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from generator import CodeGenerator

from fastapi.responses import JSONResponse

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Log to file
    file_handler = logging.FileHandler("app.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Log to console
    import sys
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

# Load .env variables
load_dotenv()

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "..", "templates"))

try:
    logger.info("Initializing CodeGenerator...")
    generator = CodeGenerator()
    logger.info("CodeGenerator initialized successfully.")
except Exception as e:
    logger.error("CodeGenerator initialization failed:")
    logger.error(traceback.format_exc())

    class ErrorGenerator:
        def generate_code(self, prompt):
            return f"System Error: Initialization failed - {str(e)}"

    generator = ErrorGenerator()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "system_ready": isinstance(generator, CodeGenerator)
    })

@app.post("/generate")
async def generate_code(request: Request, prompt: str = Form(...)):
    if not isinstance(generator, CodeGenerator):
        return templates.TemplateResponse("index.html", {
            "request": request,
            "prompt": prompt,
            "error": "System initialization failed. Please check server logs.",
            "success": False,
            "system_ready": False
        })

    try:
        generated_code = generator.generate_code(prompt)

        if generated_code.startswith("Error generating code:"):
            return templates.TemplateResponse("index.html", {
                "request": request,
                "prompt": prompt,
                "error": generated_code,
                "success": False,
                "system_ready": True
            })

        return templates.TemplateResponse("index.html", {
            "request": request,
            "prompt": prompt,
            "generated_code": generated_code,
            "success": True,
            "system_ready": True
        })

    except Exception as e:
        logger.error("Error during code generation:")
        logger.error(traceback.format_exc())
        return templates.TemplateResponse("index.html", {
            "request": request,
            "prompt": prompt,
            "error": f"Unexpected error: {type(e).__name__}: {str(e)}",
            "success": False,
            "system_ready": True
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload = False)
