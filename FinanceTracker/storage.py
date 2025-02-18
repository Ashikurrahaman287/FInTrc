from datetime import datetime
from typing import Dict, List, Optional

class Transaction:
    def __init__(self, user_id: int, amount: float, category: str, 
                 description: str, transaction_type: str):
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.description = description
        self.type = transaction_type  # 'debt' or 'credit'
        self.timestamp = datetime.now()

class InMemoryStorage:
    def __init__(self):
        self.transactions: List[Transaction] = []
        self.user_data: Dict[int, dict] = {}

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def get_user_transactions(self, user_id: int) -> List[Transaction]:
        return [t for t in self.transactions if t.user_id == user_id]

    def get_today_transactions(self, user_id: int) -> List[Transaction]:
        today = datetime.now().date()
        return [t for t in self.get_user_transactions(user_id) 
                if t.timestamp.date() == today]

    def get_user_summary(self, user_id: int) -> Dict[str, float]:
        transactions = self.get_user_transactions(user_id)
        total_debt = sum(t.amount for t in transactions if t.type == 'debt')
        total_credit = sum(t.amount for t in transactions if t.type == 'credit')
        return {
            'total_debt': total_debt,
            'total_credit': total_credit,
            'net_balance': total_debt - total_credit
        }

    def get_category_summary(self, user_id: int) -> Dict[str, float]:
        transactions = self.get_user_transactions(user_id)
        categories = {}
        for t in transactions:
            if t.category not in categories:
                categories[t.category] = 0
            if t.type == 'credit':
                categories[t.category] += t.amount
            else:
                categories[t.category] -= t.amount
        return categories

# Global storage instance
storage = InMemoryStorage()
