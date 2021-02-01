using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cw01._02
{
    class Program
    {
        Random rnd;
        static void Main(string[] args)
        {
            Random rnd = new Random();
            int a = rnd.Next(1, 50);
            Console.WriteLine(a);
            string text = "";
            if (a >= 1 && a <= 10)
            { text = "odin"; }
            else if (a >= 11 && a <= 20)
            { text = "dva"; }
            else if (a >= 21 && a <= 30)
            { text = "tri"; }
            else if (a >= 31 && a <= 40)
            { text = "chetqre"; }
            else if (a >= 41 && a <= 50)
            { text = "pjat"; }
            Console.WriteLine(text);

            StreamWriter file = new StreamWriter(@"..\..\text.txt", true);
            file.WriteLine(text);
            file.Close();
            StreamReader filest = new StreamReader(@"..\..\text.txt");
            text = filest.ReadToEnd();
            Console.ForegroundColor = ConsoleColor.DarkBlue;
            Console.BackgroundColor =ConsoleColor.Yellow;
            //Console.Clear();
            Console.SetCursorPosition(5,5); 
            Console.WriteLine("Failis on text: \n {0}", text);

            int [] numbers=new int[5] {1,2,3,4,5 } ;
            foreach (var i in numbers)
            {
                Console.WriteLine(i);
            }
            for (int j = 0; j < numbers.Length; j++)
            {
                Console.WriteLine(numbers[j]);
            }

            Random r = new Random();
            int[] numbers2 = new int[6];
            for (int k = 0; k < numbers.Length; k++)
            {

                numbers2[k] = r.Next(1, 200);
            }
            foreach (var i in numbers2)
            {
                Console.WriteLine(i);
            }

            int[,] numbers3 = new int[4,10];
            for (int i = 0; i<numbers3.GetLength(0) ; i++)
            {
                for (int j = 0; j < numbers3.GetLength(1); j++)
                {
                    numbers3[i, j] = 1;
                    Console.Write(numbers3[i, j]);
                }
                Console.WriteLine();
            }
            Console.WriteLine();
            Console.ReadLine();

            ConsoleKeyInfo nupp = new ConsoleKeyInfo();
            do
            {
                Console.WriteLine("Vajuta Backspace...");
                nupp = Console.ReadKey();


            } while (nupp.Key != ConsoleKey.Backspace);

            Console.ReadLine();
        }
    }
}
