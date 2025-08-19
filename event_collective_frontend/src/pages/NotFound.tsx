import { Link } from "react-router-dom";

export default function NotFound() {
  return (
    <div className="text-center space-y-4">
      <h1 className="text-3xl font-bold">404</h1>
      <p>Page not found.</p>
      <Link className="underline" to="/">Go home</Link>
    </div>
  );
}
