using Microsoft.EntityFrameworkCore;
using AngularProject.Models;

namespace AngularProject.Data
{
    public class ApplicationDbContext : DbContext
    {

        public DbSet<Section> Sections { get; set; }


        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }
    }
}
