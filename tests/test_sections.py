def test_get_all_sections(client):
    response = client.get('/sections')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2  
def test_get_section(client):
    response = client.get('/sections/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['section_name'] == 'Electronics'

def test_get_nonexistent_section(client):
    response = client.get('/sections/999')
    assert response.status_code == 404

def test_create_section(client):
    response = client.post('/sections', json={'section_name': 'Books'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['section_name'] == 'Books'

def test_create_existing_section(client):
    response = client.post('/sections', json={'section_name': 'Electronics'})
    assert response.status_code == 400

def test_update_section(client):
    response = client.put('/sections/1', json={'section_name': 'Tech Gadgets'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['section_name'] == 'Tech Gadgets'

def test_update_nonexistent_section(client):
    response = client.put('/sections/999', json={'section_name': 'New Section'})
    assert response.status_code == 404

def test_delete_section(client):
    response = client.delete('/sections/1')
    assert response.status_code == 200

def test_delete_nonexistent_section(client):
    response = client.delete('/sections/999')
    assert response.status_code == 404
