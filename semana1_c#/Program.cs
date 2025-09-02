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
            Console.Write("ingrese numero x: ");
            int x = int.Parse( Console.ReadLine() );

            Console.Write("ingrese numero y: ");
            int y = Convert.ToInt32( Console.ReadLine() );

            double resu = x / y;

            Console.WriteLine("suma: " + (x + y));
            Console.WriteLine("resta: " + (x - y));
            Console.WriteLine("multiplicacion: " + (x * y));
            Console.WriteLine("divicion: " + resu);

        }









        static void ejer3()
        {

        }










        static void ejer4()
        {

        }










        static void ejer5()
        {

        }









        static void ejer6()
        {

        }
    }
}
