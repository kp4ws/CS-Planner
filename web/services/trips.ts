import { Trip, TripCreate, TripUpdate } from "@/types";
import { BASE_URL, authHeaders } from "./api";

export const getTrips = async (): Promise<Trip[]> => {
  const response = await fetch(`${BASE_URL}/trips`, {
    headers: authHeaders(),
  });

  if (!response.ok) throw new Error("Failed to fetch trips");
  return response.json();
};

export const createTrip = async (data: TripCreate): Promise<Trip> => {
  const response = await fetch(`${BASE_URL}/trips`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to create trip");
  return response.json();
};

export const updateTrip = async (
  id: string,
  data: TripUpdate,
): Promise<TripUpdate> => {
  const response = await fetch(`${BASE_URL}/trips/${id}`, {
    method: "PATCH",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to create trip");
  return response.json();
};

export const deleteTrip = async (id: string): Promise<void> => {
    const response = await fetch(`${BASE_URL}/trips/${id}`, {
        method: "DELETE",
        headers: authHeaders()
    });

    if(!response.ok) throw new Error("Failed to delete trip");
};