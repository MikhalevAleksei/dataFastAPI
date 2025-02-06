from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"),
          name="static")

# Путь к шаблонам
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root_html(request: Request):
    """Возвращает HTML-страницу с формой"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/calculate", response_class=HTMLResponse)
async def calculate(request: Request, num1: str = Form(...),
                    num2: str = Form(...)):
    """Обрабатывает данные и возвращает HTML с результатом"""
    try:
        num1, num2 = int(num1), int(num2)
        if not (0 <= num1 < 111 and 0 <= num2 < 111):
            return templates.TemplateResponse("result.html",
                                              {"request": request,
                                               "error": "Числа должны быть от 0 до 110"},
                                              status_code=400)

        result = num1 + num2
        return templates.TemplateResponse("result.html",
                                          {"request": request, "num1": num1,
                                           "num2": num2, "result": result,
                                           "operation": "+"})

    except ValueError:
        return templates.TemplateResponse("result.html",
                                          {"request": request,
                                           "error": "Некорректные данные, введите числа"},
                                          status_code=400)


@app.post("/subtract", response_class=HTMLResponse)
async def subtract(request: Request, num1: str = Form(...),
                   num2: str = Form(...)):
    """Обрабатывает вычитание и возвращает HTML с результатом"""
    try:
        num1, num2 = int(num1), int(num2)
        if not (0 <= num1 < 111 and 0 <= num2 < 111):
            return templates.TemplateResponse("result.html",
                                              {"request": request,
                                               "error": "Числа должны быть от 0 до 110"},
                                              status_code=400)

        result = num1 - num2
        return templates.TemplateResponse("result.html",
                                          {"request": request, "num1": num1,
                                           "num2": num2, "result": result,
                                           "operation": "-"})

    except ValueError:
        return templates.TemplateResponse("result.html",
                                          {"request": request,
                                           "error": "Некорректные данные, введите числа"},
                                          status_code=400)
