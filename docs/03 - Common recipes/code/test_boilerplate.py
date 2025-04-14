import pytest
from boilerplate import app, db, Product, Category
import json

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

@pytest.fixture
def sample_category(client):
    category = Category(name='Electronics', description='Electronic items')
    db.session.add(category)
    db.session.commit()
    return category

def test_get_empty_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert json.loads(response.data) == []

def test_get_products(client, sample_category):
    product = Product(
        name='Test Product',
        description='Test Description',
        price=99.99,
        stock=10,
        category_id=sample_category.id
    )
    db.session.add(product)
    db.session.commit()

    response = client.get('/products')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Test Product'
    assert data[0]['price'] == 99.99
    assert data[0]['stock'] == 10
    assert data[0]['category_id'] == sample_category.id

def test_create_product_success(client, sample_category):
    product_data = {
        'name': 'New Product',
        'description': 'New Description',
        'price': 199.99,
        'stock': 50,
        'category_id': sample_category.id
    }
    
    response = client.post('/products',
                          data=json.dumps(product_data),
                          content_type='application/json')
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data
    assert data['message'] == 'Product created successfully'

def test_create_product_missing_fields(client):
    product_data = {
        'name': 'New Product',
        'price': 199.99
    }
    
    response = client.post('/products',
                          data=json.dumps(product_data),
                          content_type='application/json')
    
    assert response.status_code == 500

def test_create_product_invalid_category(client):
    product_data = {
        'name': 'New Product',
        'description': 'New Description',
        'price': 199.99,
        'stock': 50,
        'category_id': 999  # Non-existent category
    }
    
    response = client.post('/products',
                          data=json.dumps(product_data),
                          content_type='application/json')
    
    assert response.status_code == 500