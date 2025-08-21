import { Link, NavLink } from "react-router-dom";
import { useEffect, useState } from "react";
import { getMe, logout, isAuthed } from "../services/auth";
import type { User } from "../types";

export default function Navbar() {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    (async () => {
      if (isAuthed()) {
        try { setUser(await getMe()); } catch { setUser(null); }
      }
    })();
  }, []);

  const linkClass = ({ isActive }: { isActive: boolean }) =>
    `px-3 py-2 rounded-md text-sm font-medium ${isActive ? "text-black" : "text-gray-600 hover:text-black"}`;

  return (
    <header className="border-b">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <Link to="/" className="font-semibold text-xl">Event Collective</Link>
        <nav className="flex items-center gap-2">
          <NavLink to="/" className={linkClass} end>Home</NavLink>
          <NavLink to="/gallery" className={linkClass}>Gallery</NavLink>
          <NavLink to="/services" className={linkClass}>Services</NavLink>
          <NavLink to="/reviews" className={linkClass}>Reviews</NavLink>
          <NavLink to="/contact" className={linkClass}>Contact</NavLink>
          <NavLink to="/dashboard" className={linkClass}>Dashboard</NavLink>
          {user?.role === "admin" && <NavLink to="/admin" className={linkClass}>Admin</NavLink>}
          {user ? (
            <>
              <span className="text-sm text-gray-600 ml-2">Hi, {user.name || user.email}</span>
              <button
                className="ml-2 text-sm underline"
                onClick={() => { logout(); location.href = "/"; }}
              >Logout</button>
            </>
          ) : (
            <>
              <NavLink to="/login" className={linkClass}>Login</NavLink>
              <NavLink to="/register" className={linkClass}>Sign Up</NavLink>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
