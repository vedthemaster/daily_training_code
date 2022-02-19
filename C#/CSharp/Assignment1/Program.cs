using System;

namespace Assignment1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Details obj = new Details();
            Console.WriteLine("Welcome");
            Console.Write("Enter Your Name: ");
            obj.Name = Console.ReadLine();

            Console.Write("Enter Your age: ");
            obj.Age = int.Parse(Console.ReadLine());

            Console.WriteLine("Hello {0},Your age is {1}",obj.Name,obj.Age);
        }
    }
}
