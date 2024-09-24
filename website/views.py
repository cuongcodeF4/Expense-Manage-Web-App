from flask import Blueprint, render_template, request
import os
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    chart_url = None  # Khởi tạo biến cho biểu đồ
    if request.method == 'POST':
        file = request.files['file']
        chart_type = request.form['chart_type']
        
        # Đường dẫn thư mục tải lên
        upload_folder = 'uploads'
        
        # Tạo thư mục nếu nó không tồn tại
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        # Đường dẫn đầy đủ để lưu file
        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)

        # Đọc file CSV và tạo biểu đồ
        df = pd.read_csv(filepath)  # Đọc file CSV
        chart_url = create_chart(df, chart_type)  # Tạo biểu đồ
        
    return render_template('index.html', chart=chart_url)

def create_chart(df, chart_type):
    img = io.BytesIO()
    if chart_type == 'line':
        df.plot(kind='line')
    elif chart_type == 'bar':
        df.plot(kind='bar')
    else:
        return None  # Trả về None nếu loại biểu đồ không hợp lệ

    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url
