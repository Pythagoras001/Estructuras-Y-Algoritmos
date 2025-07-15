using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AlquilerDePeliculas.Clases
{

    // Clase cliente determina los atributos y controla con propiedades
    internal class Cliente
    {
        // Atrbiutos privados de la clase Cliente
        private string? _nombre;
        private int _edad;
        private int _numeroDeIdentificacion;
        private List<Alquiler> _alquileres = new List<Alquiler>();

        // Constructor de la clase Cliente
        public Cliente(string nombre, int edad, int numeroDeIdentificacion)
        {
            Nombre = nombre;
            Edad = edad;
            NumeroDeIdentificacion = numeroDeIdentificacion;

        }

        // Propiedades públicas para acceder a los atributos privados
        public string Nombre
        {
            get { return _nombre!; }
            set
            {
                if (!string.IsNullOrEmpty(value))
                {
                    _nombre = value;
                }
                else
                {
                    throw new Exception("El nombre no puede estar vacío.");
                }
            }
        }

        public int Edad
        {
            get { return _edad; }
            set
            {
                if (!(value < 5 || value > 100))
                {
                    _edad = value;
                }
                else
                {
                    throw new Exception("La edad debe estar entre 5 y 100 años.");
                }
            }
        }

        public int NumeroDeIdentificacion
        {
            get { return _numeroDeIdentificacion; }
            set
            {
                if (value > 0)
                {
                    _numeroDeIdentificacion = value;
                }
                else
                {
                    throw new Exception("El número de identificación debe ser un número positivo.");
                }
            }
        }

        public List<Alquiler> Alquileres
        {
            get { return _alquileres; }
        }

    }

    // Clase para agregar un prestamo a un clinete
    internal class ServicePrestamo
    {
        public void AgregarPrestamo(Cliente cliente, Alquiler alquiler)
        {
            cliente.Alquileres.Add(alquiler);
        }
    }

    // Clase para mostrar la info a un cliente
    internal class ServiceInfoCliente
    {
        public void MostrarInfoCliente(Cliente cliente)
        {
            Console.WriteLine($"Nombre: {cliente.Nombre}" +
                $"Edad: {cliente.Edad}" +
                $"ID User: {cliente.NumeroDeIdentificacion}" +
                $"Peliculas Prestadas: ");

            cliente.Alquileres.ForEach(x => Console.Write($"Nombre: {x}\n"));
        }
    }

    internal class SistemaCliente
    {
        public ServicePrestamo servicePrestamo = new();
        public ServiceInfoCliente serviceInfoCliente = new();

        public void MostarInfo(Cliente cliente)
        {
            serviceInfoCliente.MostrarInfoCliente(cliente);
        }

        public void AgregarPrestamo(Alquiler alquiler, Cliente cliente)
        {
            servicePrestamo.AgregarPrestamo(cliente, alquiler);
        }

    }
}
