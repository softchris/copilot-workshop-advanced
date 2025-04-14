using System.ComponentModel.DataAnnotations;

namespace ECommerceApi.Models
{
    public class Customer
    {
        public int Id { get; set; }
        
        [Required]
        [EmailAddress]
        [MaxLength(120)]
        public string Email { get; set; }
        
        [Required]
        [MaxLength(100)]
        public string Name { get; set; }
        
        [MaxLength(200)]
        public string Address { get; set; }
        
        [MaxLength(20)]
        public string Phone { get; set; }
        
        public ICollection<Order> Orders { get; set; }
    }
}