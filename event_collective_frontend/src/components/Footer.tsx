export default function Footer() {
  return (
    <footer id="contact" role="contentinfo">
      <div className="container foot-grid">
        <div>
          <div style={{ fontFamily: '"Playfair Display",serif', fontSize: 24, marginBottom: 8 }}>
            The Event Collective
          </div>
          <p className="muted">
            Boutique planning & design for weddings, corporate events, and private celebrations.
          </p>
          <div style={{ height: 1, background: "var(--ec-line)", margin: "18px 0" }} />
          <small className="muted">© {new Date().getFullYear()} The Event Collective. All rights reserved.</small>
        </div>

        <div>
          <div className="foot-title">Inquire</div>
          <p className="muted">
            hello@eventcollective.co<br />
            (555) 123-4567
          </p>
        </div>

        <div>
          <div className="foot-title">Follow</div>
          <p className="muted">Instagram · Pinterest · LinkedIn</p>
        </div>
      </div>
    </footer>
  );
}
