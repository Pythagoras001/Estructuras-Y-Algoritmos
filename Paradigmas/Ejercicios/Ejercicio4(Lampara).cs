using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p_Lamparas
{
    internal class Lampara
    {

        // Lista de opciones
        public enum l_Color {Negro, Cromo, Rojo};
        public enum l_Voltaje { Voltaje110=110, Voltaje220=220};
        public enum l_Tipo { Alogena, Led}

        // Atributos de Usuario
        private string? _marca;
        private uint _duracionHoras;
        private float _longitudCable;

        public l_Color color;
        public l_Voltaje voltaje;
        public l_Tipo tipo;

        // Atributos de estado
        private bool _estadoEncendido;
        private string? _tableroConexion;


        // Creamos el constructor
        public Lampara() 
        {
            _estadoEncendido = false;
            _tableroConexion = "Sin Conectar Aun";
        }

        public Lampara(string? marca, uint duracionHoras, float longitudCable, l_Color color, l_Voltaje voltaje, l_Tipo tipo) : this()
        {
            Marca = marca;
            DuracionHoras = duracionHoras;
            LongitudCable = longitudCable;
            this.color = color;
            this.voltaje = voltaje;
            this.tipo = tipo;
        }

        // Creamos los accesores
        public string? Marca {
            get => _marca!;

            set => _marca = (value?.Replace(" ", "").Length ?? 0) > 6 
                ? value!.ToUpper()
                : throw new Exception("Marca Invalida");
        }

        public uint DuracionHoras { 
            get => _duracionHoras; 
            set => _duracionHoras = value >= 500000 && value <= 1000000 ? value : throw new Exception("Duracion de Lampara Invalida"); 
        }

        public float LongitudCable { 
            get => _longitudCable; 
            set => _longitudCable = value >= 1.5 && value <= 4.5 ? value : throw new Exception("Longitud del cable Invalida");
        }

        public string TableroConexion {get => _tableroConexion!;}
        public bool EstadoEncendido {get => _estadoEncendido;}


        // Creamos los metodos
        public void EncenderApagarLampara() => _estadoEncendido = !_estadoEncendido ? true : false;

        public string CambiarBombilla() => _estadoEncendido ? throw new Exception("Debe Apagar La Bombilla Primero") : "Cambio Exitoso";

        public string CambiarCable(float newLongitud)
        {
            try
            {
                if (_estadoEncendido) throw new Exception("No se puede cambiar el cable con la bombilla encendida");
                LongitudCable = newLongitud;
                return "Cambio Exitoso";
            }
            catch (Exception ex)
            {
                throw new Exception(ex.Message);
            }
        }

        public void AsignarTablero(string codigoTablero) => _tableroConexion = codigoTablero.Length >= 6 ? codigoTablero : throw new Exception("Codigo Invalido");

        public string VerEstado() => $"Estado: {(EstadoEncendido ? "Prendida" : "Apagada")} \n" +
            $"Longitud del Cable: {LongitudCable}\n" +
            $"Duracion: {DuracionHoras} Horas";
    }
}
