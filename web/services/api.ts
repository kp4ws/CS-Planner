export const BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export const authHeaders = () => ({
    'Authorization': `Bearer ${localStorage.getItem('token')}`,
    'Content-Type': 'application/json'
});