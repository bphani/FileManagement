from fastapi import FastAPI
from API.UploadApi import upload_route
from uvicorn import run

app = FastAPI()


# assign routes
app.include_router(upload_route)

# @app.middleware("http")
# async def add_process_time_header(request: Request,call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response

@app.get("/", tags=["Main"])
def index():
    return {"amin": 34}


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=3005, debug=True)
