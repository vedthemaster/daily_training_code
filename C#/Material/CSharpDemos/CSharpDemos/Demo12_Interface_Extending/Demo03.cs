using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo12_Interface_Extending.Demo03
{
    
    interface IDemo
    {
        void p();
    }

    interface IAnotherDemo : IDemo
    {
        void q();
    }

    // explicit implementation
    class Demo2 : IAnotherDemo
    {
        void IDemo.p() 
        {
        }

        void IAnotherDemo.q() 
        {
        }
    }


    // implicit implementations
    class Demo : IAnotherDemo
    {
        public void p()
        {

        }

        public void q()
        {

        }
    }
}
