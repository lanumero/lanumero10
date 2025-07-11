import React, { useState } from 'react';
import { Calendar, Users, Target, BookOpen, Clock, MapPin } from 'lucide-react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { mesociclos, sesionesSemanales, materialBasico } from '../data/mockData';
import MesociclosView from './MesociclosView';
import SesionDetalle from './SesionDetalle';

const Dashboard = () => {
  const [vistaActual, setVistaActual] = useState('dashboard');
  const [mesocicloSeleccionado, setMesocicloSeleccionado] = useState(null);
  const [sesionSeleccionada, setSesionSeleccionada] = useState(null);

  const handleMesocicloClick = (mesociclo) => {
    setMesocicloSeleccionado(mesociclo);
    setVistaActual('mesociclo');
  };

  const handleSesionClick = (sesion) => {
    setSesionSeleccionada(sesion);
    setVistaActual('sesion');
  };

  const volverDashboard = () => {
    setVistaActual('dashboard');
    setMesocicloSeleccionado(null);
    setSesionSeleccionada(null);
  };

  const volverMesociclo = () => {
    setVistaActual('mesociclo');
    setSesionSeleccionada(null);
  };

  if (vistaActual === 'sesion' && sesionSeleccionada) {
    return (
      <SesionDetalle 
        sesion={sesionSeleccionada} 
        onVolver={volverMesociclo}
      />
    );
  }

  if (vistaActual === 'mesociclo' && mesocicloSeleccionado) {
    return (
      <MesociclosView 
        mesociclo={mesocicloSeleccionado} 
        onVolver={volverDashboard}
        onSesionClick={handleSesionClick}
      />
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-blue-50 to-white p-4">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-3 bg-green-500 rounded-xl shadow-lg">
              <Target className="h-8 w-8 text-white" />
            </div>
            <div>
              <h1 className="text-4xl font-bold text-gray-800">
                Entrenamiento Fútbol 7
              </h1>
              <p className="text-xl text-gray-600">
                Categoría Benjamines - Planificación 5 Meses
              </p>
            </div>
          </div>
          
          <div className="flex flex-wrap gap-4 text-sm text-gray-600">
            <div className="flex items-center gap-2">
              <Calendar className="h-4 w-4" />
              <span>5 meses de entrenamiento</span>
            </div>
            <div className="flex items-center gap-2">
              <Clock className="h-4 w-4" />
              <span>3 sesiones semanales - 90 min c/u</span>
            </div>
            <div className="flex items-center gap-2">
              <Users className="h-4 w-4" />
              <span>Benjamines (8-10 años)</span>
            </div>
            <div className="flex items-center gap-2">
              <MapPin className="h-4 w-4" />
              <span>Fútbol 7</span>
            </div>
          </div>
        </div>

        {/* Resumen ejecutivo */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <Card className="bg-white shadow-lg border-0 hover:shadow-xl transition-all duration-300">
            <CardHeader className="pb-3">
              <CardTitle className="text-lg font-semibold text-gray-800">
                Total Sesiones
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-green-600">60</div>
              <p className="text-sm text-gray-600 mt-1">
                20 semanas × 3 sesiones
              </p>
            </CardContent>
          </Card>

          <Card className="bg-white shadow-lg border-0 hover:shadow-xl transition-all duration-300">
            <CardHeader className="pb-3">
              <CardTitle className="text-lg font-semibold text-gray-800">
                Horas Totales
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-blue-600">90</div>
              <p className="text-sm text-gray-600 mt-1">
                1.5 horas por sesión
              </p>
            </CardContent>
          </Card>

          <Card className="bg-white shadow-lg border-0 hover:shadow-xl transition-all duration-300">
            <CardHeader className="pb-3">
              <CardTitle className="text-lg font-semibold text-gray-800">
                Mesociclos
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-purple-600">5</div>
              <p className="text-sm text-gray-600 mt-1">
                Progresión estructurada
              </p>
            </CardContent>
          </Card>

          <Card className="bg-white shadow-lg border-0 hover:shadow-xl transition-all duration-300">
            <CardHeader className="pb-3">
              <CardTitle className="text-lg font-semibold text-gray-800">
                Ejercicios
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-3xl font-bold text-orange-600">360+</div>
              <p className="text-sm text-gray-600 mt-1">
                Variedad y progresión
              </p>
            </CardContent>
          </Card>
        </div>

        {/* Mesociclos */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-2">
            <BookOpen className="h-6 w-6" />
            Mesociclos de Entrenamiento
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {mesociclos.map((mesociclo, index) => (
              <Card 
                key={mesociclo.id} 
                className="bg-white shadow-lg border-0 hover:shadow-xl transition-all duration-300 cursor-pointer transform hover:scale-105"
                onClick={() => handleMesocicloClick(mesociclo)}
              >
                <CardHeader className="pb-3">
                  <div className="flex items-center justify-between">
                    <Badge className={`${mesociclo.color} text-white border-0`}>
                      {mesociclo.mes}
                    </Badge>
                    <span className="text-sm text-gray-500">
                      {mesociclo.semanas} semanas
                    </span>
                  </div>
                  <CardTitle className="text-lg font-semibold text-gray-800">
                    {mesociclo.nombre}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-gray-600 mb-4">
                    {mesociclo.descripcion}
                  </CardDescription>
                  <div className="bg-gray-50 p-3 rounded-lg">
                    <p className="text-sm font-medium text-gray-700 mb-1">
                      Objetivo Principal:
                    </p>
                    <p className="text-sm text-gray-600">
                      {mesociclo.objetivo}
                    </p>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>

        {/* Material necesario */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-2">
            <Target className="h-6 w-6" />
            Material Básico Necesario
          </h2>
          
          <Card className="bg-white shadow-lg border-0">
            <CardContent className="p-6">
              <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
                {materialBasico.map((material, index) => (
                  <div 
                    key={index} 
                    className="flex items-center gap-2 p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
                  >
                    <div className="w-2 h-2 bg-green-500 rounded-full flex-shrink-0"></div>
                    <span className="text-sm text-gray-700">{material}</span>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Información adicional */}
        <Card className="bg-gradient-to-r from-green-500 to-blue-600 text-white shadow-lg border-0">
          <CardContent className="p-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <h3 className="text-xl font-bold mb-3">Metodología</h3>
                <ul className="space-y-2 text-sm">
                  <li>• Enfoque lúdico y participativo</li>
                  <li>• Progresión adaptada a la edad</li>
                  <li>• Desarrollo integral del jugador</li>
                  <li>• Valores y trabajo en equipo</li>
                </ul>
              </div>
              <div>
                <h3 className="text-xl font-bold mb-3">Estructura de Sesión</h3>
                <ul className="space-y-2 text-sm">
                  <li>• Calentamiento (10-15 min)</li>
                  <li>• Parte principal (60-70 min)</li>
                  <li>• Vuelta a la calma (5-10 min)</li>
                  <li>• Reflexión y despedida</li>
                </ul>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Dashboard;