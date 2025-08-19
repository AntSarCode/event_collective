import { useForm } from "react-hook-form";
import { register as registerUser } from "../services/auth.ts";
import type { RegisterRequest } from "../types";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const { register, handleSubmit } = useForm<RegisterRequest>();
  const navigate = useNavigate();

  const onSubmit = handleSubmit(async (data) => {
    await registerUser(data);
    navigate("/login");
  });

  return (
    <div className="max-w-sm mx-auto">
      <h1 className="text-2xl font-bold mb-4">Create Account</h1>
      <form onSubmit={onSubmit} className="space-y-3">
        <input className="w-full border rounded-md p-2" placeholder="Name" {...register("name")} />
        <input className="w-full border rounded-md p-2" placeholder="Email" {...register("email", { required: true })} />
        <input className="w-full border rounded-md p-2" type="password" placeholder="Password" {...register("password", { required: true })} />
        <button className="w-full rounded-md bg-black text-white py-2">Sign Up</button>
      </form>
    </div>
  );
}
