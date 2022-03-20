from fastapi import APIRouter, BackgroundTasks
import time

router = APIRouter()


def task_function(email: str, message=""):
    """Task function."""
    time.sleep(5)


@router.post("/task/{email}", status_code=202)
async def background_task(email: str, background_tasks: BackgroundTasks):
    """Background task."""
    background_tasks.add_task(task_function, email, message="some notification")
    return {"message": "Notification will be sent in the background"}
