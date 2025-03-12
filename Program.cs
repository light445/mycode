using System;
using System.Runtime.DesignerServices;
using System.Xml.Linq;
//命名空间声明
namespace HellowWordCS
{
    //类定义：public class 类名{
    class Program
    {//只能有一个main方法
        static void Main()
        {
            GetInput();


        }
        //方法定义：static 方法类型  方法名(参数类型 参数名) -->无返回值类型
        //有返回值方法定义：
        //void为空值
        //static(私有)
        //public(公共)
        static void GetInput()
        {
            Console.WriteLine("请输入您的姓名：");
            string name = Console.ReadLine();
            Console.WriteLine("请输入您的年龄：");
            int age = int.Parse(Console.ReadLine());
            //try
            //{
            //    Console.WriteLine("请输入您的身高：");
            //    double height = double.Parse(Console.ReadLine());

            name = ChangeDate(name);
           




            Console.WriteLine("你的年龄是"+age);
        }
        //方法定义：static 方法类型  方法名(参数类型 参数名) -->返回值类型
        //方法调用：方法类型.方法名(参数)
        static string ChangeDate(string name1)
        {
            if (name1 == "张三")
            {
                Console.WriteLine("你好,法外狂徒张三");
            }
            else
            {
                Console.WriteLine("你好, " + name1);
            }

            return name1;
        }


    }

     class Hero
    {
        public int hp=100;
        public int atk;
        public int def;
        
        static void Get()
        {
            Console.WriteLine("hp");
        }

    }
}