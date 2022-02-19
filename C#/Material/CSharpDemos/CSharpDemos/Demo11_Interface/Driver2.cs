using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo11_Interface
{
    class Driver2
    {
        public void Drive(object objVehicle)
        {
            Console.WriteLine("--- Driver is now driving a vehicle!");
            if (objVehicle is Car)                                  // 1. type-checking
            {
                Car car = objVehicle as Car;                        // 2. unbox 
                car.DriveCar();
            }
            else if (objVehicle is Scooter)
            {
                Scooter objScooter = objVehicle as Scooter;         // unboxing
                objScooter.Drive();
            }
            Console.WriteLine();
        }


    }
}
