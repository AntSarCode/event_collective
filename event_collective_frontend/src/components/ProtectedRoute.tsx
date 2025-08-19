import { Navigate } from "react-router-dom";
import { isAuthed, getMe } from "../services/auth.ts";
import { useEffect, useState } from "react";

export default function ProtectedRoute({ children, requireAdmin = false }: { children: JSX.Element, requireAdmin?: boolean }) {
  const [allowed, setAllowed] = useState<boolean | null>(null);

  useEffect(() => {
    async function check() {
      if (!isAuthed()) {
        setAllowed(false);
        return;
      }
      try {
        const me = await getMe();
        if (requireAdmin) {
          setAllowed(me.role === "admin");
        } else {
          setAllowed(true);
        }
      } catch {
        setAllowed(false);
      }
    }
    check();
  }, [requireAdmin]);

  if (allowed === null) return <div>Loading...</div>;
  if (!allowed) return <Navigate to="/login" replace />;
  return children;
}
