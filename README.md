# Python Based Chatbot Application

## Version :

`Python >= 3.8.1`

## Setup Steps

1. Clone the repository
2. create a virtual Environment by using this cmd `python3 -m venv env` or `python -m venv env` **for windows users**

3. Activate the virual environment by using cmd `source env/bin/activate` **(For mac and Linux)** or `env/Scripts/Activate.ps1` **(Form windows users)** .
4. Install packages using
   ``` pip3 install -r requirements.txt ```
5. Inside `keys` folder create a file named `key.py` and put the secret key there.
   ```py
       open_ai_key="your openai secret key"
   ```
6. Now run the application by using cmd : `uvicorn main:app --reload`
7. the backend will run on `8000` port now.