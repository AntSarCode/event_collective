import { createBrowserRouter } from "react-router-dom";
import AppLayout from "../components/AppLayout.tsx";
import Home from "../pages/Home.tsx";
import Gallery from "../pages/Gallery.tsx";
import Services from "../pages/Services.tsx";
import Reviews from "../pages/Reviews.tsx";
import Contact from "../pages/Contact.tsx";
import Dashboard from "../pages/Dashboard.tsx";
import Admin from "../pages/Admin.tsx";
import Login from "../pages/Login.tsx";
import Register from "../pages/Register.tsx";
import NotFound from "../pages/NotFound.tsx";
import ProtectedRoute from "../components/ProtectedRoute.tsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
    children: [
      { index: true, element: <Home /> },
      { path: "gallery", element: <Gallery /> },
      { path: "services", element: <Services /> },
      { path: "reviews", element: <Reviews /> },
      { path: "contact", element: <Contact /> },
      { path: "login", element: <Login /> },
      { path: "register", element: <Register /> },
      {
        path: "dashboard",
        element: (
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        ),
      },
      {
        path: "admin",
        element: (
          <ProtectedRoute requireAdmin>
            <Admin />
          </ProtectedRoute>
        ),
      },
      { path: "*", element: <NotFound /> },
    ],
  },
]);

export default router;
