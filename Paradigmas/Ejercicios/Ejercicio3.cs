using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p_Bicicleta.Clases
{
    internal class Bicicleta
    {

        // Definimos los atributos
        private char _tamMarco;
        private float _tamLlanta;
        private string? _material;
        private byte _cantCambios;

        // Creamos el constructor
        public Bicicleta(char _tamMarco, float _tamLlanta, string _material, byte _cantCambios)
        {
          
            TamMarco = _tamMarco;
            TamLlanta = _tamLlanta;
            Material = _material;
            CantCambios = _cantCambios;

        }

        // Creamos los accesores
        public char TamMarco {

            get { return _tamMarco; }

            set 
            {
                char[] marcosDisponibles = new char[] { 'S', 'M', 'L', 'X' };
                _tamMarco = marcosDisponibles.Contains(value) ? value : throw new Exception("Marco Invalido"); 
            } 
        }

        public float TamLlanta
        {
            get => _tamLlanta;
            set
            {
                float[] llantasDisponibles = new float[] {15f, 15.5f, 20f, 20.5f};
                _tamLlanta = llantasDisponibles.Contains(value) ? value : throw new Exception("Tam de llanta invalida") ;
            }
        }

        public string Material
        {
            get => _material;
            set
            {
                string[] materialesDisponibles = new string[] { "Aluminio", "Fibra de carbono", "Acero" };
                _material = materialesDisponibles.Contains(value) ? value : throw new Exception("Material Invalido");
            }
        }

        public byte CantCambios
        {
            get => _cantCambios;
            set
            {
                byte[] cambiosDisponibles = new byte[] { 7, 8, 10 };
                _cantCambios = cambiosDisponibles.Contains(value) ? value : throw new Exception("Cantidad de cambios Invalida");
            }
        }
    }
}
