import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export const api = axios.create({
  baseURL: API_BASE,
  withCredentials: false,
  headers: {
    "Content-Type": "application/json",
  },
});

// Inject JWT if present
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("ec_token");
  if (token) {
    config.headers = config.headers || {};
    (config.headers as any).Authorization = `Bearer ${token}`;
  }
  return config;
});
