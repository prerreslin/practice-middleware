from fastapi import BackgroundTasks
from main import UPLOAD_DIR
from time import sleep
from shutil import copyfileobj
from routes import task_status
import os

def generate_progress_updates(filename: str = ""):
    for progress in range(10):
        yield f"data: Processing {filename}: {progress * 10}% complete\n\n"
        sleep(1)
    yield f"data: Processing {filename}: 100% complete\n\n"

async def process_file_with_progress(filename: str, background_tasks: BackgroundTasks, task_id: str):
    file_location = os.path.join(UPLOAD_DIR, filename)
    processed_file_location = os.path.join(UPLOAD_DIR, f"{filename.split('.')[0]}_processed.{filename.split('.')[1]}")

    sleep(10)

    with open(file_location, "rb") as f_in, open(processed_file_location, "wb") as f_out:
        copyfileobj(f_in, f_out)

    task_status[task_id] = "Completed"


