using Microsoft.EntityFrameworkCore;
using ReactProject.Models;

namespace ReactProject.Data
{
    public class ApplicationDbContext
        : DbContext
    {

        public DbSet<Section> Sections { get; set; }

        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }
    }
}