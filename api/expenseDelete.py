from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
@swagger.model
class expenseDeletion(Resource):
    @swagger.operation(
        description="expense deletion",
        nickname="expense deletion",
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
            {"code": 200, "message": "Expense deleted succesfully"},
            {"code": 400, "message": "Bad Request: Error on deleting expense"}
        ],
    )
    def delete(self):
        try:
            payload = json.loads(request.data.decode())
            expense_name=payload["expense_name"]

            database.deleteExpense(expense_name)
            return make_response(jsonify(
                {
                    'title': "Workorder Deleted Successfully",
                    "status": HTTPStatus.OK
                }
            ),
                HTTPStatus.OK,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from workorder deletion",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )