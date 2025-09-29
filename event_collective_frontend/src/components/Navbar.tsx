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

  const pill: React.CSSProperties = {
    padding: "8px 14px",
    borderRadius: 999,
    border: "1px solid var(--ec-line)",
    textDecoration: "none",
    color: "var(--ec-text)",
    letterSpacing: ".08em",
    display: "inline-block",
  };

  return (
    <nav className={`ec-nav ${scrolled ? "scrolled" : ""}`}>
      <div className="container ec-nav-inner">
        {/* Brand */}
        <Link to="/" aria-label="The Event Collective" style={{ textDecoration: "none", color: "inherit" }}>
          <strong style={{ letterSpacing: ".08em" }}>THE EVENT COLLECTIVE</strong>
        </Link>

        {/* Primary nav as uniform pill buttons */}
        <div style={{ display: "flex", gap: 10, alignItems: "center" }}>
          <NavLink to="/" end style={pill}>HOME</NavLink>
          <NavLink to="/services" style={pill}>SERVICES</NavLink>
          <NavLink to="/gallery" style={pill}>GALLERY</NavLink>
          <NavLink to="/reviews" style={pill}>REVIEWS</NavLink>
          <NavLink to="/contact" style={pill}>CONTACT</NavLink>

          {/* Inquire emphasized */}
          <a
            className="cta-btn"
            href="/contact"
            aria-label="Inquire"
            style={{ padding: "10px 16px", borderRadius: 999 }}
          >
            INQUIRE
          </a>

          {/* Auth controls */}
          {user ? (
            <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
              <span className="muted" style={{ fontSize: 13 }}>Hi, {user.name || user.email}</span>
              <button
                onClick={() => { logout(); location.href = "/"; }}
                style={{ background: "transparent", border: 0, cursor: "pointer", textDecoration: "underline", fontSize: 13 }}
                aria-label="Logout"
              >Logout</button>
              {user.role === "admin" && (
                <NavLink to="/admin" style={{ ...pill, padding: "6px 10px", fontSize: 13 }}>ADMIN</NavLink>
              )}
              <NavLink to="/dashboard" style={{ ...pill, padding: "6px 10px", fontSize: 13 }}>DASHBOARD</NavLink>
            </div>
          ) : (
            <div style={{ display: "flex", gap: 8 }}>
              <NavLink to="/login" style={{ ...pill, padding: "6px 10px", fontSize: 13 }}>LOGIN</NavLink>
              <NavLink to="/register" style={{ ...pill, padding: "6px 10px", fontSize: 13 }}>SIGN&nbsp;UP</NavLink>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}
