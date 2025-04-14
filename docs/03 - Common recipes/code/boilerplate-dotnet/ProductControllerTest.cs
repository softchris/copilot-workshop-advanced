using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Moq;
using Xunit;
using ECommerceApi.Controllers;
using ECommerceApi.Data;
using ECommerceApi.Models;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Linq;

namespace ECommerceApi.Tests
{
    public class ProductsControllerTests
    {
        private readonly Mock<ECommerceContext> _mockContext;
        private readonly ProductsController _controller;
        private readonly Mock<DbSet<Product>> _mockSet;

        public ProductsControllerTests()
        {
            _mockContext = new Mock<ECommerceContext>();
            _mockSet = new Mock<DbSet<Product>>();
            _controller = new ProductsController(_mockContext.Object);
        }

        [Fact]
        public async Task GetProducts_ReturnsProductList_WhenProductsExist()
        {
            // Arrange
            var products = new List<Product>
            {
                new Product { Id = 1, Name = "Test Product 1", Price = 10.99m },
                new Product { Id = 2, Name = "Test Product 2", Price = 20.99m }
            }.AsQueryable();

            _mockSet.As<IQueryable<Product>>().Setup(m => m.Provider).Returns(products.Provider);
            _mockSet.As<IQueryable<Product>>().Setup(m => m.Expression).Returns(products.Expression);
            _mockSet.As<IQueryable<Product>>().Setup(m => m.ElementType).Returns(products.ElementType);
            _mockSet.As<IQueryable<Product>>().Setup(m => m.GetEnumerator()).Returns(products.GetEnumerator());

            _mockContext.Setup(c => c.Products).Returns(_mockSet.Object);

            // Act
            var result = await _controller.GetProducts();

            // Assert
            var actionResult = Assert.IsType<ActionResult<IEnumerable<Product>>>(result);
            var returnValue = Assert.IsAssignableFrom<IEnumerable<Product>>(actionResult.Value);
            Assert.Equal(2, returnValue.Count());
        }

        [Fact]
        public async Task GetProducts_ReturnsEmptyList_WhenNoProductsExist()
        {
            // Arrange
            var products = new List<Product>().AsQueryable();

            _mockSet.As<IQueryable<Product>>().Setup(m => m.Provider).Returns(products.Provider);
            _mockSet.As<IQueryable<Product>>().Setup(m => m.Expression).Returns(products.Expression);
            _mockSet.As<IQueryable<Product>>().Setup(m => m.ElementType).Returns(products.ElementType);
            _mockSet.As<IQueryable<Product>>().Setup(m => m.GetEnumerator()).Returns(products.GetEnumerator());

            _mockContext.Setup(c => c.Products).Returns(_mockSet.Object);

            // Act
            var result = await _controller.GetProducts();

            // Assert
            var actionResult = Assert.IsType<ActionResult<IEnumerable<Product>>>(result);
            var returnValue = Assert.IsAssignableFrom<IEnumerable<Product>>(actionResult.Value);
            Assert.Empty(returnValue);
        }
    }
}