from fastapi import FastAPI
from API.UploadApi import upload_route
from API.DownloadApi import download_route
from starlette.requests import Request
from uvicorn import run

app = FastAPI()

# assign routes
app.include_router(upload_route)
app.include_router(download_route)


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     print(request.headers["Id"], request.headers["Token"])
#     response = await call_next(request)
#     response.headers["X-Process-Time"] = 335
#     return response


@app.get("/", tags=["Main"])
def index():
    return {"amin": 34}


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=3005, debug=True)
