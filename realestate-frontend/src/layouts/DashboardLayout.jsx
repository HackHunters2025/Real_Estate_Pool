import { useState } from "react";
import { LayoutDashboard, ArrowLeft } from "lucide-react";
import PropertySelector from "../components/common/PropertySelector";
import { useNavigate } from "react-router-dom";

export default function DashboardLayout({ title, children }) {
  const [property, setProperty] = useState("A");
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-slate-50/50 font-sans text-slate-900 selection:bg-indigo-100">
      <header className="sticky top-0 z-30 bg-white/80 backdrop-blur-md border-b border-slate-200 shadow-sm">
        <div className="max-w-[1400px]  px-6 py-4 flex items-center justify-between">
          {/* Left Section */}
          <div className="flex items-center gap-4">
            <button
              onClick={() => navigate("/")}
              className="p-3 rounded-xl hover:bg-slate-100 transition cursor-pointer"
              aria-label="Go back to home"
            >
              <ArrowLeft size={26} className="text-slate-800" />
            </button>

            <div className="bg-indigo-600 p-2 rounded-lg shadow-md shadow-indigo-200">
              <LayoutDashboard size={20} className="text-white" />
            </div>

            <div>
              <h1 className="text-xl font-bold text-slate-900 tracking-tight">
                {title}
              </h1>
              <p className="text-xs text-slate-500 font-medium">
                Real Estate Analytics Platform
              </p>
            </div>
          </div>

           <div className="mr-1.5">
          <PropertySelector value={property} onChange={setProperty} />
          </div>
        </div>
      </header>

      <main className="max-w-[1400px] mx-auto px-6 py-8">
        <div className="animate-in fade-in slide-in-from-bottom-4 duration-500">
          {children}
        </div>
      </main>
    </div>
  );
}
