from flask import Flask, request, jsonify

app = Flask(__name__)

def replace_placeholders(template, variables):
    for key, value in variables.items():
        placeholder = f"{{{{{key}}}}}"
        template = template.replace(placeholder, str(value))
    return template

@app.route('/replace', methods=['POST'])
def replace_text():
    data = request.json
    template = data.get('template', '')
    variables = data.get('variables', {})
        
    if not isinstance(variables, dict):
        return jsonify({"error": "Variables must be a dictionary"}), 400
        
    replaced_text = replace_placeholders(template, variables)
    return jsonify({"original": template, "result": replaced_text})

if __name__ == '__main__':
    app.run(debug=True)