from main import Lexobot
from main import API_KEY, HOST, USERNAME

__version__ = "1.0.0"

lexobot = Lexobot(host=HOST, api_key=API_KEY, username=USERNAME)

if __name__ == "__main__":
    print(lexobot())
