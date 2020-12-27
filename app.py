import os
from config import app
from api import api
from api.personExpenseCreate import expenseCreation
from api.expenseDelete import expenseDeletion
from api.expenseList import expenseList
from api.updateExpense import expenseUpdate

api.add_resource(expenseCreation,"/api/expenseCreate")
api.add_resource(expenseDeletion,"/api/expenseDelete")
api.add_resource(expenseList,"/api/get_all_expense")
api.add_resource(expenseUpdate,"/api/update_expense")

if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5004, debug=True)