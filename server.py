import numpy as np
from flask import Flask, request, render_template
import flask
import json
import utils
import os

# Khởi tạo model.
global model 
model = None
# Khởi tạo flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static"

# Khai báo các route 1 cho API
@app.route("/", methods=["GET"])
# Khai báo hàm xử lý dữ liệu.
def _hello_world():
#   return "Hello world"
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'placeholder.png')
    return render_template('index.html', displayedimage = full_filename)

# Khai báo các route 2 cho API
@app.route("/predict", methods=["POST"])
# Khai báo hàm xử lý dữ liệu.
def _predict():
  data = {"success": False}
  labels = ['setosa', 'versicolor', 'virginica']
  request_body = request.get_json(force=True)
  if (request.method=="POST") & (request_body is not None):
    # Lấy sepal_length
    sepal_length = request_body['sp_len']
    # Lấy sepal_width
    sepal_width = request_body['sp_wid']
    # Lấy petal_length
    petal_length = request_body['pen_len']
    # Lấy petal_width
    petal_width = request_body['pen_wid']
    # Convert sang numpy array input
    X_input = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    # Dự báo nhãn và xác suất.
    label = model.predict(X_input)
    # Dự báo phân phối xác suất
    dist_probs = model.predict_proba(X_input)
    # Truyền vào data form response
    data["probability"] = dist_probs[0][label]
    data["label"] = labels[label[0]]
    data["success"] = True
    return json.dumps(data, ensure_ascii=False, cls=utils.NumpyEncoder)

if __name__ == "__main__":
  print("App run!")
  # Load model và scaler
  model = utils._load_pkl('knn.pkl')
  scaler = utils._load_pkl('scaler.pkl')
  app.run(debug=False, host='localhost', threaded=False)