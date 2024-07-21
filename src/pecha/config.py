from starlette.config import Config

config = Config(".env")

PECHA_JWT_SECRET = config("PECHA_JWT_SECRET", default='fcc334b62d74e7ebde4c2a3c522cc72e40a85059eae453d372f6de69bd616f01')
PECHA_JWT_ALG = config("PECHA_JWT_ALG", default="HS256")
PECHA_JWT_EXP = config("PECHA_JWT_EXP", cast=int, default=86400)  # Seconds
PECHA_JWT_ISSUER = config("PECHA_JWT_ISSUER", default="https://pecha.org")
PECHA_JWT_AUD = config("PECHA_JWT_AUD", default="api.pecha.org")
