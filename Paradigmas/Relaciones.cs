
// ' =============================================
// ' DIAGRAMA DE CLASES - PARQUE DE DIVERSIONES
// ' =============================================
// ' Este diagrama representa las clases, atributos y relaciones
// ' del sistema descrito en el enunciado del parque de diversiones.
// ' Cada clase es un elemento real del negocio, y las relaciones
// ' muestran cómo interactúan entre sí.
// ' =============================================

// ' ======== Clase Parque ========
// ' Representa el parque de diversiones en general.
// ' Tiene un nombre, un número total de manillas disponibles
// ' y métodos para acciones generales (ej.: abrir el parque).
// class Parque {
//     - nombre: string
//     - manillasTotales: int
//     + abrirParque(): void
// }

// ' ======== Clase Atraccion ========
// ' Representa una atracción dentro del parque.
// ' Cada atracción tiene un nombre, una duración en minutos,
// ' y la cantidad de puntos que cuesta ingresar.
// class Atraccion {
//     - nombre: string
//     - duracion: int ' en minutos
//     - puntosRequeridos: int
// }

// ' ======== Clase Taquilla ========
// ' Representa una taquilla física del parque.
// ' Tiene un ID único, el saldo en dinero que ha recaudado
// ' y la cantidad de manillas disponibles para entregar.
// ' Puede entregar manillas a las personas.
// class Taquilla {
//     - id: int
//     - saldoDinero: double
//     - manillasDisponibles: int
//     + entregarManilla(): Manilla
// }

// ' ======== Clase Persona ========
// ' Representa a un visitante del parque.
// ' Tiene un nombre y puede adquirir una manilla
// ' en una taquilla para usar las atracciones.
// class Persona {
//     - nombre: string
//     + adquirirManilla(): Manilla
// }

// ' ======== Clase Manilla ========
// ' Representa la pulsera que recibe el visitante.
// ' Tiene un ID interno, saldo en puntos y permite
// ' cargar dinero que se convierte en puntos.
// class Manilla {
//     - idInterno: int
//     - saldoPuntos: int
//     + cargarDinero(monto: double): void
// }

// ' ======== Clase Registro ========
// ' Representa el historial de uso de las atracciones.
// ' Guarda la hora de entrada y qué manilla usó
// ' en qué atracción.
// class Registro {
//     - horaEntrada: DateTime
//     + registrarEntrada(manilla: Manilla, atraccion: Atraccion): void
// }

// ' ======== RELACIONES ENTRE CLASES ========

// ' Un Parque tiene muchas Atracciones (1 → N)
// Parque "1" -- "10" Atraccion : contiene >

// ' Un Parque tiene varias Taquillas (1 → N)
// Parque "1" -- "3" Taquilla : dispone >

// ' Una Persona adquiere exactamente una Manilla
// Persona "1" -- "1" Manilla : usa >

// ' Una Taquilla entrega muchas Manillas (1 → N)
// Taquilla "1" -- "*" Manilla : entrega >

// ' Una Manilla se usa para acceder a varias Atracciones (1 → N)
// Manilla "1" -- "*" Atraccion : permiteAcceso >

// ' Un Registro guarda la relación entre una Manilla y una Atracción
// Registro "*" -- "1" Manilla
// Registro "*" -- "1" Atraccion

