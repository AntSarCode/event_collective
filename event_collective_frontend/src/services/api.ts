import axios, { AxiosHeaders, type InternalAxiosRequestConfig } from "axios";

const API_BASE = import.meta.env.VITE_API_BASE || "https://event-collective.onrender.com/api";

export const api = axios.create({
  baseURL: API_BASE,
  withCredentials: false,
  headers: {
    "Content-Type": "application/json",
  },
});

// Inject JWT if present using AxiosHeaders (no 'any', no assignment type errors)
api.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  const token = localStorage.getItem("ec_token");
  if (!token) return config;

  const headers = AxiosHeaders.from(config.headers || {});
  headers.set("Authorization", `Bearer ${token}`);
  config.headers = headers;
  return config;
});
