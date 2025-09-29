import logoUrl from "../assets/event-collective-logo.png";
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <>
      {/* Hero with logo */}
      <header className="hero">
        <div className="container" style={{ textAlign: "center" }}>
          <img
            src={logoUrl}
            alt="The Event Collective logo"
            style={{ width: 260, maxWidth: "80%", height: "auto", opacity: 0.98 }}
          />
          <h1 className="hero-title">Curating Timeless Experiences</h1>
          <div className="hero-script">Weddings • Corporate • Private</div>
          <p className="hero-sub" style={{ margin: "18px auto 0" }}>
            Boutique planning and design with a refined, modern sensibility. We orchestrate memorable
            gatherings with meticulous detail and calm execution.
          </p>
          <a className="cta-btn" href="/contact">Inquire Now</a>
        </div>
      </header>

      {/* Quick links */}
      <section aria-labelledby="quicklinks-title">
        <div className="container">
          <h2 id="quicklinks-title" style={{ fontFamily: '"Playfair Display",serif', fontSize: 24, marginBottom: 18 }}>
            Explore
          </h2>
          <div className="features">
            <Link to="/gallery" className="feature-card" style={{ textDecoration: "none", color: "inherit" }}>
              <div aria-hidden style={{ width: 44, height: 2, background: "var(--ec-accent)", marginBottom: 14 }} />
              <h3 className="feature-title">Gallery</h3>
              <p className="feature-desc">See highlights from past events.</p>
            </Link>
            <Link to="/services" className="feature-card" style={{ textDecoration: "none", color: "inherit" }}>
              <div aria-hidden style={{ width: 44, height: 2, background: "var(--ec-accent)", marginBottom: 14 }} />
              <h3 className="feature-title">Services</h3>
              <p className="feature-desc">Browse packages and pricing ranges.</p>
            </Link>
            <Link to="/reviews" className="feature-card" style={{ textDecoration: "none", color: "inherit" }}>
              <div aria-hidden style={{ width: 44, height: 2, background: "var(--ec-accent)", marginBottom: 14 }} />
              <h3 className="feature-title">Reviews</h3>
              <p className="feature-desc">Read testimonials from clients.</p>
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
