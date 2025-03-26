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
            Console.WriteLine("今天是2025.3.26");
           
            for (int i = 0 ; ; i++)
            {
                Console.WriteLine("请输入你的名字");
                string name=Console.ReadLine();
                if(name=="李白")
                Console.WriteLine("你好，李太白");
                else
                {
                    Console.WriteLine("你好，"+name);
                } 
                
            }

         
            

        }
       
        
    }
}