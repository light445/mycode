using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using mycodelib;

namespace first
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("月黑风高杀人夜");
            Console.WriteLine("请按任意键继续");
            Console.ReadKey();

            Console.WriteLine("微风吹动这路边的小草");
            Console.WriteLine("请按任意键继续");
            Console.ReadKey();

            Console.WriteLine("隐约在路的尽头有一个人影");
            Console.WriteLine("请按任意键继续");
            Console.ReadKey();

            Console.WriteLine("走进一看这人叫");
            Console.WriteLine("请按任意键继续");
            Console.ReadKey();


            Console.WriteLine("请输入大侠的名字：");
            string name = Console.ReadLine();
            Console.WriteLine("原来你就是" + name);
            Console.WriteLine("请按任意键继续");
            Console.ReadKey();

            Hero daxia = new Hero();
            daxia.xingbie = "男";
            daxia.age = 25;
            daxia.shanghai = 10000;
            daxia.hp = 100;
            daxia.shenggao = 180;
            daxia.jineng1 = "战斗力强";
            daxia.jineng1shanghai = 200;
            daxia.jineng2 = "智力超群";
            daxia.jineng2shanghai = 150;
            //ShowInfo showInfo = new ShowInfo();
            ShowInfo.ShowHeroInfo(daxia);





            Console.WriteLine("此处传来了一个女人的声音");
            Console.WriteLine("请按任意键继续");
            Console.ReadKey();

            Console.WriteLine("请输入女侠的名字：");


            string name2 = Console.ReadLine();
            Console.WriteLine("原来你叫" + name2);
            Console.WriteLine("请按任意键继续");
            Console.ReadKey();

            Hero nvxia = new Hero();

            nvxia.xingbie = "女";
            nvxia.age = 20;
            nvxia.shanghai = 5000;
            nvxia.hp = 80;
            nvxia.shenggao = 160;
            nvxia.jineng1 = "魅力十足";
            nvxia.jineng1shanghai = 100;
            nvxia.jineng2 = "幽默感十足";
            nvxia.jineng2shanghai = 120;
            //将Hero类中创建的信息传递给ShowInfo类中的ShowHeroInfo方法
            
            ShowInfo.ShowHeroInfo(nvxia);






        }
    }
    
    
}
