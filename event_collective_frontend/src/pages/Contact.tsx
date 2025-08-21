import { useForm } from "react-hook-form";
import { api } from "../services/api";
type ContactForm = { name: string; email: string; message: string };

export default function Contact() {
  const { register, handleSubmit, reset } = useForm<ContactForm>();
  const onSubmit = handleSubmit(async (data) => {
    await api.post("/contact", data);
    alert("Thanks! We’ll be in touch.");
    reset();
  });

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Contact</h1>
      <form onSubmit={onSubmit} className="space-y-3 max-w-md">
        <input className="w-full border rounded-md p-2" placeholder="Name" {...register("name", { required: true })} />
        <input className="w-full border rounded-md p-2" placeholder="Email" {...register("email", { required: true })} />
        <textarea className="w-full border rounded-md p-2 h-32" placeholder="Message" {...register("message", { required: true })} />
        <button className="rounded-md bg-black text-white py-2 px-4">Send</button>
      </form>
    </div>
  );
}
