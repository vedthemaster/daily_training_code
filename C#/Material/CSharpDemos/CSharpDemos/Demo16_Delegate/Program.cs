using System;

namespace Demo16_Delegate
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Calculator objCal = new Calculator();

            int result;
            result = objCal.Add(10, 20);
            Console.WriteLine("Sum of {0} and {1} = {2}", 10, 20, result);
            Console.WriteLine();

            Console.WriteLine("--- direct call to the method");
            result = Program.Multiply(100, 200);
            Console.WriteLine("Result = {0}", result);
            Console.WriteLine();

            Console.WriteLine("--- calling the method through the delegate!");
            result = objCal.Compute(100, 200, Program.Multiply);
            Console.WriteLine("Result = {0}", result);
            Console.WriteLine();
        }

        private static int Multiply(int a, int b)
        {
            return a * b;
        }

        static void Demo01()
        {
            Car objCar = new Car();
            Scooter objScooter = new Scooter();
            Driver objDriver = new Driver();

            objDriver.DriveVehicle(objCar.DriveCar);

            objDriver.DriveVehicle(objScooter.DriveScooter);
        }
    }
}
