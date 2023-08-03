import sys, os
from unittest import mock
from urllib import response

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','..'))
sys.path.append(os.path.join(ROOT_DIR, 'client','controller'))
sys.path.append(os.path.join(ROOT_DIR, 'server','model'))
sys.path.append(os.path.join(ROOT_DIR, 'server'))
TEST_SERVER_DIR = os.path.join(ROOT_DIR, 'tests', 'unit','test.db')

from flask import current_app
from Balance import Balance
from DBModel import DBModel
from Expense import Expense
from flaskdb import db
from connector import Connector

import unittest
from unittest.mock import MagicMock, patch,Mock
from requests.models import Response
import pytest
from controller import create_app

from unittest.mock import patch

def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            
        def json(self):
            return self.json_data
        
    if args[0] == 'http://127.0.0.1:5000/income':
        yield MockResponse({'text':'OK'}, 200)
    elif args[0] == 'http://127.0.0.1:5000/expense':
        yield MockResponse({'text':'OK'}, 200)
    else:
        yield MockResponse({'text':'Bad Request'}, 400)
class TestClass(unittest.TestCase):

    def setUp(self):
        self.connector = Connector("http://127.0.0.1:5000")
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + TEST_SERVER_DIR
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        self.connector = None
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None
        pass

    def test_app(self):
        print("============================")
        print("Testing App Initialization")
        assert self.app is not None
        assert current_app == self.app
        print("Test Success ✅")

    def test_income12(self):
        print("============================")
        print("Testing income post request URL")
        response = self.client.post('/income',json={'amount':100}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("Test Success ✅")

    def test_Expense12(self):
        print("============================")
        print("Testing expense post request URL")
        response = self.client.post('/expense',json={'amount':0}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("Test Success ✅")

    def test_balance123(self):
        print("============================")
        print("Testing balance post request URL")
        response = self.client.get('/balance', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("Test Success ✅")
        
    def test_income(self):
        print("============================")
        print("Testing save income")
        pre_balance = float((self.client.get('/balance', follow_redirects=True)).text)
        amount = 100
        local_balance = float(pre_balance)+ float(amount)
        res1 = self.client.post('/income',json={'amount':amount}, follow_redirects=True)
        self.assertEqual(res1.status_code, 200)
        res2 = self.client.get('/balance', follow_redirects=True)
        self.assertEqual(res2.status_code, 200)
        memory_balance = float(res2.text)
        self.assertEqual(local_balance, memory_balance)
        print("Test Success ✅") 

    def test_balance(self):
        print("============================")
        print("Testing balance query")
        pre_balance = float((self.client.get('/balance', follow_redirects=True)).text)
        amount = 100
        local_balance = float(pre_balance)+ float(amount)
        res1 = self.client.post('/income',json={'amount':amount}, follow_redirects=True)
        self.assertEqual(res1.status_code, 200)
        res2 = self.client.get('/balance', follow_redirects=True)
        self.assertEqual(res2.status_code, 200)
        memory_balance = float(res2.text)
        self.assertEqual(local_balance, memory_balance)
        print("Test Success ✅")

    def test_expense(self):
        print("============================")
        print("Testing save expense")
        pre_balance = float((self.client.get('/balance', follow_redirects=True)).text)
        amount = 100
        local_balance = float(pre_balance)- float(amount)
        res1 = self.client.post('/expense',json={'amount':amount}, follow_redirects=True)
        self.assertEqual(res1.status_code, 200)
        res2 = self.client.get('/balance', follow_redirects=True)
        self.assertEqual(res2.status_code, 200)
        memory_balance = float(res2.text)
        self.assertEqual(local_balance, memory_balance)
        print("Test Success ✅")

    def test_income_multiple(self):
        print("============================")
        print("Testing saving multiple incomes")
        pre_balance = float((self.client.get('/balance', follow_redirects=True)).text)
        amounts = [100, 130, 230, 10, 430, 31032, 123, 2.23, 2.3]
        amount=0
        for amt in amounts:
            res1 = self.client.post('/income',json={'amount':amt}, follow_redirects=True)
            self.assertEqual(res1.status_code, 200)
            amount+=amt
            
        local_balance = float(pre_balance)+ float(amount)
        
        res2 = self.client.get('/balance', follow_redirects=True)
        self.assertEqual(res2.status_code, 200)
        memory_balance = float(res2.text)
        self.assertEqual(local_balance, memory_balance)
        print("Test Success ✅")
        res1 = self.client.post('/dropdata', follow_redirects=True)

    def test_expense_multiple(self):
        print("============================")
        print("Testing saving multiple expense")
        pre_balance = float((self.client.get('/balance', follow_redirects=True)).text)
        amounts = [100, 130, 230, 10, 430, 31032, 123, 2.23, 2.3]
        amount=0
        for amt in amounts:
            res1 = self.client.post('/expense',json={'amount':amt}, follow_redirects=True)
            self.assertEqual(res1.status_code, 200)
            amount+=amt
            
        local_balance = float(pre_balance)-float(amount)
        
        res2 = self.client.get('/balance', follow_redirects=True)
        self.assertEqual(res2.status_code, 200)
        memory_balance = float(res2.text)
        self.assertEqual(local_balance, memory_balance)
        print("Test Success ✅")

    @pytest.fixture(scope="session")
    def flask_app():
            app = create_app()
            client = app.test_client()
            ctx = app.test_request_context()
            ctx.push()
            yield client
            ctx.pop()

    @pytest.fixture(scope="session")
    def app_with_db(flask_app):
            db.create_all()

            yield flask_app

            db.session.commit()
            db.drop_all()
        
if __name__ == '__main__':
    unittest.main()
    
