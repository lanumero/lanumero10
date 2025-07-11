#!/usr/bin/env python3
"""
Quick database inspection to check session data
"""

import asyncio
import aiohttp
import json

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
API_BASE_URL = f"{BACKEND_URL}/api"

async def check_database():
    async with aiohttp.ClientSession() as session:
        print("🔍 Checking database state...")
        
        # First, reinitialize data
        print("\n1. Reinitializing data...")
        async with session.post(f"{API_BASE_URL}/init-data") as response:
            if response.status == 200:
                data = await response.json()
                print(f"✅ Data init: {data.get('message')}")
            else:
                print(f"❌ Data init failed: {response.status}")
        
        # Check mesociclos
        print("\n2. Checking mesociclos...")
        async with session.get(f"{API_BASE_URL}/mesociclos") as response:
            if response.status == 200:
                mesociclos = await response.json()
                print(f"✅ Found {len(mesociclos)} mesociclos")
                for m in mesociclos:
                    print(f"   - ID {m['id']}: {m['nombre']}")
            else:
                print(f"❌ Mesociclos failed: {response.status}")
        
        # Check sessions for each mesociclo
        print("\n3. Checking sessions...")
        for mesociclo_id in range(1, 6):
            async with session.get(f"{API_BASE_URL}/mesociclos/{mesociclo_id}/sesiones") as response:
                if response.status == 200:
                    sessions = await response.json()
                    print(f"   Mesociclo {mesociclo_id}: {len(sessions)} sessions")
                    if len(sessions) > 0:
                        first_session = sessions[0]
                        print(f"      First session: week {first_session.get('semana')}, {len(first_session.get('sesiones', []))} training sessions")
                else:
                    print(f"   Mesociclo {mesociclo_id}: Error {response.status}")

if __name__ == "__main__":
    asyncio.run(check_database())