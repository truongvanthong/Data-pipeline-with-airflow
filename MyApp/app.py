
import random
import flask
from flask import request, make_response, jsonify
from qdrant_client import QdrantClient

app = flask.Flask(__name__)


def search(query):
    # Đặt tên collection bạn đã tạo khi thực hiện pipeline vào biến bên dưới
    collection_name = '12345678'
    # thực hiện kết nối với cơ sở dữ liệu qdrant
    client = QdrantClient(host='qdrant_db', port=6333)
    collections = client.get_collections()
    collection_names = [
        collection.name for collection in collections.collections]
    embedding = [random.random() for i in range(1536)]

    if collection_name in collection_names:
        # thực hiện tìm kiếm với vector embedding bên trên
        results = client.search(
            collection_name=collection_name, query_vector=embedding, limit=1
        )
        if results:
            result_json = results[0].model_dump()
            return {
                "status": "success",
                "query": query,
                "result": result_json
            }
        else:
            return {
                "status": "error",
                "message": "No results found"
            }
    return {"message": "Collection not found"}


@app.route('/health', methods=['GET'])
def healthCheck():
    # điền mssv của bạn vào bên dưới
    return jsonify({
        "status": "success",
        "student_id": 12345678
    })

# Viết api có route "/search", phương thức POST để nhận vào câu query từ phía ngưới dùng
# sử dụng hàm search bên trên để tìm kiếm và trả về kết quả của hàm search cho người dùng

@app.route('/search', methods=['POST'])
def searchView():
    query = request.json['query']
    results = search(query)
    return make_response(results)

@app.route('/', methods=['GET'])
def home():
    return {"message": "ok"}


if __name__ == '__main__':
    # run app với port là "99xy" với xy là 2 số cuối cùng của mssv của bạn. Ví dụ: mssv: 17101691 thì port=9991
    app.run(host='0.0.0.0', port=5678) #9978

# curl -X POST http://localhost:8989/search -H "Content-Type: application/json" -d '{"query": "hội nghị cấp khoa"}'
