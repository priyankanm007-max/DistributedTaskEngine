from fastapi import FastAPI
import uuid

app = FastAPI()

@app.post("/submit-task")
def submit_task(task_type: str, user_id: int):
    # Generate a unique tracking ID for the background job
    task_id = str(uuid.uuid4())
    
    print(f"[API] Received task '{task_type}' from User {user_id}. Assigned ID: {task_id}")
    
    return {
        "status": "Queued",
        "task_id": task_id,
        "message": f"Task '{task_type}' has been successfully scheduled."
    }
from fastapi import FastAPI
import uuid
# Import our shared queue engine from worker.py
from worker import task_queue 

app = FastAPI()

@app.post("/submit-task")
def submit_task(task_type: str, user_id: int):
    task_id = str(uuid.uuid4())
    
    # Pack the incoming request parameters into a structured dictionary payload
    task_payload = {
        "id": task_id,
        "type": task_type,
        "user": user_id
    }
    
    # Push the payload straight into our concurrent worker queue
    task_queue.put(task_payload)
    print(f"[API] 📥 Task '{task_type}' queued successfully. ID: {task_id}")
    
    return {
        "status": "Queued Successfully",
        "task_id": task_id,
    }
