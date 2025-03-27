using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 日常
{
    internal class Program
    {


        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("今天是2025.3.27");
            
            shuchu();

         
            

        }
        static void shuchu()
        {
            while (true) { 
            Console.WriteLine("请输入你的名字");
            string name = Console.ReadLine();
                if (name == "exit")
                {
                    break;
                }
                else { Console.WriteLine("hello" + name); }
            }
           
        }

    }


}