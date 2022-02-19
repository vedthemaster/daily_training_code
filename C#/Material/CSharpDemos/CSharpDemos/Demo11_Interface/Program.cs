using System;

namespace Demo11_Interface
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("------- Demo of Overloaded Methods");
            Console.WriteLine();
            Demo01();
            Console.WriteLine();

            Console.WriteLine("------- Demo of Boxing and Unboxing");
            Console.WriteLine();
            Demo02();
            Console.WriteLine();

            Console.WriteLine("------- Demo of Interface");
            Console.WriteLine();
            Demo03();
            Console.WriteLine();
        }

        static void Demo01()
        {
            Car objCar = new Car();
            Scooter objScooter = new Scooter();
            Driver1 objDriver = new Driver1();

            objDriver.Drive(objCar);
            objDriver.Drive(objScooter);
        }


        static void Demo02()
        {
            Car objCar = new Car();
            Scooter objScooter = new Scooter();
            Driver2 objDriver = new Driver2();

            objDriver.Drive(objCar);                // boxing
            objDriver.Drive(objScooter);
        }

        static void Demo03()
        {
            Car objCar = new Car();
            Scooter objScooter = new Scooter();
            Driver1 objDriver = new Driver1();

            objDriver.Drive(objCar);                // interface object
            objDriver.Drive(objScooter);
        }

    }
}
