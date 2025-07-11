#!/usr/bin/env python3
"""
Comprehensive Backend Testing for Football Training Application
Tests all API endpoints, data models, and service functionality
"""

import asyncio
import aiohttp
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Any

# Get backend URL from frontend .env file
def get_backend_url():
    try:
        with open('/app/frontend/.env', 'r') as f:
            for line in f:
                if line.startswith('REACT_APP_BACKEND_URL='):
                    return line.split('=', 1)[1].strip()
    except Exception as e:
        print(f"Error reading frontend .env: {e}")
        return None

BACKEND_URL = get_backend_url()
if not BACKEND_URL:
    print("ERROR: Could not get REACT_APP_BACKEND_URL from frontend/.env")
    sys.exit(1)

API_BASE_URL = f"{BACKEND_URL}/api"

class FootballAPITester:
    def __init__(self):
        self.session = None
        self.test_results = {
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'errors': [],
            'test_details': []
        }
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    def log_test(self, test_name: str, passed: bool, details: str = "", error: str = ""):
        """Log test result"""
        self.test_results['total_tests'] += 1
        if passed:
            self.test_results['passed_tests'] += 1
            status = "✅ PASS"
        else:
            self.test_results['failed_tests'] += 1
            status = "❌ FAIL"
            if error:
                self.test_results['errors'].append(f"{test_name}: {error}")
        
        self.test_results['test_details'].append({
            'test': test_name,
            'status': status,
            'details': details,
            'error': error
        })
        
        print(f"{status}: {test_name}")
        if details:
            print(f"   Details: {details}")
        if error:
            print(f"   Error: {error}")
    
    async def test_health_check(self):
        """Test API health check endpoint"""
        try:
            async with self.session.get(f"{API_BASE_URL}/") as response:
                if response.status == 200:
                    data = await response.json()
                    if "message" in data and "running" in data["message"]:
                        self.log_test("Health Check", True, f"API is running: {data['message']}")
                        return True
                    else:
                        self.log_test("Health Check", False, "", "Unexpected response format")
                        return False
                else:
                    self.log_test("Health Check", False, "", f"HTTP {response.status}")
                    return False
        except Exception as e:
            self.log_test("Health Check", False, "", str(e))
            return False
    
    async def test_init_data(self):
        """Test data initialization endpoint"""
        try:
            async with self.session.post(f"{API_BASE_URL}/init-data") as response:
                if response.status == 200:
                    data = await response.json()
                    if "message" in data:
                        self.log_test("Data Initialization", True, f"Response: {data['message']}")
                        return True
                    else:
                        self.log_test("Data Initialization", False, "", "Unexpected response format")
                        return False
                else:
                    self.log_test("Data Initialization", False, "", f"HTTP {response.status}")
                    return False
        except Exception as e:
            self.log_test("Data Initialization", False, "", str(e))
            return False
    
    async def test_get_mesociclos(self):
        """Test getting all mesociclos"""
        try:
            async with self.session.get(f"{API_BASE_URL}/mesociclos") as response:
                if response.status == 200:
                    data = await response.json()
                    if isinstance(data, list) and len(data) == 5:
                        # Validate mesociclo structure
                        required_fields = ['id', 'nombre', 'mes', 'descripcion', 'color', 'objetivo', 'semanas']
                        first_mesociclo = data[0]
                        
                        missing_fields = [field for field in required_fields if field not in first_mesociclo]
                        if not missing_fields:
                            self.log_test("Get All Mesociclos", True, f"Retrieved {len(data)} mesociclos with correct structure")
                            return data
                        else:
                            self.log_test("Get All Mesociclos", False, "", f"Missing fields: {missing_fields}")
                            return None
                    else:
                        self.log_test("Get All Mesociclos", False, "", f"Expected 5 mesociclos, got {len(data) if isinstance(data, list) else 'non-list'}")
                        return None
                else:
                    self.log_test("Get All Mesociclos", False, "", f"HTTP {response.status}")
                    return None
        except Exception as e:
            self.log_test("Get All Mesociclos", False, "", str(e))
            return None
    
    async def test_get_mesociclo_by_id(self, mesociclo_id: int = 1):
        """Test getting specific mesociclo"""
        try:
            async with self.session.get(f"{API_BASE_URL}/mesociclos/{mesociclo_id}") as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get('id') == mesociclo_id:
                        self.log_test(f"Get Mesociclo {mesociclo_id}", True, f"Retrieved mesociclo: {data.get('nombre')}")
                        return data
                    else:
                        self.log_test(f"Get Mesociclo {mesociclo_id}", False, "", f"ID mismatch: expected {mesociclo_id}, got {data.get('id')}")
                        return None
                elif response.status == 404:
                    self.log_test(f"Get Mesociclo {mesociclo_id}", False, "", "Mesociclo not found")
                    return None
                else:
                    self.log_test(f"Get Mesociclo {mesociclo_id}", False, "", f"HTTP {response.status}")
                    return None
        except Exception as e:
            self.log_test(f"Get Mesociclo {mesociclo_id}", False, "", str(e))
            return None
    
    async def test_get_mesociclo_detalle(self, mesociclo_id: int = 1):
        """Test getting mesociclo with full details"""
        try:
            async with self.session.get(f"{API_BASE_URL}/mesociclos/{mesociclo_id}/detalle") as response:
                if response.status == 200:
                    data = await response.json()
                    required_fields = ['mesociclo', 'objetivos', 'sesiones_semanales']
                    missing_fields = [field for field in required_fields if field not in data]
                    
                    if not missing_fields:
                        mesociclo = data['mesociclo']
                        objetivos = data['objetivos']
                        sesiones = data['sesiones_semanales']
                        
                        self.log_test(f"Get Mesociclo {mesociclo_id} Details", True, 
                                    f"Retrieved details for {mesociclo.get('nombre')}, {len(objetivos)} objectives, {len(sesiones)} weekly sessions")
                        return data
                    else:
                        self.log_test(f"Get Mesociclo {mesociclo_id} Details", False, "", f"Missing fields: {missing_fields}")
                        return None
                elif response.status == 404:
                    self.log_test(f"Get Mesociclo {mesociclo_id} Details", False, "", "Mesociclo not found")
                    return None
                else:
                    self.log_test(f"Get Mesociclo {mesociclo_id} Details", False, "", f"HTTP {response.status}")
                    return None
        except Exception as e:
            self.log_test(f"Get Mesociclo {mesociclo_id} Details", False, "", str(e))
            return None
    
    async def test_get_sesiones_mesociclo(self, mesociclo_id: int = 1):
        """Test getting sessions for a mesociclo"""
        try:
            async with self.session.get(f"{API_BASE_URL}/mesociclos/{mesociclo_id}/sesiones") as response:
                if response.status == 200:
                    data = await response.json()
                    if isinstance(data, list):
                        if len(data) > 0:
                            # Validate session structure
                            first_session = data[0]
                            required_fields = ['id', 'mesociclo_id', 'semana', 'sesiones']
                            missing_fields = [field for field in required_fields if field not in first_session]
                            
                            if not missing_fields:
                                # Check if sesiones array has proper structure
                                if 'sesiones' in first_session and isinstance(first_session['sesiones'], list):
                                    if len(first_session['sesiones']) > 0:
                                        sesion = first_session['sesiones'][0]
                                        sesion_fields = ['id', 'tipo', 'nombre', 'dia', 'duracion', 'ejercicios']
                                        missing_sesion_fields = [field for field in sesion_fields if field not in sesion]
                                        
                                        if not missing_sesion_fields:
                                            self.log_test(f"Get Sessions for Mesociclo {mesociclo_id}", True, 
                                                        f"Retrieved {len(data)} weekly sessions with proper structure")
                                            return data
                                        else:
                                            self.log_test(f"Get Sessions for Mesociclo {mesociclo_id}", False, "", 
                                                        f"Missing session fields: {missing_sesion_fields}")
                                            return None
                                    else:
                                        self.log_test(f"Get Sessions for Mesociclo {mesociclo_id}", False, "", "Empty sessions array")
                                        return None
                                else:
                                    self.log_test(f"Get Sessions for Mesociclo {mesociclo_id}", False, "", "Invalid sessions structure")
                                    return None
                            else:
                                self.log_test(f"Get Sessions for Mesociclo {mesociclo_id}", False, "", f"Missing fields: {missing_fields}")
                                return None
                        else:
                            self.log_test(f"Get Sessions for Mesociclo {mesociclo_id}", True, "No sessions found (empty array)")
                            return data
                    else:
                        self.log_test(f"Get Sessions for Mesociclo {mesociclo_id}", False, "", "Response is not an array")
                        return None
                else:
                    self.log_test(f"Get Sessions for Mesociclo {mesociclo_id}", False, "", f"HTTP {response.status}")
                    return None
        except Exception as e:
            self.log_test(f"Get Sessions for Mesociclo {mesociclo_id}", False, "", str(e))
            return None
    
    async def test_get_planificacion(self):
        """Test getting complete planificacion"""
        try:
            async with self.session.get(f"{API_BASE_URL}/planificacion") as response:
                if response.status == 200:
                    data = await response.json()
                    required_fields = ['id', 'titulo', 'descripcion', 'categoria', 'duracion_meses', 
                                     'sesiones_por_semana', 'duracion_sesion', 'mesociclos', 'material_basico']
                    missing_fields = [field for field in required_fields if field not in data]
                    
                    if not missing_fields:
                        # Validate expected values
                        if (data.get('duracion_meses') == 5 and 
                            data.get('sesiones_por_semana') == 3 and 
                            data.get('duracion_sesion') == 90 and
                            len(data.get('mesociclos', [])) == 5):
                            
                            self.log_test("Get Complete Planificacion", True, 
                                        f"Retrieved planificacion: {data.get('titulo')}, {len(data.get('mesociclos', []))} mesociclos")
                            return data
                        else:
                            self.log_test("Get Complete Planificacion", False, "", 
                                        f"Invalid values: months={data.get('duracion_meses')}, sessions/week={data.get('sesiones_por_semana')}, duration={data.get('duracion_sesion')}, mesociclos={len(data.get('mesociclos', []))}")
                            return None
                    else:
                        self.log_test("Get Complete Planificacion", False, "", f"Missing fields: {missing_fields}")
                        return None
                elif response.status == 404:
                    self.log_test("Get Complete Planificacion", False, "", "Planificacion not found")
                    return None
                else:
                    self.log_test("Get Complete Planificacion", False, "", f"HTTP {response.status}")
                    return None
        except Exception as e:
            self.log_test("Get Complete Planificacion", False, "", str(e))
            return None
    
    async def test_get_material_basico(self):
        """Test getting basic material list"""
        try:
            async with self.session.get(f"{API_BASE_URL}/material-basico") as response:
                if response.status == 200:
                    data = await response.json()
                    if "material" in data and isinstance(data["material"], list):
                        material_list = data["material"]
                        if len(material_list) >= 5:  # Should have at least 5 items
                            self.log_test("Get Material Basico", True, f"Retrieved {len(material_list)} material items")
                            return data
                        else:
                            self.log_test("Get Material Basico", False, "", f"Too few material items: {len(material_list)}")
                            return None
                    else:
                        self.log_test("Get Material Basico", False, "", "Invalid response structure")
                        return None
                else:
                    self.log_test("Get Material Basico", False, "", f"HTTP {response.status}")
                    return None
        except Exception as e:
            self.log_test("Get Material Basico", False, "", str(e))
            return None
    
    async def test_invalid_endpoints(self):
        """Test error handling for invalid endpoints"""
        test_cases = [
            ("/mesociclos/999", "Non-existent mesociclo"),
            ("/mesociclos/abc", "Invalid mesociclo ID format"),
            ("/mesociclos/999/detalle", "Non-existent mesociclo details"),
        ]
        
        for endpoint, description in test_cases:
            try:
                async with self.session.get(f"{API_BASE_URL}{endpoint}") as response:
                    if response.status in [404, 422]:  # Expected error codes
                        self.log_test(f"Error Handling - {description}", True, f"Correctly returned HTTP {response.status}")
                    else:
                        self.log_test(f"Error Handling - {description}", False, "", f"Unexpected status: {response.status}")
            except Exception as e:
                self.log_test(f"Error Handling - {description}", False, "", str(e))
    
    async def test_data_integrity(self):
        """Test data relationships and integrity"""
        try:
            # Get all mesociclos
            mesociclos = await self.test_get_mesociclos()
            if not mesociclos:
                self.log_test("Data Integrity - Mesociclos", False, "", "Could not retrieve mesociclos")
                return
            
            # Test each mesociclo has proper ID sequence
            expected_ids = list(range(1, 6))  # 1, 2, 3, 4, 5
            actual_ids = sorted([m['id'] for m in mesociclos])
            
            if actual_ids == expected_ids:
                self.log_test("Data Integrity - Mesociclo IDs", True, f"Correct ID sequence: {actual_ids}")
            else:
                self.log_test("Data Integrity - Mesociclo IDs", False, "", f"Expected {expected_ids}, got {actual_ids}")
            
            # Test mesociclo names are unique
            names = [m['nombre'] for m in mesociclos]
            if len(names) == len(set(names)):
                self.log_test("Data Integrity - Unique Names", True, "All mesociclo names are unique")
            else:
                self.log_test("Data Integrity - Unique Names", False, "", "Duplicate mesociclo names found")
            
            # Test each mesociclo has 4 weeks
            weeks_correct = all(m['semanas'] == 4 for m in mesociclos)
            if weeks_correct:
                self.log_test("Data Integrity - Weeks Count", True, "All mesociclos have 4 weeks")
            else:
                self.log_test("Data Integrity - Weeks Count", False, "", "Some mesociclos don't have 4 weeks")
                
        except Exception as e:
            self.log_test("Data Integrity", False, "", str(e))
    
    async def test_exercise_structure(self):
        """Test exercise data structure in sessions"""
        try:
            # Get sessions for first mesociclo
            sessions = await self.test_get_sesiones_mesociclo(1)
            if not sessions or len(sessions) == 0:
                self.log_test("Exercise Structure", False, "", "No sessions found to test exercises")
                return
            
            # Check first session's exercises
            first_week = sessions[0]
            if 'sesiones' in first_week and len(first_week['sesiones']) > 0:
                first_session = first_week['sesiones'][0]
                if 'ejercicios' in first_session and len(first_session['ejercicios']) > 0:
                    ejercicio = first_session['ejercicios'][0]
                    
                    # Validate exercise structure
                    required_fields = ['id', 'nombre', 'duracion', 'descripcion', 'material', 'objetivo']
                    missing_fields = [field for field in required_fields if field not in ejercicio]
                    
                    if not missing_fields:
                        # Check if durations add up correctly
                        total_duration = sum(e.get('duracion', 0) for e in first_session['ejercicios'])
                        session_duration = first_session.get('duracion', 0)
                        
                        if total_duration == session_duration:
                            self.log_test("Exercise Structure", True, 
                                        f"Exercises have correct structure and durations sum to {total_duration} minutes")
                        else:
                            self.log_test("Exercise Structure", False, "", 
                                        f"Duration mismatch: exercises sum to {total_duration}, session duration is {session_duration}")
                    else:
                        self.log_test("Exercise Structure", False, "", f"Missing exercise fields: {missing_fields}")
                else:
                    self.log_test("Exercise Structure", False, "", "No exercises found in session")
            else:
                self.log_test("Exercise Structure", False, "", "No sessions found in week")
                
        except Exception as e:
            self.log_test("Exercise Structure", False, "", str(e))
    
    async def run_all_tests(self):
        """Run all backend tests"""
        print(f"🏈 Starting Football Training API Tests")
        print(f"📍 Backend URL: {API_BASE_URL}")
        print("=" * 60)
        
        # Core API tests
        await self.test_health_check()
        await self.test_init_data()
        await self.test_get_mesociclos()
        await self.test_get_mesociclo_by_id(1)
        await self.test_get_mesociclo_by_id(2)
        await self.test_get_mesociclo_detalle(1)
        await self.test_get_sesiones_mesociclo(1)
        await self.test_get_planificacion()
        await self.test_get_material_basico()
        
        # Error handling tests
        await self.test_invalid_endpoints()
        
        # Data integrity tests
        await self.test_data_integrity()
        await self.test_exercise_structure()
        
        # Print summary
        print("\n" + "=" * 60)
        print("🏈 FOOTBALL TRAINING API TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {self.test_results['total_tests']}")
        print(f"✅ Passed: {self.test_results['passed_tests']}")
        print(f"❌ Failed: {self.test_results['failed_tests']}")
        
        if self.test_results['errors']:
            print(f"\n🚨 CRITICAL ERRORS:")
            for error in self.test_results['errors']:
                print(f"   • {error}")
        
        success_rate = (self.test_results['passed_tests'] / self.test_results['total_tests']) * 100
        print(f"\n📊 Success Rate: {success_rate:.1f}%")
        
        if success_rate >= 90:
            print("🎉 EXCELLENT: Backend is working very well!")
        elif success_rate >= 75:
            print("✅ GOOD: Backend is mostly working with minor issues")
        elif success_rate >= 50:
            print("⚠️  MODERATE: Backend has some significant issues")
        else:
            print("🚨 CRITICAL: Backend has major issues that need immediate attention")
        
        return self.test_results

async def main():
    """Main test runner"""
    async with FootballAPITester() as tester:
        results = await tester.run_all_tests()
        
        # Return appropriate exit code
        if results['failed_tests'] == 0:
            return 0
        else:
            return 1

if __name__ == "__main__":
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n🛑 Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Test runner failed: {e}")
        sys.exit(1)