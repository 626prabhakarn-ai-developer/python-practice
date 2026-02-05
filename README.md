# python-practice

Small exercises repository.

This repo contains a simple Python script `add_two_numbers.py` that reads two numbers from stdin and prints their sum.

## Files
- `add_two_numbers.py` — CLI program that prompts for two numbers and prints their sum.
- `requirements.txt` — lists virtualenv-installed packages (none required for this script).

## Usage
1. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies (none required, but run if you add packages):

```bash
python3 -m pip install -r requirements.txt
```

3. Run the script:

```bash
python3 add_two_numbers.py
```

Enter two numbers when prompted. Example:

```
Enter first number: 3
Enter second number: 4
Sum: 7
```

## Notes
- No external packages are required for this example.
- `venv/` is included in `.gitignore` to avoid committing the virtual environment.

## Author
Prabhakaran
