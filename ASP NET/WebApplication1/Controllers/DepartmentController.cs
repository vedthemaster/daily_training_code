using Microsoft.AspNetCore.Mvc;
using WebApplication1.Data;
using System.Linq;

namespace WebApplication1.Controllers
{
    public class DepartmentController : Controller
    {
        private  ApplicationDbContext _context;
        public DepartmentController(ApplicationDbContext context)
        {
            _context = context;
        }
    
        public IActionResult Index()
        {
            //
            // var query = from dept in _context.Departments
            //       select dept;

            // return View(query);
            var depts = _context.Departments.ToList();
            return View(depts);
        }
    }
}
