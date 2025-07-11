// Mock data for football training app
export const mesociclos = [
  {
    id: 1,
    nombre: "Adaptación y Familiarización",
    mes: "Mes 1",
    descripcion: "Introducción al fútbol 7, familiarización con el balón y adaptación física básica",
    color: "bg-blue-500",
    objetivo: "Crear una base sólida para el aprendizaje futuro",
    semanas: 4
  },
  {
    id: 2,
    nombre: "Técnica Individual Básica",
    mes: "Mes 2", 
    descripcion: "Desarrollo de habilidades técnicas fundamentales: pase, recepción, conducción",
    color: "bg-green-500",
    objetivo: "Dominar los fundamentos técnicos del fútbol",
    semanas: 4
  },
  {
    id: 3,
    nombre: "Técnica Individual Avanzada",
    mes: "Mes 3",
    descripcion: "Perfeccionamiento técnico y coordinación con balón",
    color: "bg-orange-500", 
    objetivo: "Mejorar la técnica individual y coordinación",
    semanas: 4
  },
  {
    id: 4,
    nombre: "Técnica Colectiva y Táctica",
    mes: "Mes 4",
    descripcion: "Introducción a conceptos tácticos básicos y juego colectivo",
    color: "bg-purple-500",
    objetivo: "Desarrollar el juego en equipo y nociones tácticas",
    semanas: 4
  },
  {
    id: 5,
    nombre: "Consolidación y Juego",
    mes: "Mes 5",
    descripcion: "Consolidación de aprendizajes y aplicación en situaciones reales de juego",
    color: "bg-red-500",
    objetivo: "Aplicar todos los conocimientos adquiridos",
    semanas: 4
  }
];

export const tiposSesiones = [
  {
    id: 1,
    nombre: "Sesión Técnica",
    descripcion: "Enfocada en el desarrollo de habilidades técnicas individuales",
    duracion: 90,
    color: "bg-blue-100 border-blue-300"
  },
  {
    id: 2,
    nombre: "Sesión Física-Coordinativa",
    descripcion: "Desarrollo de capacidades físicas y coordinativas adaptadas",
    duracion: 90,
    color: "bg-green-100 border-green-300"
  },
  {
    id: 3,
    nombre: "Sesión Táctica-Juego",
    descripcion: "Aplicación táctica y situaciones reales de juego",
    duracion: 90,
    color: "bg-orange-100 border-orange-300"
  }
];

export const sesionesSemanales = [
  {
    id: 1,
    mesocicloId: 1,
    semana: 1,
    sesiones: [
      {
        id: 1,
        tipo: "Técnica",
        nombre: "Familiarización con el balón",
        dia: "Lunes",
        duracion: 90,
        imagen: "https://images.unsplash.com/photo-1574242957680-7c8371ed191e",
        ejercicios: [
          {
            id: 1,
            nombre: "Saludo y presentación",
            duracion: 10,
            descripcion: "Círculo de presentación, explicación de reglas básicas",
            material: "Ninguno",
            objetivo: "Crear ambiente de confianza y establecer normas"
          },
          {
            id: 2,
            nombre: "Calentamiento dinámico",
            duracion: 15,
            descripcion: "Carrera suave, movilidad articular, estiramientos dinámicos",
            material: "Conos, silbato",
            objetivo: "Preparar el cuerpo para la actividad física"
          },
          {
            id: 3,
            nombre: "Toque libre con el balón",
            duracion: 20,
            descripcion: "Cada jugador con su balón, exploración libre de toques",
            material: "1 balón por jugador",
            objetivo: "Familiarización inicial con el balón"
          },
          {
            id: 4,
            nombre: "Conducción básica",
            duracion: 25,
            descripcion: "Conducción con ambos pies en línea recta y curvas",
            material: "Balones, conos",
            objetivo: "Desarrollar control básico del balón"
          },
          {
            id: 5,
            nombre: "Juego libre",
            duracion: 15,
            descripcion: "Partido libre 4vs4 sin reglas complejas",
            material: "Balones, porterías pequeñas",
            objetivo: "Aplicar lo aprendido en situación de juego"
          },
          {
            id: 6,
            nombre: "Vuelta a la calma",
            duracion: 5,
            descripcion: "Estiramientos suaves y reflexión del entrenamiento",
            material: "Ninguno",
            objetivo: "Relajación y evaluación positiva"
          }
        ]
      },
      {
        id: 2,
        tipo: "Física-Coordinativa",
        nombre: "Desarrollo coordinativo básico",
        dia: "Miércoles",
        duracion: 90,
        imagen: "https://images.unsplash.com/photo-1650897877790-0e171d2207dc",
        ejercicios: [
          {
            id: 1,
            nombre: "Activación corporal",
            duracion: 10,
            descripcion: "Movimientos articulares y activación muscular",
            material: "Ninguno",
            objetivo: "Preparar el cuerpo para el ejercicio"
          },
          {
            id: 2,
            nombre: "Circuito coordinativo",
            duracion: 25,
            descripcion: "Saltos, giros, desplazamientos laterales entre conos",
            material: "Conos, aros, escalera de coordinación",
            objetivo: "Desarrollar coordinación general"
          },
          {
            id: 3,
            nombre: "Equilibrio y propiocepción",
            duracion: 15,
            descripcion: "Ejercicios de equilibrio estático y dinámico",
            material: "Balones, superficies inestables",
            objetivo: "Mejorar el equilibrio y propiocepción"
          },
          {
            id: 4,
            nombre: "Velocidad de reacción",
            duracion: 20,
            descripcion: "Juegos de reacción a estímulos visuales y auditivos",
            material: "Conos de colores, silbato",
            objetivo: "Desarrollar velocidad de reacción"
          },
          {
            id: 5,
            nombre: "Juego coordinativo",
            duracion: 15,
            descripcion: "Juegos que combinen coordinación y diversión",
            material: "Balones, conos",
            objetivo: "Aplicar coordinación en contexto lúdico"
          },
          {
            id: 6,
            nombre: "Relajación",
            duracion: 5,
            descripcion: "Respiración y relajación muscular",
            material: "Ninguno",
            objetivo: "Vuelta a la calma progresiva"
          }
        ]
      },
      {
        id: 3,
        tipo: "Táctica-Juego",
        nombre: "Introducción al juego colectivo",
        dia: "Viernes",
        duracion: 90,
        imagen: "https://images.unsplash.com/photo-1573639615462-3a16eabd9390",
        ejercicios: [
          {
            id: 1,
            nombre: "Calentamiento con balón",
            duracion: 15,
            descripcion: "Trote suave conduciendo el balón",
            material: "1 balón por jugador",
            objetivo: "Activación con familiarización del balón"
          },
          {
            id: 2,
            nombre: "Pases por parejas",
            duracion: 20,
            descripcion: "Pases cortos estáticos, aumentando progresivamente la distancia",
            material: "Balones",
            objetivo: "Introducir el concepto de pase"
          },
          {
            id: 3,
            nombre: "Juego de persecución",
            duracion: 15,
            descripcion: "El que la pica debe tocar con el balón controlado",
            material: "Balones",
            objetivo: "Combinar diversión con control del balón"
          },
          {
            id: 4,
            nombre: "Partidillo 3vs3",
            duracion: 25,
            descripcion: "Partidos cortos con rotaciones, porterías pequeñas",
            material: "Balones, porterías pequeñas, petos",
            objetivo: "Aplicar conceptos básicos en situación real"
          },
          {
            id: 5,
            nombre: "Tiros a portería",
            duracion: 10,
            descripcion: "Tiros libres desde diferentes posiciones",
            material: "Balones, porterías",
            objetivo: "Desarrollar la precisión en el tiro"
          },
          {
            id: 6,
            nombre: "Charla final",
            duracion: 5,
            descripcion: "Comentarios positivos y despedida",
            material: "Ninguno",
            objetivo: "Refuerzo positivo y motivación"
          }
        ]
      }
    ]
  },
  {
    id: 2,
    mesocicloId: 1,
    semana: 2,
    sesiones: [
      {
        id: 4,
        tipo: "Técnica",
        nombre: "Dominio básico del balón",
        dia: "Lunes",
        duracion: 90,
        imagen: "https://images.unsplash.com/photo-1638027611065-7eb0b8cfd4fb",
        ejercicios: [
          {
            id: 1,
            nombre: "Calentamiento dinámico",
            duracion: 15,
            descripcion: "Activación muscular con ejercicios variados",
            material: "Conos",
            objetivo: "Preparación física y mental"
          },
          {
            id: 2,
            nombre: "Toques con diferentes partes del pie",
            duracion: 25,
            descripcion: "Interior, exterior, empeine, exploración de superficies",
            material: "1 balón por jugador",
            objetivo: "Conocer las diferentes formas de tocar el balón"
          },
          {
            id: 3,
            nombre: "Malabares básicos",
            duracion: 20,
            descripcion: "Toques consecutivos con el pie, intentar 2-3 toques",
            material: "Balones",
            objetivo: "Desarrollar coordinación óculo-pédica"
          },
          {
            id: 4,
            nombre: "Conducción con obstáculos",
            duracion: 20,
            descripcion: "Slalom simple entre conos a ritmo controlado",
            material: "Balones, conos",
            objetivo: "Mejorar control en movimiento"
          },
          {
            id: 5,
            nombre: "Juego del espejo",
            duracion: 5,
            descripcion: "Por parejas, uno conduce y el otro imita",
            material: "Balones",
            objetivo: "Desarrollar creatividad y observación"
          },
          {
            id: 6,
            nombre: "Estiramiento final",
            duracion: 5,
            descripcion: "Estiramientos estáticos principales grupos musculares",
            material: "Ninguno",
            objetivo: "Prevención de lesiones y relajación"
          }
        ]
      },
      {
        id: 5,
        tipo: "Física-Coordinativa",
        nombre: "Agilidad y coordinación",
        dia: "Miércoles",
        duracion: 90,
        imagen: "https://images.pexels.com/photos/2403029/pexels-photo-2403029.jpeg",
        ejercicios: [
          {
            id: 1,
            nombre: "Entrada en calor",
            duracion: 10,
            descripcion: "Trote suave con cambios de dirección",
            material: "Conos",
            objetivo: "Activación cardiovascular"
          },
          {
            id: 2,
            nombre: "Escalera de coordinación",
            duracion: 20,
            descripcion: "Diferentes patrones de pisada en escalera",
            material: "Escalera de coordinación",
            objetivo: "Mejorar coordinación de piernas"
          },
          {
            id: 3,
            nombre: "Saltos coordinados",
            duracion: 15,
            descripcion: "Saltos con un pie, dos pies, laterales",
            material: "Aros, conos",
            objetivo: "Desarrollar potencia y coordinación"
          },
          {
            id: 4,
            nombre: "Cambios de dirección",
            duracion: 20,
            descripcion: "Sprints cortos con cambios de dirección señalizados",
            material: "Conos de colores",
            objetivo: "Agilidad y velocidad de reacción"
          },
          {
            id: 5,
            nombre: "Relevos coordinativos",
            duracion: 20,
            descripcion: "Competencia por equipos con ejercicios coordinativos",
            material: "Conos, aros, balones",
            objetivo: "Aplicar coordinación en contexto competitivo"
          },
          {
            id: 6,
            nombre: "Vuelta a la calma",
            duracion: 5,
            descripcion: "Caminata suave y respiración profunda",
            material: "Ninguno",
            objetivo: "Recuperación progresiva"
          }
        ]
      },
      {
        id: 6,
        tipo: "Táctica-Juego",
        nombre: "Primeros conceptos de equipo",
        dia: "Viernes",
        duracion: 90,
        imagen: "https://images.pexels.com/photos/8028410/pexels-photo-8028410.jpeg",
        ejercicios: [
          {
            id: 1,
            nombre: "Calentamiento con balón",
            duracion: 15,
            descripcion: "Conducción libre por el espacio evitando choques",
            material: "Balones",
            objetivo: "Activación con percepción espacial"
          },
          {
            id: 2,
            nombre: "Pase y recepción",
            duracion: 25,
            descripcion: "Pases por parejas, enfatizar control y precisión",
            material: "Balones",
            objetivo: "Mejorar técnica de pase básico"
          },
          {
            id: 3,
            nombre: "Juego de posesión",
            duracion: 20,
            descripcion: "4 jugadores dentro, 2 fuera intentan recuperar",
            material: "Balones, conos para delimitar área",
            objetivo: "Introducir concepto de posesión"
          },
          {
            id: 4,
            nombre: "Partiditos reducidos",
            duracion: 25,
            descripcion: "Partidos 4vs4 con rotaciones cada 5 minutos",
            material: "Balones, porterías pequeñas, petos",
            objetivo: "Aplicar conceptos en situación real"
          },
          {
            id: 5,
            nombre: "Evaluación positiva",
            duracion: 5,
            descripcion: "Comentarios individuales positivos sobre mejoras",
            material: "Ninguno",
            objetivo: "Refuerzo positivo y motivación"
          }
        ]
      }
    ]
  }
];

export const materialBasico = [
  "Balones de fútbol (nº 3 o 4)",
  "Conos de diferentes colores",
  "Petos o camisetas de entrenamiento",
  "Porterías pequeñas (portátiles)",
  "Aros de coordinación",
  "Escalera de coordinación",
  "Silbato",
  "Cronómetro",
  "Bidones de agua",
  "Botiquín básico"
];

export const objetivosPorMes = {
  1: ["Familiarización con el balón", "Coordinación básica", "Diversión y participación"],
  2: ["Técnica individual", "Pase y recepción", "Control del balón"],
  3: ["Perfeccionamiento técnico", "Coordinación avanzada", "Creatividad"],
  4: ["Juego colectivo", "Conceptos tácticos básicos", "Competencia sana"],
  5: ["Consolidación", "Aplicación práctica", "Evaluación final"]
};