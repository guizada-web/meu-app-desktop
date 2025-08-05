from gui import AppGUI
from api_client import APIClient

def main():
    api_client = APIClient("https://api.thecatapi.com/v1")
    app = AppGUI(api_client)
    app.run()

if __name__ == "__main__":
    main()