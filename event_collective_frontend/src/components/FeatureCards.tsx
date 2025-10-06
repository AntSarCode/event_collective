type Service = { id:number; name:string; description?:string|null };

export default function FeatureCards({ services }:{ services:Service[] }) {
  const cols = services.slice(0,3);
  return (
    <section className="pl-24 pr-6 md:pl-32 py-8">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {cols.map(s => (
          <article key={s.id} className="border rounded-xl p-6">
            <h3 className="text-lg font-medium mb-2">{s.name}</h3>
            <p className="opacity-80 text-sm">{s.description || "—"}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
