import { useForm } from "react-hook-form";
import { login } from "../services/auth.ts";
import type { LoginRequest } from "../types";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const { register, handleSubmit } = useForm<LoginRequest>();
  const navigate = useNavigate();

  const onSubmit = handleSubmit(async (data) => {
    await login(data);
    navigate("/dashboard");
  });

  return (
    <div className="max-w-sm mx-auto">
      <h1 className="text-2xl font-bold mb-4">Login</h1>
      <form onSubmit={onSubmit} className="space-y-3">
        <input className="w-full border rounded-md p-2" placeholder="Email" {...register("email", { required: true })} />
        <input className="w-full border rounded-md p-2" type="password" placeholder="Password" {...register("password", { required: true })} />
        <button className="w-full rounded-md bg-black text-white py-2">Sign In</button>
      </form>
    </div>
  );
}
