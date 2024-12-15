from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class BudgetTracker(BoxLayout):
    budget = 0.0
    expenses = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Budget display
        self.budget_label = Label(text="Set Your Budget", font_size=20)
        self.add_widget(self.budget_label)

        # Input field for budget
        self.budget_input = TextInput(hint_text="Enter budget amount", multiline=False)
        self.add_widget(self.budget_input)

        # Set Budget Button
        self.set_budget_button = Button(text="Set Budget", on_press=self.set_budget)
        self.add_widget(self.set_budget_button)

        # Category input
        self.category_input = TextInput(hint_text="Expense category (e.g., Food)", multiline=False)
        self.add_widget(self.category_input)

        # Amount input
        self.amount_input = TextInput(hint_text="Expense amount", multiline=False)
        self.add_widget(self.amount_input)

        # Add Expense Button
        self.add_expense_button = Button(text="Add Expense", on_press=self.add_expense)
        self.add_widget(self.add_expense_button)

        # Expense list display
        self.expense_list_label = Label(text="No expenses added yet.", font_size=16)
        self.add_widget(self.expense_list_label)

    def set_budget(self, instance):
        try:
            self.budget = float(self.budget_input.text)
            self.budget_label.text = f"Budget: ${self.budget:.2f}"
            self.budget_input.text = ""  # Clear input field
        except ValueError:
            self.budget_label.text = "Invalid Budget Value"

    def add_expense(self, instance):
        try:
            category = self.category_input.text.strip()
            amount = float(self.amount_input.text)
            self.expenses.append({"category": category, "amount": amount})
            self.update_expense_list()
            self.category_input.text = ""  # Clear input field
            self.amount_input.text = ""  # Clear input field
        except ValueError:
            self.expense_list_label.text = "Invalid Expense Amount"

    def update_expense_list(self):
        total_spent = sum(exp["amount"] for exp in self.expenses)
        remaining_budget = self.budget - total_spent
        expenses_text = "\n".join([f"{exp['category']}: ${exp['amount']:.2f}" for exp in self.expenses])
        self.expense_list_label.text = f"Expenses:\n{expenses_text}\n\nTotal Spent: ${total_spent:.2f}\nRemaining Budget: ${remaining_budget:.2f}"


class BudgetApp(App):
    def build(self):
        return BudgetTracker()


if __name__ == "__main__":
    BudgetApp().run()
