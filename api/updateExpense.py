from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
# {
# "workorder_name":"company_name_2020-12-16 13:40:33.867911",
#  "company_name":"new_company_name",
#      "pump_details":{
# "pump type":"new xyz type",
# "power":"new 5mb",
# "cabel":"new cabel",
# "used_flag":"true",
# "rate":1000,
# "start_date":"12/16/2020",
# "end_date":"12/31/2021"
# },
#      "refered_by":"new refered_by",
#    "workorder_photo_url":"new workorder_photo_url"
# }
@swagger.model
class expenseUpdate(Resource):
    @swagger.operation(
        description="expense update",
        nickname="expense update",
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
            {"code": 200, "message": "Expense updated succesfully"},
            {"code": 400, "message": "Bad Request: Error on updating expense"}
        ],
    )
    def put(self):
        try:
            payload = json.loads(request.data.decode())
            expense_name=payload["expense_name"]
            person_name = payload["person_name"]
            description = payload["description"]
            amount = payload["amount"]

            database.updateExpense(expense_name,person_name,description,amount)
            return make_response(jsonify(
                {
                    'title': "Expense updated Successfully",
                    "status": HTTPStatus.OK
                }
            ),
                HTTPStatus.OK,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from expense updation",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )