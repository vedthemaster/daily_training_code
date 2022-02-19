using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo12_Interface_Extending.Demo02
{
    interface IDemo
    {
        void p();
    }

    interface IAnotherDemo
    {
        void p();
        void q();
    }

    class Demo : IDemo, IAnotherDemo
    {

        // implemented explicitly
        void IDemo.p()
        {

        }

        // implemented explicitly
        void IAnotherDemo.p()
        {

        }

        // implemented implicitly
        public void q()
        {

        }
    }

    class Run
    {
        public static void RunThis()
        {
            Demo obj = new Demo();
            obj.q();                    // implicitly implemented method
            (obj as IDemo).p();         // explicitly implemented method
            (obj as IAnotherDemo).p();  // explicitly implemented method


            IDemo objDemo = new Demo();
            (objDemo as Demo).q();
            objDemo.p();                // IDemo.p();   same as (obj as IDemo).p();
        }
    }
}
