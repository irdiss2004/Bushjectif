from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.dashboard import router as dashboard_router
from routes.goals import router as goals_router
from routes.stats import router as stats_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(goals_router)
app.include_router(stats_router)
