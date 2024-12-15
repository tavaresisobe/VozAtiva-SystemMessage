from starlette.responses import JSONResponse


def generate(data=None, message=None, status_code=200, notice=None, token=None):
    """HTTP response pattern design function

    | default status code is 200

    | default notice arg  is an empty array"""

    if data is None:
        data = {}
    if message is None:
        message = []
    if notice is None:
        notice = []

    return JSONResponse({
        "message": message,
        "notice": notice,
        "data": data,
        "token": token
    }, status_code=status_code)
