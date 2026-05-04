import azure.functions as func

from api.main import api

app = func.AsgiFunctionApp(
    app=api,
    http_auth_level=func.AuthLevel.ANONYMOUS
)