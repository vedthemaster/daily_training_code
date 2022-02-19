using System;

namespace Demo17_MultiCastDelegate
{
    internal class Program
    {

        delegate void ProcessHandler();

        static void Main(string[] args)
        {
            Demo1();
            Demo2();
        }

        static void Demo2()
        {
            Process proc = new Process();

            ProcessHandler objD1 = new ProcessHandler(proc.Step01);
            objD1 += new ProcessHandler(proc.Step02);
            objD1 += new ProcessHandler(proc.Step05);
            objD1 += new ProcessHandler(proc.Step03);
            objD1 += new ProcessHandler(proc.Step07);
            objD1 += new ProcessHandler(proc.Step09);
            Console.WriteLine();

            Console.WriteLine("Calling Process #1 using Multi-Cast delegate");
            objD1();            // invokes the delegate
            Console.WriteLine();

            Console.WriteLine("Calling Process #2 using Multi-Cast delegate");
            ProcessHandler objD2 = new ProcessHandler(proc.Step01);
            objD2 += new ProcessHandler(proc.Step06);
            objD2 += new ProcessHandler(proc.Step10);

            Program.Demo2ByDelegate(objD2);
            Console.WriteLine();

        }

        static void Demo2ByDelegate( ProcessHandler objD)
        {
            objD();
        }

        static void Demo1()
        {
            Console.WriteLine("--- Running Process #1");
            Process proc1 = new Process();
            proc1.Step01();
            proc1.Step02();
            proc1.Step05();
            proc1.Step03();
            proc1.Step07();
            proc1.Step09();
            Console.WriteLine();

            Console.WriteLine("---- Running Process #2");
            Process proc2 = new Process();
            proc2.Step01();
            proc2.Step06();
            proc2.Step10();
        }
    }
}
