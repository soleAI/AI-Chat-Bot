
from app import app
from websocket import endpoints
import warnings
from app.routes import auth
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router,prefix='/api/v1')

warnings.filterwarnings('ignore')

if __name__=='__main__':
    app.run()
