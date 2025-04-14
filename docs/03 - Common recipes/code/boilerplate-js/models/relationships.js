const Category = require('./category');
const Product = require('./product');
const Customer = require('./customer');
const Order = require('./order');
const Payment = require('./payment');

// Define relationships
Category.hasMany(Product);
Product.belongsTo(Category);

Customer.hasMany(Order);
Order.belongsTo(Customer);

Order.hasOne(Payment);
Payment.belongsTo(Order);

module.exports = {
  Category,
  Product,
  Customer,
  Order,
  Payment
};