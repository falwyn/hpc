import os
import pandas as pd # Khai báo thư viện hỗ trợ đọc và phân tích dữ liệu ở dạng bảng
import matplotlib.pyplot as plt # Khai báo thư viện để vẽ hình
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
from sklearn.metrics import r2_score
import pickle

# Giả sử file work_data.csv tồn tại
# Để mã này chạy được, chúng ta tạo một file giả lập
try:
    dataset = pd.read_csv("work_data.csv") # Lấy dữ liệu từ file work_data.csv
except FileNotFoundError:
    print("Không tìm thấy file work_data.csv. Tạo dữ liệu giả để chạy ví dụ.")
    data = {
        'SoNamKinhNghiem': [1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7, 3.9, 4.0, 4.0, 4.1, 4.5, 4.9, 5.1, 5.3, 5.9, 6.0, 6.8, 7.1, 7.9, 8.2, 8.7, 9.0, 9.5, 9.6, 10.3, 10.5],
        'Luong': [39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189, 63218, 55794, 56957, 57081, 61111, 67938, 66029, 83088, 81363, 93940, 91738, 98273, 101302, 113812, 109431, 105582, 116969, 112635, 122391, 121872],
        'NganhNghe': ['Sale', 'KeToan', 'HCNS', 'Sale', 'KeToan', 'HCNS', 'Sale', 'KeToan', 'HCNS', 'Sale', 'KeToan', 'HCNS', 'Sale', 'KeToan', 'HCNS', 'Sale', 'KeToan', 'HCNS', 'Sale', 'KeToan', 'HCNS', 'Sale', 'KeToan', 'HCNS', 'Sale', 'KeToan', 'HCNS', 'Sale', 'KeToan', 'HCNS']
    }
    dataset = pd.DataFrame(data)


df_keToan = dataset[dataset["NganhNghe"] == "KeToan"]
df_hcnh = dataset[dataset["NganhNghe"] == "HCNS"]
df_sale = dataset[dataset["NganhNghe"] == "Sale"]

def bieu_do_luong_kinhnghiem():
    dataset.plot(x='SoNamKinhNghiem', y='Luong', style='o')
    plt.title('Số năm kinh nghiệm - Lương')
    plt.xlabel('Số năm kinh nghiệm')
    plt.ylabel('Lương')
    plt.show()

def bieu_do_histogram():
    plt.hist(dataset['Luong'], 20)
    plt.title('Phân bố Histogram của Lương')
    plt.xlabel('Lương')
    plt.ylabel('Tần suất')
    plt.show()

def bieu_do_phan_bo_luongKT():
    plt.boxplot(df_keToan['Luong'])
    plt.title('Biểu đồ hộp phân bố lương nhân viên Kế toán')
    plt.ylabel('Lương')
    plt.xticks([1], ['Kế toán'])
    plt.show()

def show_bo_dl():
    print("Kết cấu bộ dữ liệu")
    print("Tổng số mẫu: " + str(dataset.shape[0]))
    print("Số lượng mẫu nhân viên Kế toán: " + str(df_keToan.shape[0]))
    print("Số lượng mẫu nhân viên HCNS: " + str(df_hcnh.shape[0]))
    print("Số lượng mẫu nhân viên SALE: " + str(df_sale.shape[0]))

def dudoan_():
    x = dataset["SoNamKinhNghiem"].values.reshape(-1,1)
    y = dataset['Luong'].values.reshape(-1,1)

    # Sửa rand_state thành random_state
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    print("\nMô hình hồi quy sẽ có dạng: Lương = a + b * SoNamKinhNghiem")
    print(f"Tham số a (intercept): {regressor.intercept_[0]}")
    print(f"Tham số b (coef): {regressor.coef_[0][0]}")

    # Đánh giá độ chính xác của mô hình
    y_pred = regressor.predict(x_test)

    r2_test = r2_score(y_test, y_pred)
    print("R2 trên tập kiểm tra (test) model là: " + str(r2_test))

    r2_train = r2_score(y_train, regressor.predict(x_train))
    print("R2 trên tập huấn luyện (train) model là: " + str(r2_train))

    model_filename = 'salary_model.pkl'
    with open(model_filename, 'wb') as file:
        pickle.dump(regressor, file)
    print(f"Da lua model da huan luyen vao file {model_filename}")

    plt.scatter(x_test, y_test, color='red', label='Dữ liệu thực tế')
    plt.plot(x_test, y_pred, color='blue', linewidth=2, label='Đường hồi quy dự đoán')
    plt.title('Lương vs. Kinh nghiệm (Trên tập Test)')
    plt.xlabel('Số năm kinh nghiệm')
    plt.ylabel('Lương')
    plt.legend()
    plt.show()

while True:
    print('''
**********************
1. Vẽ biểu đồ Số năm kinh nghiệm và lương
2. Vẽ biểu đồ histogram
3. Biểu đồ phân bố lương nhân viên kế toán
4. Show bộ dữ liệu
5. Dự đoán lương theo số năm kinh nghiệm
0. Thoát chương trình
**********************''')
    try:
        chon = int(input("Bạn hãy chọn một lựa chọn: "))
        if chon == 1:
            bieu_do_luong_kinhnghiem()
        elif chon == 2:
            bieu_do_histogram()
        elif chon == 3:
            bieu_do_phan_bo_luongKT()
        elif chon == 4:
            show_bo_dl()
        elif chon == 5:
            dudoan_()
        elif chon == 0:
            print("Đã thoát chương trình.")
            exit()
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
    except ValueError:
        print("Vui lòng nhập một số nguyên.")
