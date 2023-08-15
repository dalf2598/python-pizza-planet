from flask import jsonify

class BaseService:
    
    def __init__(self, controller):
        self.controller = controller
    
    def __handle_response(self, response, error):
        response = response if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    
    def create(self, request):
        response, error = self.controller.create(request.json)
        return self.__handle_response(response, error)

    def update(self, request):
        response, error = self.controller.update(request.json)
        return self.__handle_response(response, error)

    def get_by_id(self, _id: int):
        response, error = self.controller.get_by_id(_id)
        return self.__handle_response(response, error)

    def get_all(self):
        response, error = self.controller.get_all()
        return self.__handle_response(response, error)