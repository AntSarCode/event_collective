import { api } from "./api.ts";
import type { User, LoginRequest, RegisterRequest, TokenResponse } from "../types";

export async function login(data: LoginRequest): Promise<TokenResponse> {
  const res = await api.post<TokenResponse>("/auth/login", data);
  localStorage.setItem("ec_token", res.data.access_token);
  return res.data;
}

export async function logout() {
  localStorage.removeItem("ec_token");
}

export async function getMe(): Promise<User> {
  const res = await api.get<User>("/auth/me");
  return res.data;
}

export async function register(data: RegisterRequest): Promise<User> {
  const res = await api.post<User>("/auth/register", data);
  return res.data;
}

export function isAuthed(): boolean {
  return !!localStorage.getItem("ec_token");
}
