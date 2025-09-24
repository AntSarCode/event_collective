import { useEffect, useState, type ReactNode } from "react";
import { Navigate } from "react-router-dom";
import { getMe } from "../services/auth";

type ProtectedRouteProps = {
  children: ReactNode;
  requireAdmin?: boolean;
};

export default function ProtectedRoute({
  children,
  requireAdmin = false,
}: ProtectedRouteProps) {
  const [allowed, setAllowed] = useState<boolean | null>(null);

  useEffect(() => {
    (async () => {
      try {
        // your existing getMe() logic
        const me = await getMe();
        if (requireAdmin) {
          setAllowed(me.role === "admin");
        } else {
          setAllowed(true);
        }
      } catch {
        setAllowed(false);
      }
    })();
  }, [requireAdmin]);

  if (allowed === null) return <div>Loading...</div>;
  if (!allowed) return <Navigate to="/login" replace />;
  return <>{children}</>;
}
