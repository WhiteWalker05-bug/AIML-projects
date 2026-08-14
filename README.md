This read me file is created for the day 5 of the AIML course, in this file there will be a brief discription for a code written during the occurance of the lecture

this code focuses on the functioning of bank rituals of deposition, withdrawl, and showing balance for a specific customer

initially when we call the class BankAccount outside the class and create the object , the __init__ constructor runs. It takes the owner and balance as parameters and stores them using self.owner and self.balance

The deposit() method is used to add money to the account. The given amount is added to the current balance.

The withdraw() method is used to withdraw money from the account. Before withdrawing, it checks whether the requested amount is less than or equal to the available balance. If there is enough balance, the amount is deducted. Otherwise, it displays an "insufficient balance" message.

The show_balance() method displays the current balance of the account.

Example

A BankAccount object is created for Sakshi with an initial balance of 5000. Then, 1500 is deposited and 2000 is withdrawn.

The final balance is:

Balance 4500
