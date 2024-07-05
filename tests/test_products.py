def test_get_all_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 4  

def test_get_product(client):
    response = client.get('/products/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['product_name'] == 'Laptop'

def test_get_nonexistent_product(client):
    response = client.get('/products/999')
    assert response.status_code == 404

def test_create_product(client):
    response = client.post('/products', json={
        'section_id': 1,
        'product_name': 'Tablet',
        'quantity_in_stock': 30,
        'price_per_unit': 300,
        'is_product_available': True,
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['product_name'] == 'Tablet'

def test_create_product_with_invalid_section(client):
    response = client.post('/products', json={
        'section_id': 999,
        'product_name': 'Invalid Product',
        'quantity_in_stock': 30,
        'price_per_unit': 300,
        'is_product_available': True,
    })
    assert response.status_code == 400

def test_create_existing_product(client):
    response = client.post('/products', json={
        'section_id': 1,
        'product_name': 'Laptop',
        'quantity_in_stock': 30,
        'price_per_unit': 300,
        'is_product_available': True,
    })
    assert response.status_code == 400

def test_update_product(client):
    response = client.put('/products/1', json={
        'section_id': 1,
        'product_name': 'Updated Laptop',
        'quantity_in_stock': 45,
        'price_per_unit': 900,
        'is_product_available': True,
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['product_name'] == 'Updated Laptop'

def test_update_nonexistent_product(client):
    response = client.put('/products/999', json={
        'section_id': 1,
        'product_name': 'Nonexistent Product',
        'quantity_in_stock': 45,
        'price_per_unit': 900,
        'is_product_available': True,
    })
    assert response.status_code == 404

def test_delete_product(client):
    response = client.delete('/products/1')
    assert response.status_code == 200

def test_delete_nonexistent_product(client):
    response = client.delete('/products/999')
    assert response.status_code == 404
