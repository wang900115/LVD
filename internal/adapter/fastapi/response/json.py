from typing import Any
from fastapi.responses import JSONResponse
# from message import Message

class JsonResponse:
    def success(self, message: str) -> JSONResponse:
        return self._response(200,message)
    
    def successWithData(self, message: str, data: Any) -> JSONResponse:
        return self._response(201,message,data=data)
    
    def fail(self, message: str) -> JSONResponse:
        return self._response(500,message)
    
    def failWithError(self, message: str, err: Exception) -> JSONResponse:
        return self._response(501,message,err=err)
    
    def authFail(self, message: str) -> JSONResponse:
        return self._response(401,message)
    
    def authFailWithError(self, message: str, err: Exception) -> JSONResponse:
        return self._response(401,message,err=err)
    
    def _response(self, status_code:int, message: str, data: Any = None, err: Exception = None) -> JSONResponse:
        content = {"message": message}
        if err:
            content["err"] = err
        if data:
            content["data"] = data
        return JSONResponse(content=content, status_code=status_code)