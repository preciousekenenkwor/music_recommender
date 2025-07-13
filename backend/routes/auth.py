from fastapi import APIRouter

router = APIRouter()

@router.post("/signin")
def signin(email: str, password: str):
    if email == "user@example.com" and password == "test123":
        return {"token": "fake-jwt-token"}
    return {"error": "Invalid credentials"}
