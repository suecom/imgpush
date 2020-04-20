import os

IMAGES_DIR = "/images/"
CACHE_DIR = "/cache/"
OUTPUT_TYPE = None
MAX_UPLOADS_PER_DAY = 100000
MAX_UPLOADS_PER_HOUR = 1000
MAX_UPLOADS_PER_MINUTE = 200
ALLOWED_ORIGINS = ["*"]
NAME_STRATEGY = "randomstr"
MAX_TMP_FILE_AGE = 5 * 60

VALID_SIZES = []

MAX_SIZE_MB = 20

for variable in [item for item in globals() if not item.startswith("__")]:
    NULL = "NULL"
    env_var = os.getenv(variable, NULL).strip()
    if env_var is not NULL:
        try:
            env_var = eval(env_var)
        except Exception:
            pass
    globals()[variable] = env_var if env_var is not NULL else globals()[variable]
