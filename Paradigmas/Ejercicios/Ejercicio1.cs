using static p_puntos_superm.Program;

namespace p_puntos_superm
{
    //Este es un programa basado en programación modular o por funciones. 
    //El reto es usar los conceptos del repaso para mejorarlo.
    //Controlando los errores tanto en el programa principal como en las funciones. En estas últimas los errores deben ser arrojados al main
    //quien será el único que los podrá escribir
    //Eliminando todos los Console de las funciones

    // Creamos las clases
    internal class Cliente
    {
        public uint id { get; set; }
        public string nombre { get; set; }
        public ulong telefono { get; set; }
        public string direccion { get; set; }
        public ulong saldoPuntos { get; set; }
        public Cliente(uint id, string nombre, ulong telefono, string direccion)
        {
            this.id = id;
            this.nombre = nombre;
            this.telefono = telefono;
            this.direccion = direccion;
            this.saldoPuntos = 0;
        }

    }

    internal class Premio
    {
        public ulong min { get; set; }
        public ulong max { get; set; }
        public string descipcion { get; set; }

        public Premio(ulong min, ulong max, string descripcion)
        {
            this.min = min;
            this.max = max;
            this.descipcion = descripcion;
        }
    }

    internal class Registro
    {
        public int caja { get; set; }
        public uint clienteId { get; set; }
        public ulong compra { get; set; }
        public ulong puntos { get; set; }
        public DateTime fecha { get; set; }

        public Registro(int caja, uint clienteId, ulong compra, ulong puntos, DateTime fecha)
        {
            this.caja = caja;
            this.clienteId = clienteId;
            this.compra = compra;
            this.puntos = puntos;
            this.fecha = fecha;
        }
    }

    internal class Program
    {
       

        // Constantes Globales
        const ushort PesosPorPunto = 500;
        const byte CantCajasPorSuper = 4;

        // Variables globales
        static ulong[] saldosVentas = new ulong[CantCajasPorSuper];

        static List<Cliente> clientes = new List<Cliente>();

        static List<Premio> premios = new List<Premio>();

        static List<Registro> registros = new List<Registro>();

        static bool[] cajasAbiertas = new bool[CantCajasPorSuper];

        static void Main(string[] args)
        {
            // Abre la caja
            try
            {
                AbrirCaja(0);
                Console.WriteLine($"Caja {0} abierta");
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            
            RegistrarCliente(new Cliente(1, "Ana", 3210001111, "Calle 1"));
            AdicionarPremio(new Premio(100, 500, "Descuento 5%"));
            AdicionarPremio(new Premio(501, 1000, "Descuento 10%"));

            try
            {
                Console.WriteLine(RegistrarCompra(0, 1, 25000));
                Console.WriteLine(RegistrarCompra(0, 2, 60000));
            }
            catch (Exception e) 
            {
                Console.WriteLine(e.Message);
            }
         
            Console.WriteLine(ConsultarPremios(1));

            try
            {
                Console.WriteLine(CerrarCaja(0));
            }
            catch (Exception e) 
            {
                Console.WriteLine(e.Message);
            }
        }

        static void AbrirCaja(int numeroCaja)
        {
            // Vemos si es numero de caja valido
            if (numeroCaja < 0 || numeroCaja >= CantCajasPorSuper) throw new Exception("Número de caja inválido");
            // Abrimos la caja si esta cerrada
            cajasAbiertas[numeroCaja] = (cajasAbiertas[numeroCaja]) ? throw new Exception($"Caja {numeroCaja} ya estaba abierta") : true; 
            
        }

        static string CerrarCaja(int numeroCaja)
        {
            // Creamos las Variables
            ulong saldo;
            // Vemos q si este abierta y la cerramos
            cajasAbiertas[numeroCaja] = (!cajasAbiertas[numeroCaja]) ? throw new Exception($"La caja {numeroCaja} ya está cerrada") : false;
            // Guardamos la cantidad vendida
            saldo = saldosVentas[numeroCaja];
            // Reiniciamos su valor
            saldosVentas[numeroCaja] = 0;

            return $"Se recogió en la caja {numeroCaja}: {saldo:C2}";
        }

        static void RegistrarCliente(Cliente objCliente) => clientes.Add(objCliente);
       
        static void AdicionarPremio(Premio objPremio) => premios.Add(objPremio);
   
        static string RegistrarCompra(int numeroCaja, uint clienteId, ulong valorCompra)
        {
            // Creamos la varibles
            ulong puntosGanados;
            int indexCliente;

            // Revisamos que la caja este abierta
            if (!cajasAbiertas[numeroCaja]) throw new Exception($"No se puede registrar la compra: caja {numeroCaja} está cerrada.");
            
            // Revisamos que el cliente exita
            indexCliente = clientes.FindIndex(c => c.id == clienteId);
            if (indexCliente == -1) throw new Exception("Cliente no encontrado");

            // Calculamos los puntos ganados
            puntosGanados = valorCompra / PesosPorPunto;

            // Le sumamos los puntos ganados
            clientes[indexCliente].saldoPuntos += puntosGanados;
            
            // Sumamos el valor de compra a la - saldo
            saldosVentas[numeroCaja] += valorCompra;
            // Registramos la compra
            registros.Add(new Registro(numeroCaja, clienteId, valorCompra, puntosGanados, DateTime.Now));

            return $"Compra registrada: Cliente {clienteId}, Puntos ganados {puntosGanados}";
        }

        static string ConsultarPremios(uint clienteId)
        {

            // Creamos las varibles
            string resultado;
            Cliente? cliente;

            // Buscamos el cliente
            cliente = clientes.Find(p => p.id == clienteId);
            
            // Verificamos que exita
            if (cliente!.id == 0) throw new Exception("Cliente no encontrado");

            // Concatenamos el resultado
            resultado = $"El cliente {cliente.nombre} puede reclamar con {cliente.saldoPuntos} puntos:\n";

            var premiosGanados = premios.Where(premio => cliente.saldoPuntos >= premio.min && cliente.saldoPuntos <= premio.max);
            resultado += string.Join("", premios.Select(premio => $"- {premio.descipcion}\n"));

            return resultado;
        }

    }
}
