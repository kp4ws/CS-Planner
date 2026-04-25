
import { Button } from "@/components/ui/button";
import {Zap} from "lucide-react";
import Link from "next/link";

export default function Home() {
  return (
    <div className="bg-emerald-900">
      {/* HERO SECTION */}
      <section className="py-10 md:py-20 min-h-screen flex flex-col items-center justify-center">
        <h1 className="text-2xl md:text-4xl font-extrabold text-white mb-4">Pack Smarter.</h1>
        <p className="text-emerald-100 text-lg mb-8">Plan every trip with the perfect loadout.</p>
        
        <Link href="/planner">
          <Button size="lg" className="gap-2">
          <Zap size={20} />
            Start Building
            </Button>
        </Link>
      </section>

      {/* TODO: FEATURES SECTION */}
      {/* <section>
        TODO: Features Section
      </section> */}
    </div>
  );
}
