using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment1
{
    class Details
    {
        private string name;
        private int age;


        public string Name
        {
            get { return name; }    
            set { name = value; }
        }public int Age
        {
            get { return age; }
            set {
                if (value < 18 || value > 65)
                {
                    Console.WriteLine("Age is Invalid");
                }
                else
                {
                    age = value;
                }
            }
        }

    }

}
