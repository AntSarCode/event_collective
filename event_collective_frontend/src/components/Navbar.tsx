import { Link, NavLink } from "react-router-dom";
import { useEffect, useState } from "react";
import { getMe, logout, isAuthed } from "../services/auth";
import type { User } from "../types";

export default function Navbar() {
  const [user, setUser] = useState<User | null>(null);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    (async () => {
      if (isAuthed()) {
        try { setUser(await getMe()); } catch { setUser(null); }
      }
    })();
  }, []);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 10);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const linkStyle: React.CSSProperties = { letterSpacing: ".08em" };

  return (
    <nav className={`ec-nav ${scrolled ? "scrolled" : ""}`}>
      <div className="container ec-nav-inner">
        {/* Brand */}
        <Link to="/" aria-label="The Event Collective" style={{ textDecoration: "none", color: "inherit" }}>
          <strong style={{ letterSpacing: ".08em" }}>THE EVENT COLLECTIVE</strong>
        </Link>

        {/* Primary nav */}
        <div style={{ display: "flex", gap: 28, alignItems: "center" }}>
          <NavLink to="/" end style={linkStyle}>HOME</NavLink>
          <NavLink to="/services" style={linkStyle}>SERVICES</NavLink>
          <NavLink to="/gallery" style={linkStyle}>GALLERY</NavLink>
          <NavLink to="/reviews" style={linkStyle}>REVIEWS</NavLink>
          <NavLink to="/contact" style={linkStyle}>CONTACT</NavLink>

          {/* Inquire CTA echoes brand button styling */}
          <a className="cta-btn" href="/contact" aria-label="Inquire">INQUIRE</a>

          {/* Auth controls (kept minimal and on-brand) */}
          {user ? (
            <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
              <span className="muted" style={{ fontSize: 13 }}>Hi, {user.name || user.email}</span>
              <button
                onClick={() => { logout(); location.href = "/"; }}
                style={{ background: "transparent", border: 0, cursor: "pointer", textDecoration: "underline", fontSize: 13 }}
                aria-label="Logout"
              >Logout</button>
              {user.role === "admin" && (
                <NavLink to="/admin" style={{ ...linkStyle, fontSize: 13 }}>ADMIN</NavLink>
              )}
              <NavLink to="/dashboard" style={{ ...linkStyle, fontSize: 13 }}>DASHBOARD</NavLink>
            </div>
          ) : (
            <div style={{ display: "flex", gap: 12 }}>
              <NavLink to="/login" style={{ ...linkStyle, fontSize: 13 }}>LOGIN</NavLink>
              <NavLink to="/register" style={{ ...linkStyle, fontSize: 13 }}>SIGN&nbsp;UP</NavLink>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}
