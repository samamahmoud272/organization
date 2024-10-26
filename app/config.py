class Config:
    # MONGO_URI = "mongodb://localhost:27017/orgdb"  for locally run with command -- flask run
    MONGO_URI = "mongodb://mongo:27017/orgdb" # for docker running
    JWT_SECRET_KEY = "1c119451894c0a7b45bd2854182ba76fbd5d4cc418fee2421f4eb27a71266487"  
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Token expiration time  (1 hour)
    JWT_REFRESH_TOKEN_EXPIRES = 604800  # Refresh token expiration time (1 week)