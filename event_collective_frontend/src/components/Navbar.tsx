import { useState } from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <header className="fixed top-0 left-0 w-full h-16 bg-[#faf9f7] border-b border-gray-300 flex items-center justify-between px-6 md:px-12 z-50">
      <h1 className="text-lg font-serif tracking-wide">THE EVENT COLLECTIVE</h1>

      {/* Desktop Navigation */}
      <nav className="hidden md:flex items-center gap-6">
        <Link to="/" className="hover:text-[var(--ec-accent)] transition-colors">Home</Link>
        <Link to="/services" className="hover:text-[var(--ec-accent)] transition-colors">Services</Link>
        <Link to="/gallery" className="hover:text-[var(--ec-accent)] transition-colors">Gallery</Link>
        <Link to="/reviews" className="hover:text-[var(--ec-accent)] transition-colors">Reviews</Link>
        <Link to="/contact" className="hover:text-[var(--ec-accent)] transition-colors">Contact</Link>
        <a href="/contact" className="ml-4 border border-current px-4 py-2 rounded-full hover:bg-[var(--ec-accent)] hover:text-white transition-colors">Inquire</a>
        <Link to="/login" className="hover:text-[var(--ec-accent)] transition-colors">Login</Link>
        <Link to="/register" className="hover:text-[var(--ec-accent)] transition-colors">Sign Up</Link>
      </nav>

      {/* Mobile Menu Toggle */}
      <button onClick={() => setMenuOpen(!menuOpen)} className="md:hidden flex flex-col justify-center items-center focus:outline-none">
        <div className="w-6 h-0.5 bg-current mb-1" />
        <div className="w-6 h-0.5 bg-current mb-1" />
        <div className="w-6 h-0.5 bg-current" />
      </button>

      {/* Mobile Menu */}
      {menuOpen && (
        <div className="absolute top-16 left-0 w-full bg-[#faf9f7] border-t border-gray-300 flex flex-col items-center py-4 md:hidden animate-fadeIn">
          <Link to="/" className="py-2" onClick={() => setMenuOpen(false)}>Home</Link>
          <Link to="/services" className="py-2" onClick={() => setMenuOpen(false)}>Services</Link>
          <Link to="/gallery" className="py-2" onClick={() => setMenuOpen(false)}>Gallery</Link>
          <Link to="/reviews" className="py-2" onClick={() => setMenuOpen(false)}>Reviews</Link>
          <Link to="/contact" className="py-2" onClick={() => setMenuOpen(false)}>Contact</Link>
          <a href="/contact" className="py-2 border border-current px-4 mt-2 rounded-full hover:bg-[var(--ec-accent)] hover:text-white transition-colors" onClick={() => setMenuOpen(false)}>Inquire</a>
          <Link to="/login" className="py-2" onClick={() => setMenuOpen(false)}>Login</Link>
          <Link to="/register" className="py-2" onClick={() => setMenuOpen(false)}>Sign Up</Link>
        </div>
      )}
    </header>
  );
}