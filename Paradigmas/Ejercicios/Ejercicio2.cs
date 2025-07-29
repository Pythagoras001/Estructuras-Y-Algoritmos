using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio1
{   
    // Creamos la clase Jugador
    internal class Jugador
    {
        public string? nombre { get; set; }
        public int nivel { get; set; }
        public List<string> points { get; set; } = new List<string>();

        public Jugador(string nombre, int nivel) 
        {
            this.nombre = nombre;
            this.nivel = nivel;
        }
    }

    // Creamos la clase Main
    internal class Programa
    {

        // Creamos las varibles globales
        static List<Jugador> jugadores = new List<Jugador>();
        static List<(Jugador jugador1, Jugador jugador2, int resultado, string veredicto)> partidas = new();
        static Dictionary<Jugador, int> clasificacion = new Dictionary<Jugador, int> ();

        static void Main(string[] args)
        {
            // Creamos las varibles
            string nombre;
            int nivel;

            string jugadorNameSelect;
            Jugador jugador1;
            Jugador jugador2;
            
            int opcion;

            string entrada;

            // Creamos el menu de seleccion 
            while (true)
            {


                // Solicitamos selccionar una opcion
                while (true)
                {
                    try
                    {
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        Console.Write("Ingrese Una Opcion\n0| Crear Jugador\n1|Jugar Partida\n2|Ver Jugadores\n3| Ver Historico\n4| Salir\nSelcione => ");

                        entrada = Console.ReadLine() ?? "";

                        if (!int.TryParse(entrada, out opcion) || opcion < 0 || opcion > 4) throw new Exception("Entrada Invalida Intente de Nuevo");

                        break;
                    }
                    catch (Exception e)
                    {
                        Console.BackgroundColor = ConsoleColor.Red;
                        Console.ForegroundColor = ConsoleColor.Black;
                        Console.WriteLine(e.Message);
                        Console.ResetColor();

                        continue;
                    }
                }

                switch (opcion)
                {
                    // Agregar jugador
                    case 0:
                        Console.ForegroundColor = ConsoleColor.Magenta;
                        Console.Write("Ingrese el nombre => ");
                        Console.ResetColor();
                        nombre = Console.ReadLine()!;

                        Console.ForegroundColor = ConsoleColor.Magenta;
                        Console.Write("Ingrese el nivel => ");
                        Console.ResetColor();
                        nivel = int.Parse(Console.ReadLine()!);

                        AgregarJugador(new Jugador(nombre, nivel));
                        break;

                    // Jugar Partida
                    case 1:
                        Console.ForegroundColor = ConsoleColor.Magenta;
                        Console.Write("ingrese el primer jugador => ");
                        jugadorNameSelect  = Console.ReadLine()!;
                        Console.ResetColor();

                        jugador1 = BuscarJugador(jugadorNameSelect);

                        Console.ForegroundColor = ConsoleColor.Magenta;
                        Console.Write("ingrese el segundo jugador => ");
                        Console.ResetColor();
                        jugadorNameSelect = Console.ReadLine()!;

                        jugador2 = BuscarJugador(jugadorNameSelect);

                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.Write(JugarPartida(jugador1, jugador2));
                     
                        break;

                    // Ver Jugadores
                    case 2:
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine(VerJugadores());
                        break;

                    // Ver Historico de partidas
                    case 3:
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.Write(VerHistorialPartidas());
                        break;

                    // Salir
                    case 4:
                        Environment.Exit(0);
                        break;

                }

                Console.WriteLine();

            }
        }

        // Metodo Agragar jugador
        static void AgregarJugador(Jugador objJugador) => jugadores.Add(objJugador);

        // Metodo Buscar Jugador
        static Jugador BuscarJugador(string nombreJugador) => jugadores.Find(p => p.nombre == nombreJugador) ?? throw new Exception("Jugador No Encontrado");

        static string VerHistorialPartidas() => string.Join("\n", partidas.Select((p, i) => $"PARTIDA #{i+1}\nJugador 1: {p.jugador1.nombre}\nJugador 2: {p.jugador2.nombre}\nResultado: {p.resultado}\nVeredicto: {p.veredicto}\n"));

        static string VerJugadores() => string.Join("\n", jugadores.Select((p, i) => $"\nJUGADOR #{i+1}\nNombre: {p.nombre}\nNivel: {p.nivel}\nPartidas{string.Join(" ", p.points)}\nPuntos Totales: {(clasificacion.ContainsKey(p) ? clasificacion[p] : 0)}"));

        // Metodo Jugar una partida
        static string JugarPartida(Jugador jugador1, Jugador jugador2)
        {
            Random rand = new Random();
            int resultado = rand.Next(-1, 2);
            string resultadoString;

            // Agragamos el resultado del juego al historial de partidas de los jugadores
            if (resultado == 0)
            {
                resultadoString = "Empate";
                jugador1.points.Add("Empate");
                jugador2.points.Add("Empate");
                AgregarPuntos(jugador1, jugador2, true);
            }
            else if (resultado == 0)
            {
                resultadoString = "Jugador 1 Gana";
                jugador1.points.Add("Gana");
                jugador2.points.Add("Pierde");
                AgregarPuntos(jugador1, jugador2, false);
            }
            else
            {
                resultadoString = "Jugador 2 Gana";
                jugador1.points.Add("Pierde");
                jugador2.points.Add("Gana");
                AgregarPuntos(jugador2, jugador1, false);
            }
            partidas.Add((jugador1, jugador2, resultado, resultadoString));
            return $"\n{resultadoString}\n";
        }

        // Metodo dar puntos a los jugadores depues de una partida
        static void AgregarPuntos(Jugador ganador, Jugador perdedor, bool empate)
        {
            if (!empate)
            {
                clasificacion[ganador] = clasificacion.ContainsKey(ganador) ? clasificacion[ganador] + 3 : 3;
                if (ganador.nivel < perdedor.nivel) clasificacion[ganador] += 1;
            }
            else
            {
                clasificacion[ganador] = clasificacion.ContainsKey(ganador) ? clasificacion[ganador] + 1 : 1;
                clasificacion[perdedor] = clasificacion.ContainsKey(perdedor) ? clasificacion[perdedor] + 1 : 1;
            }
            
        }

    
    }
}
