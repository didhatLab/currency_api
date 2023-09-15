import uvicorn

from src.build import build_app


def main():
    app = build_app()

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()



