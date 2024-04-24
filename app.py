from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

app = Flask(__name__)

# Load the saved model and tokenizer
model_path = "my_best"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)


sent_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.json['message']
    result = sent_pipeline(message)[0]
    label = result['label']
    if label == 'LABEL_1':
        sentiment = 'Depressed'
    elif label == 'LABEL_0':
        sentiment = 'Not depressed'
    else:
        sentiment = 'unknown'
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
