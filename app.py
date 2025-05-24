from flask import Flask,render_template, request, jsonify
app = Flask(__name__)

@app.route('/hw')
def hello_world():
    return 'Hello World'

from api import GetResponse
@app.route('/',methods=['GET','POST']) 
def index():
    if request.method == 'POST':
        query = request.form['userInput']
        result = GetResponse(query)
        print("🤖 AI Response from main :\n", result)
        # GetResponse(query)
        # print(query)
        result = "🤖 AI Response :\n" + result
        return (render_template('index.html', result=result))
    return (render_template('index.html'))

# from weather import GetWeather
# @app.route('/weather',methods=['GET','POST']) 
# def index():
    if request.method == 'POST':
        query = request.form['userInput']
        weather = GetWeather(query)
        print("🤖 AI Response from main :\n", weather)
        # GetResponse(query)
        # print(query)
        result = "🤖 AI Response :\n" + weather
        return (render_template('index.html', weather=weather))
    return (render_template('index.html'))

if __name__ == '__main__':
    app.run(debug=True)
    app.run()


# import request

# API_KEY = "fyIzQ9Di8ywkmqeGUiFCjjj5ZPIskycr"
# url = "https://api.deepinfra.com/v1/inference/meta-llama/Meta-Llama-3-8B-Instruct"

# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# print("\n🤖 Welcome to DeepInfra AI Chat (LLaMA 3 - 8B)!")
# print("Type your message below. Type 'exit' to quit.\n")

# while True:
#     user_input = input("🧑 You: ")
#     if user_input.lower().strip() == "exit":
#         print("👋 Exiting chat. Goodbye!")
#         break

#     data = {
#         "input": user_input,
#         "parameters": {
#             "temperature": 0.7,
#             "max_new_tokens": 256
#         }
#     }

#     try:
#         response = requests.post(url, headers=headers, json=data)
#         if response.status_code == 200:
#             result = response.json()
#             if 'results' in result and result['results']:
#                 reply = result['results'][0].get('generated_text', '').strip()
#                 print(f"🤖 AI: {reply}\n")
#             else:
#                 print("🤖 AI: [No result returned]\n")
#         else:
#             print(f"❌ Error {response.status_code}: {response.text}\n")
#     except Exception as e:
#         print(f"⚠️ Exception occurred: {e}\n")
