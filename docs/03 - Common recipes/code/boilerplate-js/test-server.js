// Mock the models
jest.mock('./models/relationships');
jest.mock('./models');

describe('Server', () => {
  let app;

  beforeEach(() => {
    // Clear all mocks before each test
    jest.clearAllMocks();
    
    // Reset the express app
    app = express();
    app.use(express.json());
    
    // Import fresh instance of routes
    require('./server');
  });

  describe('GET /products', () => {
    it('should return all products', async () => {
      const mockProducts = [
        { id: 1, name: 'Product 1' },
        { id: 2, name: 'Product 2' }
      ];
      
      Product.findAll.mockResolvedValue(mockProducts);

      const response = await request(app)
        .get('/products');

      expect(response.status).toBe(200);
      expect(response.body).toEqual(mockProducts);
      expect(Product.findAll).toHaveBeenCalled();
    });

    it('should handle errors', async () => {
      Product.findAll.mockRejectedValue(new Error('Database error'));

      const response = await request(app)
        .get('/products');

      expect(response.status).toBe(500);
      expect(response.body).toHaveProperty('error');
    });
  });

  describe('POST /products', () => {
    it('should create a new product', async () => {
        const newProduct = { name: 'New Product' };
        const createdProduct = { id: 1, ...newProduct };
    
        Product.create.mockResolvedValue(createdProduct);
    
        const response = await request(app)
            .post('/products')
            .send(newProduct);
    
        expect(response.status).toBe(201);
        expect(response.body).toEqual(createdProduct);
        expect(Product.create).toHaveBeenCalledWith(newProduct);
        });

    it('should handle validation errors', async () => {
        const invalidProduct = { name: '' }; // Assuming name is required
    
        const response = await request(app)
            .post('/products')
            .send(invalidProduct);
    
        expect(response.status).toBe(400);
        expect(response.body).toHaveProperty('error', 'Validation error');
    })

    it('should handle database errors', async () => {
        const newProduct = { name: 'New Product' };
    
        Product.create.mockRejectedValue(new Error('Database error'));
    
        const response = await request(app)
            .post('/products')
            .send(newProduct);
    
        expect(response.status).toBe(500);
        expect(response.body).toHaveProperty('error', 'Database error');
    })
})
});
