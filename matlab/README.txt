Để chạy ví dụ, hãy làm theo các bước sau:

1. Thay đổi thư mục làm việc hiện tại của bạn thành Vehical_Counting / matlab / , nơi tập tin nguồn backgroundSubtractorOCV.cpp nằm ở đâu

2. Tạo tệp MEX từ tệp nguồn:
>> mexOpenCV backgroundSubtractorOCV.cpp

3. Chạy tập lệnh thử nghiệm:
>> testSample1.m
Tập lệnh thử nghiệm sử dụng lớp backgroundSubtractor, đến lượt nó, sử dụngđã tạo tệp MEX.

# Để chạy video, thay tệp 'Sample1.avi' trong file testSample1.m thành tên video cần (ưu tiên định dạng .avi) (Line 10).
# Trong trường hợp góc quay xa, sửa tỉ lệ định dạng (Line 50).
# Công cụ hỗ trợ: Matlab & Mex OpenCV.

## Dựa trên Copyright 2014 The MathWorks, Inc.
