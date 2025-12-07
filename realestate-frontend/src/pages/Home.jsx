import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  ArrowRight,
  User,
  Search,
  Building2,
  TrendingUp,
  ShieldCheck,
  Star,
  ExternalLink,
  LayoutDashboard, // Imported icon for dashboard
} from "lucide-react";

// Data with 20 companies and Updated Images for Godrej & Embassy
const COMPANIES = [
  {
    id: 1,
    name: "RMZ Corp",
    segment: "Commercial",
    image:
      "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&h=400&fit=crop",
    url: "https://www.rmzcorp.com/",
  },
  {
    id: 2,
    name: "Prestige",
    segment: "Luxury Living",
    image:
      "https://images.unsplash.com/photo-1582407947304-fd86f028f716?w=600&h=400&fit=crop",
    url: "https://www.prestigeconstructions.com/",
  },
  {
    id: 3,
    name: "Brigade",
    segment: "Mixed Use",
    image:
      "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=600&h=400&fit=crop",
    url: "https://www.brigadegroup.com/",
  },
  {
    id: 4,
    name: "Sobha",
    segment: "Premium",
    image:
      "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600&h=400&fit=crop",
    url: "https://www.sobha.com/",
  },
  {
    id: 5,
    name: "Godrej",
    segment: "Townships",
    image:
      "https://images.unsplash.com/photo-1577495508048-b635879837f1?w=600&h=400&fit=crop",
    url: "https://www.godrejproperties.com/",
  },
  {
    id: 6,
    name: "DLF",
    segment: "Commercial",
    image:
      "https://images.unsplash.com/photo-1486325212027-8081e485255e?w=600&h=400&fit=crop",
    url: "https://www.dlf.in/",
  },
  {
    id: 7,
    name: "Oberoi Realty",
    segment: "Luxury",
    image:
      "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600&h=400&fit=crop",
    url: "https://www.oberoirealty.com/",
  },
  {
    id: 8,
    name: "Lodha Group",
    segment: "World Towers",
    image:
      "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=600&h=400&fit=crop",
    url: "https://www.lodhagroup.in/",
  },
  {
    id: 9,
    name: "Hiranandani",
    segment: "Community",
    image:
      "https://images.unsplash.com/photo-1531835551805-16d864c8d311?w=600&h=400&fit=crop",
    url: "https://www.hiranandani.com/",
  },
  {
    id: 10,
    name: "Tata Housing",
    segment: "Trusted",
    image:
      "https://images.unsplash.com/photo-1554469384-e58fac16e23a?w=600&h=400&fit=crop",
    url: "https://www.tatahousing.in/",
  },
  {
    id: 11,
    name: "Mahindra",
    segment: "Sustainable",
    image:
      "https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=600&h=400&fit=crop",
    url: "https://www.mahindralifespaces.com/",
  },
  {
    id: 12,
    name: "Puravankara",
    segment: "Residential",
    image:
      "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=600&h=400&fit=crop",
    url: "https://www.puravankara.com/",
  },
  {
    id: 13,
    name: "Salarpuria",
    segment: "IT Parks",
    image:
      "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=600&h=400&fit=crop",
    url: "https://www.sattvagroup.in/",
  },
  {
    id: 14,
    name: "Embassy",
    segment: "Office Parks",
    image:
      "https://images.unsplash.com/photo-1464938050520-ef2270bb8ce8?w=600&h=400&fit=crop",
    url: "https://www.embassyindia.com/",
  },
  {
    id: 15,
    name: "Kalpataru",
    segment: "Premium",
    image:
      "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&h=400&fit=crop",
    url: "https://www.kalpataru.com/",
  },
  {
    id: 16,
    name: "Casagrand",
    segment: "Villas",
    image:
      "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=600&h=400&fit=crop",
    url: "https://www.casagrand.co.in/",
  },
  {
    id: 17,
    name: "Shapoorji",
    segment: "Engineering",
    image:
      "https://images.unsplash.com/photo-1583608205776-bfd35f0d9f83?w=600&h=400&fit=crop",
    url: "https://shapoorjipallonji.com/",
  },
  {
    id: 18,
    name: "Assetz",
    segment: "Boutique",
    image:
      "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&h=400&fit=crop",
    url: "https://www.assetzproperty.com/",
  },
  {
    id: 19,
    name: "Phoenix",
    segment: "Retail/Mixed",
    image:
      "https://images.unsplash.com/photo-1555636222-cae831e670b3?w=600&h=400&fit=crop",
    url: "https://www.thephoenixmills.com/",
  },
  {
    id: 20,
    name: "Runwal",
    segment: "Suburban",
    image:
      "https://images.unsplash.com/photo-1625602812206-5ec545ca1231?w=600&h=400&fit=crop",
    url: "https://runwal.com/",
  },
];

export default function Home() {
  const [searchTerm, setSearchTerm] = useState("");
  const navigate = useNavigate();

  // Search Logic
  const filteredCompanies = COMPANIES.filter(
    (company) =>
      company.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      company.segment.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="flex flex-col min-h-screen bg-slate-50 font-sans w-full text-slate-900">
      <header className="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200">
        <div className="max-w mx-auto px-4 sm:px-6 lg:px-8 w-full">
          <div className="flex justify-between items-center h-16 sm:h-20">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 sm:w-10 sm:h-10 bg-blue-600 rounded-lg flex items-center justify-center shadow-blue-200 shadow-md">
                <Building2 size={20} className="text-white" />
              </div>
              <h1 className="text-xl sm:text-2xl font-bold ">
                Estate<span className="text-blue-600">X</span>
              </h1>
            </div>

            <div className="flex items-center gap-4">
              <nav className="hidden md:flex gap-6 text-ls font-medium text-slate-600 mr-4">
                <a href="#about-us" className="hover:text-blue-600 transition-colors">
                  About Us
                </a>
              </nav>

              {/* NEW: Get Started / Dashboard Button */}
              <button
                onClick={() => navigate("/dashboard")}
                className="hidden sm:flex items-center gap-2 bg-slate-900 hover:bg-slate-800 text-white px-5 py-2.5 rounded-full font-semibold text-sm transition-all shadow-md hover:shadow-lg active:scale-95 group"
              >
                <span>Get Started</span>
                <ArrowRight
                  size={16}
                  className="group-hover:translate-x-0.5 transition-transform"
                />
              </button>

              <button className="p-2 hover:bg-slate-100 rounded-full transition-colors duration-200">
                <User size={24} className="text-slate-600" />
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="flex-1 w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-16">
        <div className="text-center max-w-4xl mx-auto mb-16">
          <h2 className="text-4xl sm:text-4xl lg:text-6xl font-extrabold text-slate-900 leading-tight tracking-tight">
            Find space with{" "}
            <span className="text-blue-600">Industry Giants</span>
          </h2>

          <p className="mt-6 text-lg sm:text-xl text-slate-600 max-w-2xl mx-auto">
            Access exclusive listings from India's top real estate developers.
          </p>
        </div>

        <div className="mb-20">
          <div className="flex justify-between items-end mb-6 px-2">
            <h3 className="text-sm font-bold text-slate-400 uppercase tracking-widest">
              Trusted Partners
            </h3>
            {/* <button className="text-blue-600 text-sm font-bold flex items-center hover:underline group">
              View Directory 
              <ArrowRight size={16} className="ml-1 group-hover:translate-x-0.5 transition-transform" />
            </button> */}
          </div>

          <div className="flex overflow-x-auto gap-8 pb-10  snap-x p-2 -mx-2">
            {filteredCompanies.length > 0 ? (
              filteredCompanies.map((company) => (
                <a
                  key={company.id}
                  href={company.url}
                  target="_blank"
                  rel="noreferrer"
                  className="group shrink-0 w-96 bg-white p-5 rounded-3xl border border-slate-100 shadow-sm hover:shadow-2xl hover:shadow-blue-900/10 hover:-translate-y-2 hover:border-blue-100 transition-all duration-300 cursor-pointer relative snap-center"
                >
                  <div className="absolute top-5 right-5 z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 p-1.5 bg-white/90 backdrop-blur-md rounded-full shadow-sm">
                    <ExternalLink size={16} className="text-slate-700" />
                  </div>

                  <div className="w-full h-56 mb-5 rounded-2xl overflow-hidden relative shadow-inner">
                    <img
                      src={company.image}
                      alt={company.name}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
                    />
                    <div className="absolute inset-0 bg-linear-to-t from-slate-900/10 to-transparent pointer-events-none"></div>
                  </div>

                  <h4 className="text-slate-900 font-bold text-2xl mb-2">
                    {company.name}
                  </h4>
                  <div className="items-center gap-1.5 text-xs text-slate-600 font-semibold bg-slate-50 py-1.5 px-3 rounded-lg border border-slate-100 self-start inline-flex">
                    <TrendingUp size={14} className="text-blue-600" />
                    {company.segment}
                  </div>
                </a>
              ))
            ) : (
              <div className="w-full text-center py-12 bg-slate-50 rounded-xl border border-dashed border-slate-200">
                <p className="text-base text-slate-400 font-medium">
                  No partners found matching "{searchTerm}"
                </p>
              </div>
            )}
          </div>
        </div>

        {/* Footer Area aligned left */}
        <div id="about-us" className="scroll-mt-24 w-full rounded-3xl p-8 lg:p-12">
          <div className="ml-0 grid grid-cols-1 lg:grid-cols-2 gap-5 lg:gap-20 items-center">
            <div className="w-full">
              {/* <div className="inline-flex items-center gap-1.5 bg-green-50 border border-green-200/60 rounded-full px-3 py-1 mb-6 shadow-sm">
                 <ShieldCheck size={16} className="text-green-600" />
                 <span className="text-sm font-bold text-green-700">RERA Verified Platform</span>
              </div> */}

              <h3 className="text-3xl sm:text-4xl font-bold text-slate-900 mb-4">
                Smarter decisions for modern real estate.
              </h3>
              <p className="text-slate-900 text-xl mb-8 max-w-lg">
                EstateX Intelligence is an AI-powered real estate analytics
                platform designed to help asset managers, investors, and
                enterprises make smarter, data-driven decisions.
              </p>

              <div className="hidden lg:block text-slate-400 text-sm font-medium">
                Trusted by{" "}
                <span className="text-slate-900 font-bold">10,000+</span>{" "}
                homebuyers this month
              </div>
            </div>
            <div className="flex flex-col sm:flex-row gap-6">
              <div className="flex-1 grid grid-cols-2 gap-4">
                <div className="bg-slate-50 p-6 rounded-2xl border border-slate-100 flex flex-col items-center justify-center text-center">
                  <div className="text-3xl sm:text-4xl font-black text-blue-600 mb-2">
                    500+
                  </div>
                  <div className="text-xs sm:text-sm text-slate-500 font-bold uppercase tracking-wide">
                    Premium Projects
                  </div>
                </div>
                <div className="bg-slate-50 p-6 rounded-2xl border border-slate-100 flex flex-col items-center justify-center text-center">
                  <div className="flex items-center gap-1 text-3xl sm:text-4xl font-black text-emerald-500 mb-2">
                    4.9{" "}
                    <Star
                      size={24}
                      fill="currentColor"
                      className="text-emerald-500"
                    />
                  </div>
                  <div className="text-xs sm:text-sm text-slate-500 font-bold uppercase tracking-wide">
                    User Rating
                  </div>
                </div>
              </div>

              <button
                onClick={() => (window.location.href = "/dashboard")}
                className="flex-1 sm:max-w-[200px] bg-slate-900 hover:bg-slate-800 text-white font-semibold p-6 rounded-2xl shadow-xl shadow-slate-200 transition-all flex flex-col items-center justify-center gap-2 group active:scale-[0.98]"
              >
                <span className="text-lg">Start Exploring</span>
                <ArrowRight
                  size={24}
                  className="group-hover:translate-x-1 transition-transform"
                />
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
