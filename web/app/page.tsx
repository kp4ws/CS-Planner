import Link from "next/link";
import { Button } from "@/components/ui/button";
import { BookOpen, CheckCircle2, BarChart3, Zap } from "lucide-react";

export default function Home() {
  return (
    <main className="min-h-screen bg-linear-to-br from-slate-50 via-white to-slate-100">
      <nav className="sticky top-0 z-50 border-b border-slate-200 bg-white/80 backdrop-blur-md">
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <div className="text-2xl font-bold text-slate-900">CS Planner</div>
          <div className="flex gap-3">
            {/* OPTIONAL LINK BUTTONS */}
            {/* <Link href='/register'>
              <Button>Register</Button>
            </Link>
            <Link href="/login">
              <Button variant="outline">Sign In</Button>
            </Link> */}
          </div>
        </div>
      </nav>

      <section className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-24 sm:py-32">
        <div className="text-center">
          <h1 className="text-5xl sm:text-6xl font-bold tracking-tight text-slate-900 mb-6">
            Plan Your Computer Science Degree
            <span className="block text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 pb-2">
              Strategically
            </span>
          </h1>
          <p className="text-xl text-slate-600 mb-8 max-w-2xl mx-auto leading-relaxed">
            CS Planner helps you organize your course selection, track
            prerequisites, and visualize your academic path to success.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/planner">
              <Button size="lg" className="text-lg px-8">
                Continue as Guest
              </Button>
            </Link>
            <Link href="/login">
              <Button size="lg" variant="outline" className="text-lg px-8">
                Sign In
              </Button>
            </Link>
          </div>
        </div>
      </section>

      <section className="bg-white border-y border-slate-200">
        <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-20">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-slate-900 mb-4">
              Everything You Need
            </h2>
            <p className="text-lg text-slate-600">
              Powerful tools designed for CS students
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {/* Feature 1 */}
            <div className="flex flex-col items-start p-6 rounded-lg border border-slate-200 bg-slate-50 hover:bg-white hover:shadow-md transition-all">
              <BookOpen className="w-8 h-8 text-blue-600 mb-4" />
              <h3 className="font-semibold text-slate-900 mb-2">Course Planning</h3>
              <p className="text-slate-600 text-sm">
                Organize and plan all your CS courses with ease
              </p>
            </div>

            {/* Feature 2 */}
            <div className="flex flex-col items-start p-6 rounded-lg border border-slate-200 bg-slate-50 hover:bg-white hover:shadow-md transition-all">
              <CheckCircle2 className="w-8 h-8 text-green-600 mb-4" />
              <h3 className="font-semibold text-slate-900 mb-2">Prerequisites</h3>
              <p className="text-slate-600 text-sm">
                Organize and plan all your CS courses with ease
              </p>
            </div>

            {/* Feature 3 */}
            <div className="flex flex-col items-start p-6 rounded-lg border border-slate-200 bg-slate-50 hover:bg-white hover:shadow-md transition-all">
              <BarChart3 className="w-8 h-8 text-purple-600 mb-4" />
              <h3 className="font-semibold text-slate-900 mb-2">Progress Tracking</h3>
              <p className="text-slate-600 text-sm">
                Organize and plan all your CS courses with ease
              </p>
            </div>

            {/* Feature 4 */}
            <div className="flex flex-col items-start p-6 rounded-lg border border-slate-200 bg-slate-50 hover:bg-white hover:shadow-md transition-all">
              <Zap className="w-8 h-8 text-amber-600 mb-4" />
              <h3 className="font-semibold text-slate-900 mb-2">Smart Suggestions</h3>
              <p className="text-slate-600 text-sm">
                Organize and plan all your CS courses with ease
              </p>
            </div>
          </div>

        </div>
      </section>
    </main>
  );
}
