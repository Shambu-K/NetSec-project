from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Print the HTTP request
    print(request.method, request.url, request.headers, request.get_data())

    # Return a response
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True, port=8700)
