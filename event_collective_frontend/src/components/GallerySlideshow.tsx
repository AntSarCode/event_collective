import { useEffect, useState } from "react";

type Img = { id: number; url: string; alt_text?: string | null };

// Lightweight fade slideshow (no external deps). Keeps the same export name
// so you can replace the file without changing imports.
export default function GallerySlideshow({ images }: { images: Img[] }) {
  const slides = images.slice(0, 12);
  const [idx, setIdx] = useState(0);

  // Auto-advance every 3.5s
  useEffect(() => {
    if (slides.length <= 1) return;
    const t = setInterval(() => setIdx((i) => (i + 1) % slides.length), 3500);
    return () => clearInterval(t);
  }, [slides.length]);

  if (!slides.length) return null;

  return (
    <section className="relative pl-24 pr-6 md:pl-32 py-8">
      <div className="relative h-64 md:h-80 overflow-hidden rounded-2xl">
        {slides.map((img, i) => (
          <img
            key={img.id}
            src={img.url}
            alt={img.alt_text ?? ""}
            className={`absolute inset-0 w-full h-full object-cover transition-opacity duration-700 ${i === idx ? "opacity-100" : "opacity-0"}`}
          />
        ))}
      </div>

      {/* Dots */}
      <div className="mt-3 flex justify-center gap-2">
        {slides.map((_, i) => (
          <button
            key={i}
            aria-label={`Show slide ${i + 1}`}
            onClick={() => setIdx(i)}
            className={`h-2 w-2 rounded-full ${i === idx ? "bg-[var(--ec-fg)]" : "bg-gray-400/50"}`}
          />
        ))}
      </div>
    </section>
  );
}