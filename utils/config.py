from utils.functions import *
from dotenv import load_dotenv

load_dotenv()

routes = {
    "Dev": "",
    "Stage": ""
    }


if "ENVIRONMENT" in os.environ:
    environment = os.getenv('ENVIRONMENT')
else:
    environment = get_config("behave", "environment")

base_url = routes[environment]
driver_default = get_config("driver", "default")
