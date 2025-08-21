import { useEffect, useState } from "react";
import { api } from "../services/api";
import type { Review } from "../types";

export default function Reviews() {
  const [items, setItems] = useState<Review[] | null>(null);

  useEffect(() => {
    (async () => {
      try {
        const { data } = await api.get<Review[]>("/reviews", { params: { limit: 10 } });
        setItems(data);
      } catch {
        setItems([]);
      }
    })();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Reviews</h1>
      {!items && <div>Loading…</div>}
      {items?.length === 0 && <div>No reviews yet.</div>}
      <ul className="space-y-3">
        {items?.map(r => (
          <li key={r.id} className="p-4 border rounded-xl">
            <div className="font-medium">Rating: {"⭐".repeat(Math.max(1, Math.min(5, r.rating)))}</div>
            <div className="text-gray-700">{r.comment || "—"}</div>
            <div className="text-xs text-gray-500">{new Date(r.created_at).toLocaleString()}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}
