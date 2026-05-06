import { GearItem, GearItemCreate, GearItemUpdate } from "@/types";
import { BASE_URL, authHeaders } from "./api";

export const getGearItems = async (): Promise<GearItem[]> => {
  const response = await fetch(`${BASE_URL}/gear_items`, {
    headers: authHeaders(),
  });

  if (!response.ok) throw new Error("Failed to fetch gear items");
  return response.json();
};

export const createGearItem = async (data: GearItemCreate): Promise<GearItem> => {
  const response = await fetch(`${BASE_URL}/gear_items`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to create gear item");
  return response.json();
};

export const updateGearItem = async (
  id: string,
  data: GearItemUpdate,
): Promise<GearItemUpdate> => {
  const response = await fetch(`${BASE_URL}/gear_items/${id}`, {
    method: "PATCH",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to create gear item");
  return response.json();
};

export const deleteGearItem = async (id: string): Promise<void> => {
    const response = await fetch(`${BASE_URL}/gear_items/${id}`, {
        method: "DELETE",
        headers: authHeaders()
    });

    if(!response.ok) throw new Error("Failed to delete gear item");
};