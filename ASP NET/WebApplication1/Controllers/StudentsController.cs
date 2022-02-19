using Microsoft.AspNetCore.Mvc;

namespace WebApplication1.Controllers
{
    public class StudentsController : Controller
    {
        public IActionResult Index()
        {
            return Ok("Hello World from Server");
        }
    }
}
