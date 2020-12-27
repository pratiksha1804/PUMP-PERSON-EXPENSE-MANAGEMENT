from config import app
from config import mongo
import datetime

def addExpense(person_name,description,amount):
    date=datetime.datetime.now()
    expense_name=person_name + "_" + str(date)
    expense_info={
    "expense_name":expense_name,
    "person_name":person_name,
    "description":description,
    "amount":amount,
    "date":date
    }
    return mongo.db.PERSON_EXPENSE_INVENTORY.insert_one(expense_info)

def deleteExpense(expense_name):
    expense_info={
        "expense_name":expense_name
    }
    return mongo.db.PERSON_EXPENSE_INVENTORY.delete_one(expense_info)

def getExpenses():
    expenses = mongo.db.PERSON_EXPENSE_INVENTORY.find({},{'_id': False})
    expense_list = []
    if expenses:
        for exp in expenses:
            expense_list.append(exp)
        return expense_list
    return None

def getParticularExpense(expense_name):
    expense = mongo.db.PERSON_EXPENSE_INVENTORY.find_one({"expense_name":expense_name}, {'_id': False})
    if expense:
        return expense
    return None

def updateExpense(expense_name,person_name,description,amount):
        my_query = {"expense_name": expense_name}
        new_values = {"$set": {"person_name":person_name,"description":description,"amount":amount}}
        return mongo.db.PERSON_EXPENSE_INVENTORY.update(my_query, new_values)