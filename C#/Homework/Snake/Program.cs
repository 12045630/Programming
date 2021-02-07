using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Snake
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.SetWindowSize(80, 25);

            Walls walls = new Walls(80, 25);
            walls.Draw();
            
            Point p = new Point(4, 5, '*');
            Snake snake = new Snake(p, 4, Direction.RIGHT);
            snake.Draw();

            FoodCreator foodCreator = new FoodCreator(79, 24, '$');
            Point food = foodCreator.CreateFood();
            food.Draw();
            int score = 0;

            while (true)
            {
                if (walls.IsHit(snake) || snake.IsHitTail())
                {
                    break;
                }
                if (snake.Eat(food))
                {
                    food = foodCreator.CreateFood();
                    food.Draw();
                    score++;
                    Colors col = new Colors(score);
                }
                else
                {
                    snake.Move();
                    Thread.Sleep(100);
                }
                
                if (Console.KeyAvailable)
                {
                    ConsoleKeyInfo key = Console.ReadKey();
                    snake.HandleKey(key.Key);
                    
                }
                //Console.ReadLine();
            }

            TotalScore(score);
        }
        
        static void WriteInt(string text1,int text, int xOffset, int yOffset)
        {
            Console.SetCursorPosition(xOffset, yOffset);
            Console.Write(text1);
            Console.WriteLine(text);
        }

        static void TotalScore(int score)
        {
            int xOffset = 25;
            int yOffset = 8;
            Console.ForegroundColor=ConsoleColor.Blue;
            Console.SetCursorPosition( xOffset, yOffset++ );
            WriteInt(" Всего ",score,xOffset,yOffset++);
        }
        
        
    }
}