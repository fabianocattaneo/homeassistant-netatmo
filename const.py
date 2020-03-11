"""Constants used by the Netatmo component."""
from datetime import timedelta

API = "api"

DOMAIN = "netatmo"
MANUFACTURER = "Netatmo"

AUTH = "netatmo_auth"
CONF_PUBLIC = "public_sensor_config"
CAMERA_DATA = "netatmo_camera"
HOME_DATA = "netatmo_home_data"

CONF_CLOUDHOOK_URL = "cloudhook_url"

OAUTH2_AUTHORIZE = "https://api.netatmo.com/oauth2/authorize"
OAUTH2_TOKEN = "https://api.netatmo.com/oauth2/token"

DATA_PERSONS = "netatmo_persons"

NETATMO_WEBHOOK_URL = None
NETATMO_EVENT = "netatmo_event"

DEFAULT_PERSON = "Unknown"
DEFAULT_DISCOVERY = True
DEFAULT_WEBHOOKS = False

ATTR_ID = "id"
ATTR_PSEUDO = "pseudo"
ATTR_NAME = "name"
ATTR_EVENT_TYPE = "event_type"
ATTR_HOME_ID = "home_id"
ATTR_HOME_NAME = "home_name"
ATTR_PERSONS = "persons"
ATTR_IS_KNOWN = "is_known"
ATTR_FACE_URL = "face_url"
ATTR_SCHEDULE_ID = "schedule_id"
ATTR_SCHEDULE_NAME = "schedule_name"

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=5)
MIN_TIME_BETWEEN_EVENT_UPDATES = timedelta(seconds=5)

SERVICE_SETSCHEDULE = "set_schedule"
