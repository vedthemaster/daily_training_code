using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Collections.Generic;

namespace WebApplication1.Models
{
    [Table("Departments")]
    public class Department
    {
        [Display(Name ="Department ID")]
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int DepartmentId { get; set; }
        [Display(Name ="Department Name")]
        [Required(ErrorMessage ="{0} can not be empty")]
        [StringLength(50,ErrorMessage = "{0} cannot be more than {1} characters")]
        public string DepartmentName { get; set; }

        #region
        public ICollection<Subject> Subjects { get; set; }
        #endregion
    }
}
