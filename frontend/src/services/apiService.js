import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
apiClient.interceptors.request.use(
  (config) => {
    console.log(`Making API request to: ${config.url}`);
    return config;
  },
  (error) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor
apiClient.interceptors.response.use(
  (response) => {
    console.log(`API response from ${response.config.url}:`, response.status);
    return response;
  },
  (error) => {
    console.error('Response error:', error);
    return Promise.reject(error);
  }
);

export const footballAPI = {
  // Get all mesociclos
  getMesociclos: async () => {
    try {
      const response = await apiClient.get('/mesociclos');
      return response.data;
    } catch (error) {
      console.error('Error fetching mesociclos:', error);
      throw error;
    }
  },

  // Get specific mesociclo
  getMesociclo: async (id) => {
    try {
      const response = await apiClient.get(`/mesociclos/${id}`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching mesociclo ${id}:`, error);
      throw error;
    }
  },

  // Get mesociclo with full details
  getMesocicloDetalle: async (id) => {
    try {
      const response = await apiClient.get(`/mesociclos/${id}/detalle`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching mesociclo detalle ${id}:`, error);
      throw error;
    }
  },

  // Get sesiones for a mesociclo
  getSesionesMesociclo: async (mesocicloId) => {
    try {
      const response = await apiClient.get(`/mesociclos/${mesocicloId}/sesiones`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching sesiones for mesociclo ${mesocicloId}:`, error);
      throw error;
    }
  },

  // Get complete planificacion
  getPlanificacion: async () => {
    try {
      const response = await apiClient.get('/planificacion');
      return response.data;
    } catch (error) {
      console.error('Error fetching planificacion:', error);
      throw error;
    }
  },

  // Get material básico
  getMaterialBasico: async () => {
    try {
      const response = await apiClient.get('/material-basico');
      return response.data.material;
    } catch (error) {
      console.error('Error fetching material básico:', error);
      throw error;
    }
  },

  // Initialize data (for setup)
  initData: async () => {
    try {
      const response = await apiClient.post('/init-data');
      return response.data;
    } catch (error) {
      console.error('Error initializing data:', error);
      throw error;
    }
  }
};

export default footballAPI;