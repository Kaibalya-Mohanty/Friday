import asyncio
import threading
from core.pipeline import Pipeline
from dashboard.app import start_dashboard

if __name__ == "__main__":
    print("🤖 Starting F.R.I.D.A.Y...")

    dashboard_thread = threading.Thread(target=start_dashboard, daemon=True)
    dashboard_thread.start()
    print("📊 Dashboard running at http://localhost:5000")

    pipeline = Pipeline()
    asyncio.run(pipeline.run())