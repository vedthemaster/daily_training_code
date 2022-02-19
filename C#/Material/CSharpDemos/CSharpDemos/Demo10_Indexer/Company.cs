using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


/// <summary>
///     Demo of 
///     (1) Aggregation (one object inside another Eg: ArrayList of Employee is inside Company)
///     (2) Dynamically resizable collection (ArrayList) Vs. Array
///     (3) Auto-Implemented property
///     (4) Late-Instantiation Pattern (create an aggregated object only when required)
///     (5) instance constructor to automatically seed the ID of the Employee.
/// </summary>


namespace Demo10_Indexer
{
    class Company
    {

        //private string _companyName;                // backing data field
        //public string CompanyName                   // property
        //{
        //    get {  return _companyName; }
        //    private set { _companyName = value; }
        //}

        // Auto-Implemented Property
        // C# language compiler will generate the backing data field, and the property's GET & SET accessor
        public string CompanyName { get; private set; }

        private System.Collections.ArrayList theEmployees { get; set; }

        private int counter;


        public Company( string name )
        {
            this.theEmployees = null;                // 1. collection is initialized to NULL
            this.counter = 0;
            CompanyName = name;
        }


        // Indexer
        public Employee this[string name]
        {
            get
            {
                Employee empFound = null;

                foreach(Employee emp in theEmployees)
                {
                    if( emp.EmployeeName == name)
                    {
                        empFound = emp;
                        break;
                    }
                }

                return empFound;
            }
        }
        
        // Indexer
        public Employee this[int id]
        {
            get
            {
                Employee empFound = null;

                foreach(Employee emp in theEmployees)
                {
                    if(emp.EmployeeID == id)
                    {
                        empFound = emp;
                        break;
                    }
                }

                return empFound;
            }
        }

        

        public void AddEmployee(string nameOfNewEmployee)
        {
            Employee emp = new Employee();
            emp.EmployeeID = ++this.counter;
            emp.EmployeeName = nameOfNewEmployee;

            // 2. check collection is still NULL
            if(theEmployees == null)
            {
                // 3. instantiate the collection
                theEmployees = new System.Collections.ArrayList();
            }

            // 4. add the newly created employee object to the collection.
            theEmployees.Add(emp);
        }


        public void DisplayEmployees()
        {
            foreach( Employee emp in theEmployees)
            {
                Console.WriteLine("{0} {1}", emp.EmployeeID, emp.EmployeeName);
            }
        }
    }
}
