using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace semana1_c_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer1();
            Console.ReadKey();

        }
        static void ejer1()
        {
            string nombre, carrera; //declarar variables

            Console.Write("ingrese su nombre");
            nombre = Console.ReadLine();

            Console.Write("ingrese su carrera");
            carrera = Console.ReadLine();

            Console.WriteLine($"\n{nombre}, bienvenido a FA de {carrera}");
        }




        static void ejer2()
        {
            Console.WriteLine("\"jesus\"");

        }









        static void ejer3()
        {
            Console.Write("ingrese numero x: ");
            int x = int.Parse(Console.ReadLine());

            Console.Write("ingrese numero y: ");
            int y = Convert.ToInt32(Console.ReadLine());

            double resu = (double)x / (double)y;

            Console.WriteLine("suma: " + (x + y));
            Console.WriteLine("resta: " + (x - y));
            Console.WriteLine("multiplicacion: " + (x * y));
            Console.WriteLine("divicion: " + resu);
        }










        static void ejer4()
        {
            Console.Write("Ingrese el numero decial: ");
            double num = Convert.ToDouble(Console.ReadLine());

            double raiz2 = Math.Sqrt(num);
            int redo = (int)Math.Round(num,0);
            double cubo = Math.Pow(num, 3);
            double raiz3 = Math.Pow(num, 1 / 3d);
            Console.WriteLine("Raiz 2: " + raiz2);
            Console.WriteLine("al cubo: " + cubo);
            Console.WriteLine("Raiz3: " + raiz3);
        }










        static void ejer5()
        {
            Console.Write("Ingrese numero:");
            string num = Console.ReadLine();

            int entero =int.Parse(num);
            double deci = double.Parse(num);

            Console.WriteLine("resto: " + (entero % 2));
            Console.WriteLine("division: " + (deci / 3));
        }









        static void ejer6()
        {

        }
    }
}
