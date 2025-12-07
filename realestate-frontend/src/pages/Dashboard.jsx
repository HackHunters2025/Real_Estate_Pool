import DashboardLayout from "../layouts/DashboardLayout";
import ForecastChart from "../components/dashboard/ForecastChart";
import ESGStatusCard from "../components/dashboard/ESGStatusCard";
import ChurnRiskCard from "../components/dashboard/ChurnRiskCard";
import PricingSlider from "../components/dashboard/PricingSlider";
import AlertsPanel from "../components/alerts/AlertsPanel";
import ScenarioSimulator from "../components/dashboard/ScenarioSimulator";
import LeaseAnalyzer from "../components/dashboard/LeaseAnalyzer";
import MaintenanceStatusCard from "../components/dashboard/MaintenanceStatusCard";
import OccupancyCard from "../components/dashboard/OccupancyChart";
import PortfolioOptimization from "../components/dashboard/PortfolioSummary";
import NewsSentimentCard from "../components/dashboard/NewsSentimentCard";

export default function Dashboard() {
  return (
    <DashboardLayout title="EstateX Intelligence">
      <div className="space-y-8">
        {/* TOP GRID */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-3">
          <div className="lg:col-span-2">
            <ForecastChart />
          </div>
          <ESGStatusCard />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-3">
          <ChurnRiskCard />
          <NewsSentimentCard />
          <MaintenanceStatusCard />
        </div>

           <div className="grid grid-cols-3 lg:grid-cols-3 gap-3">
        <OccupancyCard />
         <div className="lg:col-span-2">
        <PortfolioOptimization />
        </div>
      </div>

        {/* Pricing */}
        <PricingSlider />

        {/* Scenario */}
        <ScenarioSimulator />

        {/* Alerts */}
        <AlertsPanel />

        {/* Lease */}
        <LeaseAnalyzer />
      </div>
    </DashboardLayout>
  );
}
