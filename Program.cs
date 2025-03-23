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
            Console.WriteLine("今天是2025.3.15");
            Hero xiaoli = new Hero();
            
            xiaoli.name = "李探花";
            xiaoli.hp = 100;
            xiaoli.attack = 100;
            xiaoli.defence = 100;
            xiaoli.speed = 100;
            xiaoli.XingWi();


        }
        /* static void ChangeName()
         {
             Console.WriteLine("请输入你的名字：");
             string name = Console.ReadLine();
             if (name == "小李")
             {
                 Console.WriteLine("你好李探花");
             }
             else
             {
                 Console.WriteLine("你好，" + name);
             }
         }
     }*/
        class Hero
        {
            public string name;
            public int hp;
            public int attack;
            public int defence;
            public int speed;
            public void XingWi()
            {
                Console.WriteLine("技能1：小李飞刀");
                Console.WriteLine("技能2：星位移");
                Console.WriteLine("技能3：星位斩");
                Console.WriteLine("技能4：星位爆");
                Console.WriteLine("你的名字：" + name);
                Console.WriteLine("你的速度：" + speed);
                Console.WriteLine("你的防御力：" + defence);
                Console.WriteLine("你的血量：" + hp);
                Console.WriteLine("你的攻击力：" + attack);

                
            }
        }
    }
}