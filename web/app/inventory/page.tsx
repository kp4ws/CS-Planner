"use client";

import { Button } from "@/components/ui/button";
import { Filter } from "lucide-react";
import { useState, useEffect } from "react";

import CategoryGroup from "@/components/category-group";

export default function Inventory() {
  const [loading, setLoading] = useState<boolean>(true);
  const [filter, setFilter] = useState<string | null>(null); //TODO: Create FilterState for more advance filtering
  // const [categories, setCategories] = useState<>();
  // const [items, setItems] = useState<GearItem[]>([]);

  //Load categories and inventory items from database
  useEffect(() => {

  }, []);

  // useEffect(() => {
  //   fetch("http://localhost:8000/inventory")
  //     .then((res) => res.json())
  //     .then((data) => {
  //       setItems(data);
  //       setLoading(false);
  //     });
  // }, []);

  // TODO: Fetch Categories from database
  // TODO: Should categories be hardcoded? Is having them the database going to slow down the website?

  // const handleEdit = (item: GearItem) => {

  // };

  const handleDelete = (id: string) => {

  };


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
      <section className="flex flex-col items-start">
        {/* TODO: Icon should be associated with each category */}
        {/* {categories.map((category) => (
          <CategoryGroup
            key={category}
            title={category}
            items={items?.filter((item) => item.category === category)}
            onEdit={(item) => handleEdit(item)}
            onDelete={(id) => handleDelete(id)}
          />
        ))} */}
      </section>

      {/* FOOTER SECTION (ADD BUTTON) */}
      <section className="flex justify-center items-center">
        <Button size="lg">Add</Button>
      </section>
    </div>
  );
}
