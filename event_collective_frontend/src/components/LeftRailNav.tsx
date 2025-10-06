import { Link } from "react-router-dom";

export default function LeftRailNav({ items }:{items:{label:string;href:string}[]}) {
  return (
    <aside className="fixed left-0 top-0 h-screen w-20 md:w-28 flex flex-col items-center justify-between py-6">
      <button aria-label="Menu" className="mt-2">
        <div className="w-7 h-0.5 mb-1 bg-current" />
        <div className="w-7 h-0.5 mb-1 bg-current" />
        <div className="w-7 h-0.5 bg-current" />
      </button>

      <nav className="flex-1 flex flex-col items-center justify-center gap-8">
        {items.map(i => (
          <Link key={i.href} to={i.href} className="-rotate-90 tracking-wide text-sm opacity-80 hover:opacity-100">
            {i.label}
          </Link>
        ))}
      </nav>

      <div className="mb-4 text-xs opacity-60">EC</div>
    </aside>
  );
}
