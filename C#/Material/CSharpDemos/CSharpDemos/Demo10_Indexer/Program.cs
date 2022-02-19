using System;

namespace Demo10_Indexer
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Demo02();
        }

        static void Demo02()
        {
            Company objCompany = new Company("Microsoft");
            // objCompany.CompanyName = "Apple";
            objCompany.AddEmployee("Bill Gates");
            objCompany.AddEmployee("Steve Jobs");

            objCompany.DisplayEmployees();


            Employee empFirst = objCompany[1];
            if(empFirst != null)
            {
                Console.WriteLine("Employee ID: 1 was found!");
                Console.WriteLine("{0} {1}", empFirst.EmployeeID, empFirst.EmployeeName);
            }

            Employee emp = objCompany["Bill Gates"];
            if(emp != null)
            {
                Console.WriteLine("Employee with the Name 'Bill Gates' was found!");
                Console.WriteLine("{0} {1}", emp.EmployeeID, emp.EmployeeName);
            }

            emp = objCompany["Manoj"];
            if(emp == null)
            {
                Console.WriteLine("Employee with the name 'Manoj' was not found!");
            }
        }


        static void Demo01()
        {
            int[] arr = new int[3] { 10, 20, 30 };

            arr[1] = 200;           // index to the second element
        }
    }
}
