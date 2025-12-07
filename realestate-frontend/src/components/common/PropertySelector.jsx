import { ChevronDown, Building } from "lucide-react";

const properties = [
  { id: "A", name: "Building A – Mumbai" },
  { id: "B", name: "Building B – Bangalore" },
  { id: "C", name: "Building C – New York" },
];

export default function PropertySelector({ value, onChange }) {
  return (
    <div className="relative group">
      <div className="absolute top-1/2 -translate-y-1/2 pointer-events-none pl-5">
        <Building size={14} className="text-slate-400 group-hover:text-indigo-500 transition-colors" />
      </div>
      
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="
          appearance-none
          bg-slate-50
          hover:bg-white
          border border-transparent
          hover:border-indigo-100
          hover:ring-2 hover:ring-indigo-50/50
          rounded-xl
          pl-9
          pr-10
          py-2.5
          text-sm font-semibold
          text-slate-700
          transition-all
          duration-200
          cursor-pointer
          focus:outline-none
          focus:ring-2
          focus:ring-indigo-500
          focus:bg-white
          shadow-sm
        "
      >
        {properties.map((p) => (
          <option key={p.id} value={p.id}>
            {p.name}
          </option>
        ))}
      </select>

      <div className="pointer-events-none absolute inset-y-0 right-3 flex items-center text-slate-400">
        <ChevronDown size={14} />
      </div>
    </div>
  );
}
