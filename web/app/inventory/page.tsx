"use client";

import { useInventory } from "@/hooks/features/use-inventory";
import { Button } from "@/components/ui/button";
import { Filter } from "lucide-react";
import { logger } from "@/lib/logger";

export default function InventoryPage() {
  const { items, categories, isLoading, error, deleteItem } = useInventory();

  if (error) {
    // TODO: Refactor error screen
    return (
      <div className="">
        <h2 className="text-white">Failed to load inventory</h2>
      </div>
    );
  }

  if (!isLoading) {
    logger.info(
      "Category Titles:",
      categories.map((c) => c.title),
    );
  } else {
    logger.info("Data is loading");
  }

  return (
    <div className="min-h-screen px-6 py-4">
      {/* Inventory Header */}
      <header className="flex justify-between items-center mb-6">
        {/* TODO: Consider hiding page headers on desktop screens */}
        <h1 className="text-lg md:text-4xl text-white font-bold">Inventory</h1>

        {/* IMPORT/EXPORT BUTTONS & FILTER */}
        <div className="flex justify-center items-center">
          <div className="px-4">
            <Button size="lg">Import</Button>
            <Button size="lg">Export</Button>
          </div>

          <Filter color="white" size={24} />
        </div>
      </header>

      {/* CATEGORY SECTIONS */}
      <section className="flex flex-col items-start gap-4">
        {categories.map((category) => (
          <h1 key={category.id} className="text-xl font-semibold text-white">
            {category.title}
          </h1>
        ))}
      </section>

      {/* FOOTER SECTION (ADD BUTTON) */}
      <section className="flex justify-center items-center">
        <Button size="lg">Add</Button>
      </section>
    </div>
  );
}
