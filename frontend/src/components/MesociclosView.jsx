import React from 'react';
import { ArrowLeft, Calendar, Clock, Users, Target, PlayCircle } from 'lucide-react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { sesionesSemanales, objetivosPorMes } from '../data/mockData';

const MesociclosView = ({ mesociclo, onVolver, onSesionClick }) => {
  const sesionesDelMesociclo = sesionesSemanales.filter(
    semana => semana.mesocicloId === mesociclo.id
  );

  const objetivos = objetivosPorMes[mesociclo.id] || [];

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-blue-50 to-white p-4">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <Button 
            variant="ghost" 
            onClick={onVolver}
            className="mb-4 hover:bg-white hover:shadow-md transition-all duration-200"
          >
            <ArrowLeft className="h-4 w-4 mr-2" />
            Volver al Dashboard
          </Button>
          
          <div className="flex items-center gap-4 mb-6">
            <div className={`p-4 ${mesociclo.color} rounded-xl shadow-lg`}>
              <Target className="h-8 w-8 text-white" />
            </div>
            <div>
              <h1 className="text-4xl font-bold text-gray-800">
                {mesociclo.nombre}
              </h1>
              <p className="text-xl text-gray-600">
                {mesociclo.mes} - {mesociclo.descripcion}
              </p>
            </div>
          </div>

          <div className="flex flex-wrap gap-4 text-sm text-gray-600">
            <div className="flex items-center gap-2">
              <Calendar className="h-4 w-4" />
              <span>{mesociclo.semanas} semanas</span>
            </div>
            <div className="flex items-center gap-2">
              <Clock className="h-4 w-4" />
              <span>3 sesiones por semana - 90 min c/u</span>
            </div>
            <div className="flex items-center gap-2">
              <Users className="h-4 w-4" />
              <span>Benjamines (8-10 años)</span>
            </div>
          </div>
        </div>

        {/* Objetivos del mesociclo */}
        <Card className="mb-8 bg-white shadow-lg border-0">
          <CardHeader>
            <CardTitle className="text-xl font-bold text-gray-800 flex items-center gap-2">
              <Target className="h-5 w-5" />
              Objetivos del Mesociclo
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {objetivos.map((objetivo, index) => (
                <div key={index} className="flex items-center gap-3 p-3 bg-gray-50 rounded-lg">
                  <div className="w-2 h-2 bg-green-500 rounded-full flex-shrink-0"></div>
                  <span className="text-gray-700">{objetivo}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Información general */}
        <Card className="mb-8 bg-gradient-to-r from-green-500 to-blue-600 text-white shadow-lg border-0">
          <CardContent className="p-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <h3 className="text-xl font-bold mb-3">Enfoque del Mesociclo</h3>
                <p className="text-sm opacity-90">
                  {mesociclo.objetivo}
                </p>
              </div>
              <div>
                <h3 className="text-xl font-bold mb-3">Metodología</h3>
                <ul className="space-y-1 text-sm opacity-90">
                  <li>• Aprendizaje progresivo</li>
                  <li>• Adaptación a la edad</li>
                  <li>• Enfoque lúdico</li>
                  <li>• Desarrollo integral</li>
                </ul>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Sesiones semanales */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-2">
            <PlayCircle className="h-6 w-6" />
            Sesiones Semanales
          </h2>
          
          {sesionesDelMesociclo.map((semana) => (
            <Card key={semana.id} className="mb-6 bg-white shadow-lg border-0">
              <CardHeader>
                <CardTitle className="text-lg font-semibold text-gray-800">
                  Semana {semana.semana}
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  {semana.sesiones.map((sesion) => (
                    <Card 
                      key={sesion.id} 
                      className="cursor-pointer hover:shadow-lg transition-all duration-300 transform hover:scale-105 border-2 border-gray-100 hover:border-green-300"
                      onClick={() => onSesionClick(sesion)}
                    >
                      <div className="relative">
                        <img 
                          src={sesion.imagen} 
                          alt={sesion.nombre}
                          className="w-full h-32 object-cover rounded-t-lg"
                        />
                        <div className="absolute top-2 right-2">
                          <Badge className="bg-white text-gray-800 border-0">
                            {sesion.dia}
                          </Badge>
                        </div>
                      </div>
                      <CardHeader className="pb-2">
                        <CardTitle className="text-base font-semibold text-gray-800">
                          {sesion.nombre}
                        </CardTitle>
                        <CardDescription className="text-sm">
                          {sesion.tipo} - {sesion.duracion} min
                        </CardDescription>
                      </CardHeader>
                      <CardContent>
                        <div className="flex justify-between items-center">
                          <span className="text-sm text-gray-600">
                            {sesion.ejercicios.length} ejercicios
                          </span>
                          <Button 
                            size="sm" 
                            className="bg-green-500 hover:bg-green-600"
                            onClick={(e) => {
                              e.stopPropagation();
                              onSesionClick(sesion);
                            }}
                          >
                            Ver Sesión
                          </Button>
                        </div>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Nota metodológica */}
        <Card className="bg-yellow-50 border-yellow-200 shadow-lg">
          <CardContent className="p-6">
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 bg-yellow-400 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                <span className="text-yellow-800 text-sm font-bold">!</span>
              </div>
              <div>
                <h3 className="font-bold text-yellow-800 mb-2">Nota Metodológica</h3>
                <p className="text-sm text-yellow-700">
                  Recuerda que cada sesión está diseñada para ser adaptable según las necesidades del grupo. 
                  Los tiempos son orientativos y pueden modificarse según la respuesta de los jugadores. 
                  La diversión y el aprendizaje son prioritarios sobre el rendimiento.
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default MesociclosView;