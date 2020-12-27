from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import constant
import json
@swagger.model
class expenseList(Resource):
    @swagger.operation(
        description="expense list",
        nickname="expense list",
        parameters=[
            {
                "name": "expense_name",
                "dataType": "String",
                "description": "expense details",
                "required": False,
                "allowMultiple": False,
                "paramType": "query"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "person expense details fetched successfully"},
            {"code": 400, "message": "Bad Request: Error on fetching expenses list"}
        ],
    )
    def get(self):
        try:
            expense_name = request.args.get(constant.EXPENSE_NAME)
            if expense_name:
                expenses=database.getParticularExpense(expense_name)
            else:
                expenses=database.getExpenses()
            return make_response(jsonify(
                {
                    "title": "Expense Details Fetched Successfully",
                    "status": HTTPStatus.OK,
                    "data": expenses,
                }
            ),
                HTTPStatus.OK
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from fetching expenses",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )