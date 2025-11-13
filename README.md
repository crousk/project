# project

## Docker
- project\backend> docker build -t superapp .
- docker run superapp
- docker run -d superapp
## docker compose 
- docker compose up


- uv add "fastapi[all]"
-  uv add bcrypt==4.1.3 passlib==1.7.4
- uv run -m uvicorn app.main:app
- \backend\app> uv run -m uvicorn main:app  --reload --port 4569

## create new service
   1 uv init frontend
   2 cd .\frontend\
   3 uv add "fastapi[all]"
