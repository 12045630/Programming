using System;

namespace Snake
{
    public class Colors
    {
        public Colors(int score) //Смена цвета в зависимости от очков
        {
            if (score <= 2)
            {
                Console.ForegroundColor = ConsoleColor.White;
            }
            else if (score >= 3 && score <= 5)
            {
                Console.ForegroundColor = ConsoleColor.DarkGreen;
            }
            else if (score >= 6 && score <= 8)
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
            }
            else if (score >= 9 && score <= 11)
            {
                Console.ForegroundColor = ConsoleColor.Red;
            }
        }
    }
}