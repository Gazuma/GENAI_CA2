# Savings Account Model

## Overview

This Python script simulates a banking system for savings accounts. It creates multiple bank accounts, performs random transactions on them, and manages balances. The script logs transaction details to a file and outputs a list of accounts sorted by their final balance.

## Features

- **Account Creation**: Generates 100 savings accounts with random initial balances between $100 and $10,000.
- **Transactions**: Simulates monthly transactions (deposits and withdrawals) for each account over 12 months.
- **Logging**: Records all transactions, including deposits, withdrawals, and any issues, to a log file (`logs.txt`).
- **Sorting**: Outputs a sorted list of accounts based on their final balance from lowest to highest.

## Files

- `savings_account_model.py`: The main Python script implementing the savings account model.
- `logs.txt`: Log file that records the details of all transactions performed during the simulation.

## Script Overview

1. **BankAccount Class**:
   - **Initialization**: Sets up an account with an ID and an initial balance.
   - **Deposit Method**: Adds funds to the account and logs the transaction.
   - **Withdraw Method**: Deducts funds from the account (if sufficient balance) and logs the transaction.
   - **String Representation**: Provides a readable format for the account's balance.

2. **Generate Transactions Function**:
   - Performs a random number of transactions (deposits and withdrawals) each month for a specified number of months.

3. **Main Function**:
   - Creates 100 bank accounts with random initial balances.
   - Simulates transactions for each account.
   - Sorts accounts by their final balance and prints the sorted list.

## Usage

1. **Run the Script**:
    ```bash
    python savings_account_model.py
    ```

2. **Output**:
    - **Terminal Output**: A sorted list of accounts with their final balances.
    - **Logs**: Details of each transaction, including successful deposits, withdrawals, and invalid transactions, are recorded in `logs.txt`.
