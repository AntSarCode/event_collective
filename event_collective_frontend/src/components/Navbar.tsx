import { Link, NavLink } from "react-router-dom";

export default function Navbar() {
  const linkClass = ({ isActive }: { isActive: boolean }) =>
    `px-3 py-2 rounded-md text-sm font-medium ${isActive ? "text-black" : "text-gray-600 hover:text-black"}`;

  return (
    <header className="border-b">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <Link to="/" className="font-semibold text-xl">Event Collective</Link>
        <nav className="flex gap-2">
          <NavLink to="/" className={linkClass} end>Home</NavLink>
          <NavLink to="/gallery" className={linkClass}>Gallery</NavLink>
          <NavLink to="/services" className={linkClass}>Services</NavLink>
          <NavLink to="/reviews" className={linkClass}>Reviews</NavLink>
          <NavLink to="/contact" className={linkClass}>Contact</NavLink>
          <NavLink to="/dashboard" className={linkClass}>Dashboard</NavLink>
          <NavLink to="/admin" className={linkClass}>Admin</NavLink>
        </nav>
      </div>
    </header>
  );
}
