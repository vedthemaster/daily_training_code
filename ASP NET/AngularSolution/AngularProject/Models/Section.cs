using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AngularProject.Models
{
    [Table("Sections")]
    public class Section
    {
        [Display(Name = "Section ID")]
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int SectionId { get; set; }

        [Display(Name = "Name of the Section")]
        [Required]
        [StringLength(50)]
        [Column("varchar")]
        public string SectionName { get; set; }
    }
}
