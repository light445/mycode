using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace lianxiGAME1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("请输入你的名字：");
            string name = (Console.ReadLine());
            Console.WriteLine("请输入你的年龄：");
            int age = int.Parse(Console.ReadLine());
            Console.WriteLine("你好" + name);
            if (age == 18)
            {
                Console.WriteLine("恭喜你成年了");

            }
            else if(age < 18)
            {
                Console.WriteLine("你还未成年");
            }
            else 
            {
                Console.WriteLine("你今年" + age + "岁了");
            }
            
            
            Console.ReadKey();
        }
    }
}