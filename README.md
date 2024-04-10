# Build Data Pipeline With Airflow, MongoDB, QdrantDB, and App Search

0. Vào docker-compose.yml và comment các thông số sau:
```
  # myapp:
  #   build: ../MyApp
  #   ports:
  #     - "9955:9955"
  #   networks:
  #     - qdrant-network
  #   depends_on:
  #     - qdrant_db
  #     - mongodb
```
0. Mở Docker Desktop
1. Vào airflow:
```bash
cd airflow
```
2. Build Data Pipeline:
```bash
docker compose up --build
```
3. Truy cập vào Airflow UI: TK-MK: airflow-airflow
> http://localhost:8080/
4. Truy cập vào QdrantDB UI:
> http://localhost:6333/dashboard
5. Mở MongoDB Compass và kết nối đến MongoDB:
> url: mongodb://localhost:27017
+ Mở Advanced và chọn Authentication: 
    + Username: admin
    + Password: admin
    + Authentication Database: admin
6. Thêm fit và json vào thư mục dags:
+ copy nó vào
+ New terminal (PS):
```bash
docker ps
```
+ Lấy id của scheduler airflow
```bash
docker exec -it 3id bash
```
```bash
airflow scheduler
```
## Build App Search
1. Mở lại docker-compose.yml và bỏ comment các thông số sau:
```
  myapp:
    build: ../MyApp
    ports:
      - "9955:9955"
    networks:
      - qdrant-network
    depends_on:
      - qdrant_db
      - mongodb
```
2. Build App Search: nhớ cd vô airflow
```bash
docker compose up myapp --build
```
3. Truy cập vào App Search UI:
> http://localhost:9955/
4. Vào file test_Thong.ipynb test:
```python

import requests
url = "http://localhost:9955"
response = requests.post(f"{url}/search", json = {"query": "Hội nghị cấp khoa?"})
response.json()

output:
{'id': '88a6b327-5265-417f-90bb-51557709d181',
 'payload': {'content': 'Chiều ngày 15/01/2021 tại phòng LAB của Khoa CNTT ĐH Công Nghiệp TP HCM đã tổ chức buổi giới thiệu môn học ERP do TVHpro Edu xây dựng và mô phỏng trên hệ thống Hoạch định nguồn lực doanh nghiệp\xa0SS4U.ERP Express 2021\xa0của SS4U Express. Đây là lần thứ 3 chúng tôi trình bày môn học ERP với IUH. Lần 1 với Khoa QTKD năm 2013, lần 2 với Khoa CNTT vào năm 2018.\n\nGiảng viên Khoa CNTT tham khảo tài liệu sản phẩm ERP của SS4U\nÔng Thẩm Văn Hương- Sáng lập, Chủ tịch HĐQT các công ty đã giới thiệu kinh nghiệm đào tạo ERP ở các trường đại học, chương trình đào tạo và demo phần mềm SS4U.ERP Express,\xa0SS4U.BI\n\nKịch bản mô phỏng ERP phiên bản 2021\nCác bên đã trao đổi nhiều nội dung liên quan và thống nhất sẽ đưa hệ thống SS4U.ERP Express cùng với chương trình đào tạo cho ngành hệ thống thông tin quản lý ngay trong năm học tới.\n\nHệ thống SS4U.ERP Express 2021 được xây dựng trên công nghệ Oracle\n\nÔng Thẩm Văn Hương giới thiệu chi tiết kịch bản đào tạo cho Khoa CNTT\nNhư vậy, SS4U cùng với TVHpro Edu đã hoàn thành xuất sắc kế hoạch phát triển hoạt động đào tạo trong năm 2020 với các trường ĐH quy mô lớn nhất TP HCM như: ĐH Kinh tế TP HCM, ĐH Bách Khoa TP HCM (Khoa Quản lý công nghiệp), ĐH Sư Phạm Kỹ Thuật TP HCM, ĐH Văn Lang TP HCM, ĐH Tài Chính Marketing TP HCM, ĐH Hoa Sen TP HCM, ĐH Hutech, ĐH Kinh Tế Tài Chính TP HCM…và ĐH Công Nghiệp TP HCM.\nTrong buổi làm việc, kỹ thuật Công ty cung cấp giải pháp Cloud Server\xa0EXA\xa0đã chia sẻ giải pháp Server phù hợp cho hoạt động đào tạo.\n\nNăm 2021, TVHpro Edu & SS4U sẽ chia sẻ môn học ERP cho các Trường ĐH ở Phú Yên, Đà Nẵng và ĐBSCL.\nSS4U đang lên kế hoạch xây dựng giải pháp lập báo cáo tài chính theo chuẩn mực kế toán quốc tế IFRS trong năm 2021 để đáp ứng yêu cầu quản trị của doanh nghiệp và phù hợp với xu hướng hội nhập quốc tế của Việt Nam.\nNguồn. SS4U\nLink online\n',
  'date': '2021-01-25T00:00:00',
  'href': 'news.html@detail@102@2689@SS4U-&-TVHpro-EDU-HOP-TAC-DAO-TAO-ERP-VOI-KHOA-CNTT-DH-CONG-NGHIEP-TP-HCM',
  'title': 'SS4U & TVHpro EDU HỢP TÁC ĐÀO TẠO ERP VỚI KHOA CNTT ĐH CÔNG NGHIỆP TP HCM'},
 'score': 0.051544394,
 'shard_key': None,
 'vector': None,
 'version': 471}

```

