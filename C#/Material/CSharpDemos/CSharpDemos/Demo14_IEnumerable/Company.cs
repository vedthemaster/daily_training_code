using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo14_IEnumerable
{
    class Company
        : System.Collections.IEnumerable
    {
        private System.Collections.ArrayList theEmployees;
        private int counter;

        public string CompanyName { get; private set; }
        
        public Company(string companyName)
        {
            CompanyName = companyName;
            theEmployees = null;
            counter = 0;
        }


        #region System.Collections.IEnumerable members

        public System.Collections.IEnumerator GetEnumerator()
        {
            if (theEmployees != null)
            {
                foreach (var emp in theEmployees)
                {
                    yield return emp;
                }
            }
            else
            {
                yield break;
            }
        }

        #endregion

        public void AddEmployee( string name )
        {
            Employee emp = new Employee();
            emp.EmployeeId = ++counter;
            emp.EmployeeName = name;

            if(theEmployees == null)
            {
                theEmployees = new System.Collections.ArrayList();
            }
            theEmployees.Add( emp );
        }

        public void DisplayEmployees()
        {
            Console.WriteLine("-- Employees of {0}", this.CompanyName);
            foreach( Employee emp in theEmployees)
            {
                Console.WriteLine("{0} {1}", emp.EmployeeId, emp.EmployeeName);
            }
        }
    }
}
