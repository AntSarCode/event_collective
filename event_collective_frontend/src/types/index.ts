export type Role = "user" | "admin";

export interface User {
  id: number;
  email: string;
  name?: string;
  role: Role;
  created_at?: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: "bearer";
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  email: string;
  password: string;
  name?: string;
}

export interface EventItem {
  id: number;
  title: string;
  date: string;
  location?: string;
  description?: string;
  status?: "planned" | "in_progress" | "completed";
}

export interface Review {
  id: number;
  user_id: number;
  rating: number; // 1-5
  comment?: string;
  created_at: string;
}

export interface ServiceItem {
  id: number;
  name: string;
  description?: string;
  price_min?: number;
  price_max?: number;
}

export interface MessageThread {
  id: number;
  user_id: number;
  subject: string;
  last_message_at: string;
}

export interface Message {
  id: number;
  thread_id: number;
  sender_id: number;
  body: string;
  created_at: string;
}
