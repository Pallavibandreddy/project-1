from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

with open('LogisticRegression_model.pkl','rb') as f:
     model = pickle. load(f)

@app.route('/', methods=['GET', 'POST'])
def clickhere():
    if request.method == 'POST':
        try:
            title = float(request.form['title'])
            text = float(request.form['text'])
        
            prediction = model.predict([[title, text]])

            return render_template('navigation.html', prediction=prediction)
        except KeyError:
            
            error_message = "Please enter a message."
            return render_template('navigation.html', error=error_message)
    return render_template('navigaton.html')



if __name__ == '__main__':
    app.run(debug=True)