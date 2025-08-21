import { useEffect, useState } from "react";
import { api } from "../services/api";

type GalleryItem = { id: number; image_url?: string; title?: string };

export default function Gallery() {
  const [items, setItems] = useState<GalleryItem[] | null>(null);

  useEffect(() => {
    (async () => {
      try {
        const { data } = await api.get<GalleryItem[]>("/gallery", { params: { limit: 12 } });
        setItems(data);
      } catch {
        // simple placeholders if endpoint not live yet
        setItems(Array.from({ length: 12 }).map((_, i) => ({ id: i + 1 })));
      }
    })();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Gallery</h1>
      {!items && <div>Loading…</div>}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        {items?.map(g => (
          <div key={g.id} className="aspect-square bg-gray-100 rounded-xl overflow-hidden">
            {g.image_url ? (
              <img src={g.image_url} alt={g.title || "Image"} className="w-full h-full object-cover" />
            ) : (
              <div className="w-full h-full grid place-items-center text-gray-400">Image</div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
