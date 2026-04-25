"use client"
import Link from "next/link";
import { Menu } from "lucide-react";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";

export default function NavBar() {
  return (
    <nav className="sticky top-0 z-50 bg-emerald-950">
      {/* FIRST ROW */}
      <div className="flex items-center justify-between px-6 py-4">
        {/* APP LOGO */}
        <Link
          href="/"
          className="text-lg md:text-xl font-bold text-white hover:text-emerald-200"
        >
          Backpack Pal
        </Link>

        {/* DESKTOP NAVIGATION */}
        <div className="hidden md:flex items-center gap-3 md:gap-6">
          <Link href="/login" className="text-white hover:text-emerald-200">
            Login
          </Link>
          <Link href="/register" className="text-white hover:text-emerald-200">
            Register
          </Link>
        </div>

        {/* MOBILE Menu */}
        <Sheet>
          <SheetTrigger asChild className="md:hidden">
            <button>
              <Menu size={24} className="text-white" />
            </button>
          </SheetTrigger>
          <SheetContent className="bg-emerald-950 [&_button]:text-white">
            <div className="flex flex-col items-center gap-4 mt-8">
              <Link href="" className="text-white hover:text-emerald-200">
                Builder
              </Link>
              <Link href="" className="text-white hover:text-emerald-200">
                Storage Locker
              </Link>

              <hr />

              <Link
                href="/login"
                className="text-lg text-white hover:text-emerald-200"
              >
                Login
              </Link>
              <Link
                href="/register"
                className="text-lg text-white hover:text-emerald-200"
              >
                Register
              </Link>
            </div>
          </SheetContent>
        </Sheet>
      </div>

      {/* SECOND ROW */}
      <div className="hidden md:flex border-t border-emerald-900 gap-6 px-6 py-3">
        <Link href="" className="text-white hover:text-emerald-200">
          Builder
        </Link>
        <Link href="" className="text-white hover:text-emerald-200">
          Storage Locker
        </Link>
      </div>

      {/* DARK MODE TOGGLE: TODO */}
    </nav>
  );
}
