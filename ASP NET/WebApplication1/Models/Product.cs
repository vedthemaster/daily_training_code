using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace WebApplication1.Models
{
    [Table("Products")]
    public class Product
    {
        [Display(Name ="Product ID")]
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int ProductId { get; set; }

        [Display(Name ="Product Name")]
        [Required(ErrorMessage ="{0} can not be Empty")]
        [StringLength(50,ErrorMessage ="{0} can not be more than {1}")]
        public string ProductName { get; set; }

        [Required(ErrorMessage ="{0} this can not be empty")]
        [Range(minimum:1,maximum:100, ErrorMessage ="{0} needs to be between {1} and {2}")]
        public int Quantity { get; set; }

        [Required(ErrorMessage ="{0} this can not be empty")]
        [Range(minimum:1,maximum:1000, ErrorMessage ="{0} needs to be between {1} and {2}")]
        public int Price { get; set; }

    }
}
