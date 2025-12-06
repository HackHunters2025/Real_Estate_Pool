// import { useEffect, useState } from "react";
// import { calculatePricingScenario } from "../../api/pricingAPI";

// export default function PricingSlider({ propertyId = "A" }) {
//   const [adjustment, setAdjustment] = useState(0);
//   const [data, setData] = useState(null);
//   const [loading, setLoading] = useState(false);

//   useEffect(() => {
//     setLoading(true);
//     calculatePricingScenario(propertyId, adjustment)
//       .then((res) => setData(res))
//       .finally(() => setLoading(false));
//   }, [propertyId, adjustment]);

//   return (
//     <div className="bg-white rounded-2xl ring-1 ring-slate-200 shadow-sm p-6 space-y-5">
//       <div>
//         <h2 className="text-sm font-semibold text-slate-900">
//           Dynamic Pricing Simulator
//         </h2>
//         <p className="text-xs text-slate-500">
//           Simulate rent impact using AI demand modeling
//         </p>
//       </div>

//       <input
//         type="range"
//         min="-10"
//         max="20"
//         value={adjustment}
//         onChange={(e) => setAdjustment(Number(e.target.value))}
//         className="w-full accent-indigo-600"
//       />

//       {loading || !data ? (
//         <p className="text-xs text-slate-500">
//           Pricing agent evaluating market signals…
//         </p>
//       ) : (
//         <>
//           <div className="grid grid-cols-2 gap-4">
//             <div className="rounded-lg bg-slate-50 p-4">
//               <p className="text-xs text-slate-500">Monthly Rent</p>
//               <p className="text-xl font-semibold text-slate-900">
//                 ₹{data.adjustedRent}
//               </p>
//             </div>

//             <div className="rounded-lg bg-slate-50 p-4">
//               <p className="text-xs text-slate-500">Annual Revenue</p>
//               <p className="text-xl font-semibold text-slate-900">
//                 ₹{data.annualRevenue}
//               </p>
//             </div>
//           </div>

//           <p className="text-xs text-slate-500">{data.explanation}</p>
//         </>
//       )}
//     </div>
//   );
// }

import { useEffect, useState } from "react";
import { Calculator, ArrowRight, DollarSign } from "lucide-react";
import { calculatePricingScenario } from "../../api/pricingAPI";

export default function PricingSlider({ propertyId = "A" }) {
  const [adjustment, setAdjustment] = useState(0);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    calculatePricingScenario(propertyId, adjustment)
      .then((res) => setData(res))
      .finally(() => setLoading(false));
  }, [propertyId, adjustment]);

  return (
    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-8">
      <div className="flex items-center gap-3 mb-6">
        <div className="bg-indigo-600 p-2 rounded-lg shadow-lg shadow-indigo-200">
          <Calculator size={20} className="text-white" />
        </div>
        <div>
          <h2 className="text-lg font-bold text-slate-900">Dynamic Pricing Simulator</h2>
          <p className="text-sm text-slate-500">AI-driven demand elasticity modeling</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        {/* Slider Section */}
        <div className="lg:col-span-5 space-y-4">
          <div className="flex justify-between items-center text-sm font-medium">
             <span className="text-slate-500">Rent Adjustment</span>
             <span className={`px-3 py-1 rounded-md ${adjustment > 0 ? 'bg-emerald-50 text-emerald-700' : adjustment < 0 ? 'bg-rose-50 text-rose-700' : 'bg-slate-100 text-slate-700'}`}>
               {adjustment > 0 ? '+' : ''}{adjustment}%
             </span>
          </div>
          
          <input
            type="range"
            min="-10"
            max="20"
            value={adjustment}
            onChange={(e) => setAdjustment(Number(e.target.value))}
            className="w-full h-2 bg-slate-100 rounded-lg appearance-none cursor-pointer accent-indigo-600"
          />
          <div className="flex justify-between text-xs text-slate-400 font-medium px-1">
            <span>-10%</span>
            <span>Current</span>
            <span>+20%</span>
          </div>
        </div>

        {/* Results Section */}
        <div className="lg:col-span-7">
          {loading || !data ? (
            <div className="h-24 bg-slate-50 rounded-xl border border-slate-100 border-dashed flex items-center justify-center text-sm text-slate-400 animate-pulse">
              Simulating market response...
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="bg-slate-50 rounded-xl p-4 border border-slate-100 group hover:border-indigo-100 transition-colors">
                <p className="text-xs text-slate-500 font-medium uppercase tracking-wide mb-1">Projected Rent</p>
                <div className="flex items-baseline gap-1">
                   <span className="text-lg font-bold text-slate-900">₹{data.adjustedRent.toLocaleString()}</span>
                   <span className="text-xs text-slate-400">/mo</span>
                </div>
              </div>

              <div className="bg-slate-900 rounded-xl p-4 border border-slate-800 shadow-lg shadow-slate-200 group">
                <p className="text-xs text-slate-400 font-medium uppercase tracking-wide mb-1">Projected Revenue</p>
                <div className="flex items-baseline gap-1">
                   <span className="text-lg font-bold text-white">₹{data.annualRevenue.toLocaleString()}</span>
                   <span className="text-xs text-slate-500">/yr</span>
                </div>
              </div>

              <div className="sm:col-span-2 mt-2">
                 <p className="text-xs text-slate-500 bg-white p-3 rounded-lg border border-slate-100 flex gap-2">
                   <ArrowRight size={14} className="text-indigo-500 mt-0.5 shrink-0" />
                   {data.explanation}
                 </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}