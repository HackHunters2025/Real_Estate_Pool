// import DashboardLayout from "../layouts/DashboardLayout";
// import ForecastChart from "../components/dashboard/ForecastChart";
// import ESGStatusCard from "../components/dashboard/ESGStatusCard";
// import ChurnRiskCard from "../components/dashboard/ChurnRiskCard";
// import PricingSlider from "../components/dashboard/PricingSlider";
// import AlertsPanel from "../components/alerts/AlertsPanel";

// export default function Dashboard() {
//   return (
//     <DashboardLayout title="EstateX Intelligence Dashboard">
//       <div className="space-y-8">
//         <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
//           <ForecastChart />
//           <ESGStatusCard />
//           <ChurnRiskCard />
//         </div>

//         <PricingSlider />
//         <AlertsPanel />
//       </div>
//     </DashboardLayout>
//   );
// }

import DashboardLayout from "../layouts/DashboardLayout";
import ForecastChart from "../components/dashboard/ForecastChart";
import ESGStatusCard from "../components/dashboard/ESGStatusCard";
import ChurnRiskCard from "../components/dashboard/ChurnRiskCard";
import PricingSlider from "../components/dashboard/PricingSlider";
import AlertsPanel from "../components/alerts/AlertsPanel";

export default function Dashboard() {
  return (
    <DashboardLayout title="EstateX Intelligence">
      <div className="space-y-6">
        
        {/* Top Row: Chart takes 2 cols, Cards take 1 col each */}
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 h-auto lg:h-[400px]">
          <div className="lg:col-span-2 h-full">
            <ForecastChart />
          </div>
          <div className="lg:col-span-1 h-full">
            <ESGStatusCard />
          </div>
          <div className="lg:col-span-1 h-full">
            <ChurnRiskCard />
          </div>
        </div>

        {/* Bottom Row: Pricing Slider */}
        <div className="grid grid-cols-1 gap-6">
          <PricingSlider />
        </div>

        {/* Alerts Section */}
        <div className="mt-8">
          <AlertsPanel />
        </div>
      </div>
    </DashboardLayout>
  );
}
