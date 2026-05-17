"use client";

import { useInventory } from "@/hooks/features/use-inventory";
import { Button } from "@/components/ui/Button";
import { Filter } from "lucide-react";
import { logger } from "@/lib/logger";

export default function InventoryPage() {
  const { items, categories, isLoading, error, deleteItem } = useInventory();

  if (isLoading) {
    // TODO: Refactor loading widget
    return <p>Loading ...</p>;
  }

  if (error) {
    // TODO: Refactor error widget
    return (
      <div className="">
        <h2 className="text-white">Failed to load inventory</h2>
      </div>
    );
  }

  return (
    <div className="min-h-screen px-6 py-4">
      {/* Inventory Header */}
      <header className="flex justify-between items-center mb-6">
        {/* TODO: Error/Warning bar at top */}
        <div></div>

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
        {categories.map(category => {
          const categoryItems = items.filter(item => item.category_id === category.id);
          
          return (
              <div key={category.id}>

              </div>
          );
        })}
      </section>

      {/* FOOTER SECTION (ADD BUTTON) */}
      <section className="flex justify-center items-center">
        <Button size="lg">Add</Button>
      </section>
    </div>
  );
}
