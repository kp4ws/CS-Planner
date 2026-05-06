import { Category, CategoryCreate, CategoryUpdate } from "@/types";
import { BASE_URL, authHeaders } from "./api";

export const getCategories = async (): Promise<Category[]> => {
  const response = await fetch(`${BASE_URL}/categories`, {
    headers: authHeaders(),
  });

  if (!response.ok) throw new Error("Failed to fetch categories");
  return response.json();
};

export const createCategory = async (
  data: CategoryCreate
): Promise<Category> => {
  const response = await fetch(`${BASE_URL}/categories`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(data),
  });

  if (!response.ok) throw new Error("Failed to create category");
  return response.json();
};

export const updateCategory = async (id: string, data: CategoryUpdate) : Promise<Category> => {
    const response = await fetch(`${BASE_URL}/categories/${id}`, {
        method: "PATCH",
        headers: authHeaders(),
        body: JSON.stringify(data)
    });

    if(!response.ok) throw new Error("Failed to update category");
    return response.json();
};

export const deleteCategory = async (id: string): Promise<void> => {
    const response = await fetch(`${BASE_URL}/categories/${id}`, {
        method: 'DELETE',
        headers: authHeaders(),
    });  

    if(!response.ok) throw new Error("Failed to delete category");
};