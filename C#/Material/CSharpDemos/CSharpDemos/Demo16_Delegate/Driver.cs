using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo16_Delegate
{
    // 1. Define DELEGATE
    //    Define the signature of the method to call, without defining the name of method
    delegate void DriveHandler();

    class Driver
    {

        public void DriveVehicle(DriveHandler objD)
        {
            Console.WriteLine("Driver is now driving some vehicle!");
            objD();
        }

    }
}
