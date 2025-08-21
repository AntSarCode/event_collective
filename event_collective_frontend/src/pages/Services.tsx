import { useEffect, useState } from "react";
import { api } from "../services/api";
import type { ServiceItem } from "../types";

export default function Services() {
  const [items, setItems] = useState<ServiceItem[] | null>(null);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    (async () => {
      try {
        const { data } = await api.get<ServiceItem[]>("/services");
        setItems(data);
      } catch (e: any) {
        setErr("Couldn’t load services. Showing placeholders.");
        setItems([
          { id: 1, name: "Wedding Coordination", description: "Day-of + vendor mgmt." },
          { id: 2, name: "Corporate Events", description: "Planning & production." },
          { id: 3, name: "Private Parties", description: "Birthdays, showers, more." },
        ]);
      }
    })();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Services</h1>
      {err && <div className="mb-3 text-amber-700">{err}</div>}
      {!items && <div>Loading…</div>}
      <div className="grid md:grid-cols-3 gap-4">
        {items?.map(s => (
          <div key={s.id} className="p-6 rounded-2xl border shadow-sm">
            <h3 className="font-semibold text-lg">{s.name}</h3>
            <p className="text-gray-600">{s.description}</p>
            {(s.price_min ?? s.price_max) != null && (
              <p className="mt-2 text-sm text-gray-500">
                {s.price_min ? `$${s.price_min}` : ""}–{s.price_max ? `$${s.price_max}` : ""}
              </p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

