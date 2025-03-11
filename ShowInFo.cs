using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using mycodelib;

namespace first
{
    class ShowInfo//代码抽离封装成库
    {
        public static void ShowHeroInfo(Hero hero)//这里的第二个hero就是类中的对象
        {

            Console.WriteLine("姓名:" + hero.xingbie);
            Console.WriteLine("年龄:" + hero.age);
            Console.WriteLine("伤害:" + hero.shanghai);
            Console.WriteLine("血量" + hero.hp);
            Console.WriteLine("身高:" + hero.shenggao);
            Console.WriteLine("技能1:" + hero.jineng1);
            Console.WriteLine("技能1伤害:" + hero.jineng1shanghai);
            Console.WriteLine("技能2:" + hero.jineng2);
            Console.WriteLine("技能2伤害:" + hero.jineng2shanghai);
        }

    }
}
