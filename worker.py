import time
import queue
import threading

# 1. Create an in-memory shared queue to hold tasks safely
task_queue = queue.Queue()

def process_worker():
    """This function runs indefinitely in the background, processing tasks from the queue."""
    print("[Worker] Engine started. Waiting for incoming background tasks...")
    while True:
        try:
            # Pull a task from the queue. blocks=True means wait until a task appears
            task = task_queue.get(block=True)
            
            task_id = task.get("id")
            task_type = task.get("type")
            user_id = task.get("user")
            
            print(f"\n[Worker] 🛠️  Processing Task {task_id} ({task_type}) for User {user_id}...")
            
            # Simulate a heavy machine learning or data processing operation
            time.sleep(3) 
            
            print(f"[Worker] ✅ Successfully completed Task {task_id}!")
            
            # Notify the queue that processing is done
            task_queue.task_done()
            
        except Exception as e:
            print(f"[Worker] ❌ Error processing task: {e}")

# 2. Spin up a dedicated background background thread for the worker
worker_thread = threading.Thread(target=process_worker, daemon=True)
worker_thread.start()

