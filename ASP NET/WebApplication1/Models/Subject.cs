using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace WebApplication1.Models
{
    [Table("Subjects")]
    public class Subject
    {
        [Display(Name ="Subject ID")]
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int SubjectId { get; set; }

        [Display(Name ="Name of the Subject")]
        [Required]
        public string SubjectName { get; set; }

        #region

        [Display(Name ="Department Name")]
        [Required]
        [ForeignKey(nameof(Subject.Department))]
        public int DepartmentId { get; set; }
        public Department Department { get; set; }
        #endregion


    }
}
