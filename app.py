from flask import Flask 
import generate_random_password

app = Flask(__name__)

@app.route('/api/helloworld', methods=['GET'])
def api_helloworld():
    return generate_random_password.generate_random_password(8)


if __name__ == '__main__':
    app.run(debug=True)
    

# Starten mit ```flask --app run --debug````
