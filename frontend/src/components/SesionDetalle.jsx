import React, { useState } from 'react';
import { ArrowLeft, Clock, Target, Package, Users, Play, CheckCircle } from 'lucide-react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Progress } from './ui/progress';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from './ui/accordion';

const SesionDetalle = ({ sesion, onVolver }) => {
  const [ejerciciosCompletados, setEjerciciosCompletados] = useState(new Set());
  const [tiempoTranscurrido, setTiempoTranscurrido] = useState(0);

  const toggleEjercicio = (ejercicioId) => {
    const nuevosCompletados = new Set(ejerciciosCompletados);
    if (nuevosCompletados.has(ejercicioId)) {
      nuevosCompletados.delete(ejercicioId);
    } else {
      nuevosCompletados.add(ejercicioId);
    }
    setEjerciciosCompletados(nuevosCompletados);
  };

  const progreso = (ejerciciosCompletados.size / sesion.ejercicios.length) * 100;

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-blue-50 to-white p-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <Button 
            variant="ghost" 
            onClick={onVolver}
            className="mb-4 hover:bg-white hover:shadow-md transition-all duration-200"
          >
            <ArrowLeft className="h-4 w-4 mr-2" />
            Volver al Mesociclo
          </Button>
          
          <div className="flex items-center gap-4 mb-6">
            <div className="relative">
              <img 
                src={sesion.imagen} 
                alt={sesion.nombre}
                className="w-20 h-20 object-cover rounded-xl shadow-lg"
              />
              <div className="absolute -top-2 -right-2">
                <Badge className="bg-green-500 text-white border-0">
                  {sesion.dia}
                </Badge>
              </div>
            </div>
            <div className="flex-1">
              <h1 className="text-3xl font-bold text-gray-800 mb-2">
                {sesion.nombre}
              </h1>
              <p className="text-lg text-gray-600 mb-2">
                {sesion.tipo} - {sesion.duracion} minutos
              </p>
              <div className="flex flex-wrap gap-3 text-sm text-gray-600">
                <div className="flex items-center gap-1">
                  <Clock className="h-4 w-4" />
                  <span>{sesion.duracion} min</span>
                </div>
                <div className="flex items-center gap-1">
                  <Users className="h-4 w-4" />
                  <span>Benjamines</span>
                </div>
                <div className="flex items-center gap-1">
                  <Target className="h-4 w-4" />
                  <span>{sesion.ejercicios.length} ejercicios</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Progreso de la sesión */}
        <Card className="mb-8 bg-white shadow-lg border-0">
          <CardHeader>
            <CardTitle className="text-xl font-bold text-gray-800 flex items-center gap-2">
              <Play className="h-5 w-5" />
              Progreso de la Sesión
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">
                  Ejercicios completados: {ejerciciosCompletados.size} de {sesion.ejercicios.length}
                </span>
                <span className="text-sm font-semibold text-green-600">
                  {Math.round(progreso)}%
                </span>
              </div>
              <Progress value={progreso} className="h-2" />
            </div>
          </CardContent>
        </Card>

        {/* Ejercicios */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-2">
            <Target className="h-6 w-6" />
            Ejercicios de la Sesión
          </h2>
          
          <Accordion type="single" collapsible className="space-y-4">
            {sesion.ejercicios.map((ejercicio, index) => (
              <AccordionItem key={ejercicio.id} value={`ejercicio-${ejercicio.id}`}>
                <Card className={`shadow-lg border-0 ${ejerciciosCompletados.has(ejercicio.id) ? 'bg-green-50 border-green-200' : 'bg-white'}`}>
                  <AccordionTrigger className="p-0 border-0 hover:no-underline">
                    <CardHeader className="w-full">
                      <div className="flex items-center justify-between w-full">
                        <div className="flex items-center gap-4">
                          <div className={`w-8 h-8 rounded-full flex items-center justify-center text-white font-bold ${ejerciciosCompletados.has(ejercicio.id) ? 'bg-green-500' : 'bg-gray-400'}`}>
                            {ejerciciosCompletados.has(ejercicio.id) ? (
                              <CheckCircle className="h-5 w-5" />
                            ) : (
                              index + 1
                            )}
                          </div>
                          <div className="text-left">
                            <CardTitle className="text-lg font-semibold text-gray-800">
                              {ejercicio.nombre}
                            </CardTitle>
                            <CardDescription className="text-sm text-gray-600">
                              {ejercicio.duracion} minutos
                            </CardDescription>
                          </div>
                        </div>
                        <div className="flex items-center gap-2">
                          <Badge variant="outline" className="bg-blue-50 border-blue-200 text-blue-700">
                            {ejercicio.duracion} min
                          </Badge>
                          <Button
                            size="sm"
                            variant={ejerciciosCompletados.has(ejercicio.id) ? "default" : "outline"}
                            onClick={(e) => {
                              e.stopPropagation();
                              toggleEjercicio(ejercicio.id);
                            }}
                            className={ejerciciosCompletados.has(ejercicio.id) ? "bg-green-500 hover:bg-green-600" : ""}
                          >
                            {ejerciciosCompletados.has(ejercicio.id) ? 'Completado' : 'Marcar'}
                          </Button>
                        </div>
                      </div>
                    </CardHeader>
                  </AccordionTrigger>
                  
                  <AccordionContent className="p-0 border-0">
                    <CardContent className="pt-0">
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div className="space-y-4">
                          <div>
                            <h4 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
                              <Target className="h-4 w-4" />
                              Descripción
                            </h4>
                            <p className="text-gray-600 text-sm leading-relaxed">
                              {ejercicio.descripcion}
                            </p>
                          </div>
                          
                          <div>
                            <h4 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
                              <Package className="h-4 w-4" />
                              Material Necesario
                            </h4>
                            <Badge variant="outline" className="bg-orange-50 border-orange-200 text-orange-700">
                              {ejercicio.material}
                            </Badge>
                          </div>
                        </div>
                        
                        <div>
                          <h4 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
                            <Target className="h-4 w-4" />
                            Objetivo
                          </h4>
                          <div className="bg-gray-50 p-3 rounded-lg">
                            <p className="text-sm text-gray-700">
                              {ejercicio.objetivo}
                            </p>
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </AccordionContent>
                </Card>
              </AccordionItem>
            ))}
          </Accordion>
        </div>

        {/* Notas y consejos */}
        <Card className="bg-blue-50 border-blue-200 shadow-lg">
          <CardContent className="p-6">
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 bg-blue-400 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                <span className="text-blue-800 text-sm font-bold">💡</span>
              </div>
              <div>
                <h3 className="font-bold text-blue-800 mb-2">Consejos para el Entrenador</h3>
                <ul className="text-sm text-blue-700 space-y-1">
                  <li>• Mantén un ambiente positivo y motivador</li>
                  <li>• Adapta los ejercicios según las necesidades del grupo</li>
                  <li>• Fomenta la participación de todos los jugadores</li>
                  <li>• Asegúrate de que todos comprendan los ejercicios</li>
                  <li>• Recuerda hidratarse durante la sesión</li>
                </ul>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default SesionDetalle;