# LinearRegressionTechnicalAnalyService
hồi quy tuyến tính là phân tích kĩ thuật phổ biến trong thực tế. Chiến lược của hồi quy tuyến tính là với một tập các điểm trong quá khứ, chúng ta có thể vẽ được một đường thẳng sao cho tổng khoảng cách từ các điểm tới đường thẳng sẽ là nhỏ nhất. Và giá một đường thẳng sẽ y=ax + b sẽ được biểu diễn bằng hai thành phần: độ dốc a, và giá trị chặn b

## Tính toán hồi quy tuyến tính
Phương pháp tính đường thẳng hồi quy tuyến tính từ một tập điểm như sau
Tính giá trị trung bình x, y

Độ lệch của tập điểm với giá trị trung bình

Tính giá trị độ dốc 

Tính giá trị chặn

## Hồi quy tuyến tính đa chiều


## Chiến lược giao dịch bằng hồi quy tuyến tính
Linear regression forcast

Linear regression intercept

Nguy cơ trong chiến lược

## Các bước thực hiện
### Collect data
Nhiệm vụ của việc collect data là thu thập các thông tin trong rawdata trong những khung thời gian khác nhau. trong đó có các khung thời gian từ 1, 5, 10, 20 phút

### Collect data set
Mục tiêu thu thâp data set giá trị linear regresstion của tập dataset trên mỗi khung thời gian 5 và 10

### ListCandidatePoint
Liệt kê danh sách các candidate là các điểm mà tại đó giá trị linear thay đổi so với điểm phía trước. Tại mỗi thời điểm giá trị hồi quy được xác định bởi hai yếu tố, slope và intercept. Nếu giá trị slop = 0 tức tại thời điểm đó, hướng đi của giá bắt đầu chuyển 
