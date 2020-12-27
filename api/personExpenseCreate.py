from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json

@swagger.model
class expenseCreation(Resource):
    @swagger.operation(
        description="person expense creation",
        nickname="person expense creation",
        parameters=[
            {
                "name": "body",
                "dataType": "string",

                "required": True,
                "allowMultiple": False,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Person Expense Created succesfully"},
            {"code": 400, "message": "Bad Request: Error on creating expense"}
        ],
    )
    def post(self):
        try:
            payload = json.loads(request.data.decode())
            person_name=payload["person_name"]
            description=payload["description"]
            amount=payload["amount"]

            database.addExpense(person_name,description,amount)
            return make_response(jsonify(
                {
                    'title': "Expense Created Successfully",
                    "status": HTTPStatus.CREATED
                }
            ),
                HTTPStatus.CREATED,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from expense creation",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )