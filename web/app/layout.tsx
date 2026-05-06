import type { Metadata, Viewport } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { cn } from "@/lib/utils";
import NavBar from "@/components/navbar";
import Providers from "@/components/providers";

const inter = Inter({ subsets: ["latin"], variable: "--font-sans" });

export const viewport: Viewport = {
  themeColor: "#064e3b",
  width: "device-width",
  initialScale: 1,
}

export const metadata: Metadata = {
  title: "Backpack Pal",
  description: "Strategic gear planning.",
  manifest: "/manifest.json",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={cn("font-sans", inter.variable)}>
      <body
        className={`${inter.variable} ${inter.variable} antialiased`}
      >
        <NavBar />

        <main className="bg-emerald-900">
          <Providers>{children}</Providers>
        </main>

        <footer className="py-10 md:py-20 bg-emerald-950 text-white text-center">
          <p>&copy; 2026 Backpack Pal. All rights reserved.</p>
        </footer>
      </body>
    </html>
  );
}
