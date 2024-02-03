#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uvicorn
import fastapi 

import pydantic
import logging


from src.routes import contacts, auth

app = fastapi.FastAPI()
   
#
# API methods
#

app.include_router(auth.router, prefix='/api')
app.include_router(contacts.router, prefix='/api')


@app.get("/")
async def root():
    return {"message": "--> super duper FastAPI sample contacts  <--"}
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    