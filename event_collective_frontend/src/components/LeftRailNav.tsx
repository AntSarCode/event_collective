import { Link } from "react-router-dom";

export default function LeftRailNav({ items }:{items:{label:string;href:string}[]}) {
  return (
    <aside className="fixed top-0 left-0 h-screen w-24 bg-[#faf9f7] border-r border-gray-300 flex flex-col items-center justify-center z-40">
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
