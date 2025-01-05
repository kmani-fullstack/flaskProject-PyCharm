from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items":[
            {
                "name": "Chair",
                "price": 15.90,
            }
        ]
    }
]

@app.route('/')
def hello_world():
    return 'Hello World!'

# Return all stores
@app.get('/store')
def get_stores():
    return {'stores':stores}


@app.post('/store')
def add_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": [],
    }
    stores.append(new_store)
    #stores[0]['items'].append(new_store)
    return new_store, 201

@app.post('/store/<string:store_name>/item')
def add_store_item(store_name):
    for store in stores:
        if store["name"] == store_name:
            request_data = request.get_json()
            item = {
                "name": request_data["name"],
                "price": request_data["price"],
            }
            store['items'].append(item)
            return item, 201

    return {'message':"Store not found"}, 404


# Return a store and items
@app.get('/store/<string:store_name>')
def get_store(store_name):
    for store in stores:
        if store['name'] == store_name:
            return store
    return {"message": "Store not found"}, 404

# Return store items based on store name
@app.get('/store/<string:store_name>/item')
def get_store_items(store_name):
    for store in stores:
        if store['name'] == store_name:
            return {"items":store['items']}
    return {"message": "Store not found"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')
