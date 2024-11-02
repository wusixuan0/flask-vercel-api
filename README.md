### Get Started
```
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
export FLASK_APP=api.index
flask run
``` 
### To Deploy
Install Vercel CLI:
```
npm i -g vercel
```
Test locally:
```
vercel dev
```
API should be available at http://localhost:3000/api/

Deploy to Vercel:
```
vercel
```