type Img = { id:number; url:string; alt_text?:string|null };

export default function GalleryMarquee({ images }:{images:Img[]}) {
  // simple CSS marquee effect using duplicate row
  const row = images.slice(0, 18);
  return (
    <section className="pl-24 pr-0 md:pl-32 overflow-hidden py-8">
      <div className="whitespace-nowrap animate-[marquee_28s_linear_infinite]">
        {row.concat(row).map(img => (
          <img key={`${img.id}-${Math.random()}`} src={img.url} alt={img.alt_text||""}
               className="inline-block h-36 w-auto object-cover rounded-lg mx-2" />
        ))}
      </div>
      {/* marquee keyframes */}
      <style>{`
        @keyframes marquee { from { transform: translateX(0) } to { transform: translateX(-50%) } }
      `}</style>
    </section>
  );
}
