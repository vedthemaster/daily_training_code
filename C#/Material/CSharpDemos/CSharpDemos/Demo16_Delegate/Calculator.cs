using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo16_Delegate
{

    // 1. Define the Delegate
    delegate int ComputeHandler(int a, int b);


    class Calculator
    {

        // 2. Define the method to receive the Delegate pointer
        public int Compute(int a, int b, ComputeHandler objD)
        {
            int result = -1;

            Console.WriteLine("---- Five Steps of Encapsulation");
            Console.WriteLine("---- 1. Authentication");
            Console.WriteLine("---- 2. Authorization");
            Console.WriteLine("---- 3. Validation");

            // 3. Check if the Delegate is "subscribed" (check if pointer is provided)
            if (objD != null)
            {
                Console.WriteLine("---- 4. The Process / Activity");

                // 4. Invoke / Call the method pointed to by the Delegate
                result = objD(a, b);
            }


            Console.WriteLine("---- 5. Audit Logging");


            return result;
        }

        public int Add(int a, int b)
        {
            Console.WriteLine("---- Five Steps of Encapsulation");
            Console.WriteLine("---- 1. Authentication");
            Console.WriteLine("---- 2. Authorization");
            Console.WriteLine("---- 3. Validation");
            Console.WriteLine("---- 4. The Process / Activity");
            Console.WriteLine("---- 5. Audit Logging");

            return a + b;
        }

    }
}
