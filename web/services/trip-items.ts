import { TripItem, TripItemCreate, TripItemUpdate } from "@/types";
import { BASE_URL, authHeaders } from "./api";

export const getTripItems = async (): Promise<TripItem[]> => {
  const response = await fetch(`${BASE_URL}/trip_items`, {
    headers: authHeaders(),
  });

  if (!response.ok) throw new Error("Failed to fetch trip items");
  return response.json();
};

export const createTripItem = async (data: TripItemCreate): Promise<TripItem> => {
  const response = await fetch(`${BASE_URL}/trip_items`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to create trip item");
  return response.json();
};

export const updateTripItem = async (
  id: string,
  data: TripItemUpdate,
): Promise<TripItemUpdate> => {
  const response = await fetch(`${BASE_URL}/trip_items/${id}`, {
    method: "PATCH",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to create trip item");
  return response.json();
};

export const deleteTripItem = async (id: string): Promise<void> => {
    const response = await fetch(`${BASE_URL}/trip_items/${id}`, {
        method: "DELETE",
        headers: authHeaders()
    });

    if(!response.ok) throw new Error("Failed to delete trip item");
};