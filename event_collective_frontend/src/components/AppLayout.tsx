import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Footer from "./Footer";

export default function AppLayout() {
  return (
    <>
      <Navbar />
      <main>
        {/* Optional hero placeholder to create elegant white space on all pages */}
        <section style={{ padding: "48px 0 0" }} aria-hidden />
        <Outlet />
      </main>
      <Footer />
    </>
  );
}
