from machineLearning import clean
from machineLearning import models
from flask import Flask
from flask import render_template, request
app = Flask("Sentiment Analyzer")


@app.route('/')
def hello():
    return render_template("index.html",data=[],length = 0)


@app.route('/sentiments', methods=['POST'])
def sentiments():
    data = [clean.cleanText(request.form['sentimentText'])]
    sentiments_result = []
    for text in data:
        sentiment = models.getSentiment(text)
        sentiments_result.append("Negative" if sentiment == 0 else "Positive")
        print([request.form['sentimentText'],sentiments_result[0]])
    return render_template('index.html', data= [[request.form['sentimentText'],sentiments_result[0]]],length = len(data))


@app.route('/sentiments_file', methods=['POST'])
def sentiments_file():
    file_Data = request.files['sentimentFile']
    data = file_Data.read().decode('ascii')
    data = clean.cleanSentence(data)
    sentiments_result = []
    for text in data:
        sentiment = models.getSentiment(text)
        sentiments_result.append("Negative" if sentiment == 0 else "Positive")
    results = []
    print(file_Data.read().decode('ascii'))
    for i,d in enumerate(file_Data.read().decode('ascii')):
        results.append([d,sentiments_result[i]])
    print(results)
    return render_template('index.html',data = results,length = len(data))

if __name__ == "__main__":
    app.run(debug=False)
    
