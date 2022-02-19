using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo11_Interface
{
    // Demo of how Overloaded Version of the method can be used.
    class Driver1
    {

        public void Drive(Car objCar)
        {
            Console.WriteLine("--- Driver is now driving a Car!");
            objCar.DriveCar();
            Console.WriteLine();
        }

        public void Drive(Scooter objScooter)
        {
            Console.WriteLine("--- Driver is now driving a Scooter!");
            objScooter.Drive();
            Console.WriteLine();
        }
    }
}
