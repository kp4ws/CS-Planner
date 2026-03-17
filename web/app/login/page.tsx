"use client"
import {useState} from 'react';
import Link from "next/link";
import {useRouter} from "next/navigation";

export default function Login() {
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');

    const router = useRouter();

    const handleSubmit = async (event: React.SubmitEvent) => {
        event.preventDefault();
        // console.log("Login with: ", {username, password});
        const response = await fetch("http://localhost:8000/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({username, password})
        });

        const data = await response.json();
        console.log(data);
    };

    const handleGuest = () => {
        router.push("/planner");
    };

    return (
        <main className="flex items-center justify-center h-screen">
            <div className="bg-white p-8 rounded-lg shadow-md w-96">
                <h1 className="text-4xl font-bold">Login</h1>
                <form onSubmit={handleSubmit}>
                    <div className="flex flex-col mb-4">
                        <label htmlFor='username'>Username</label>
                        <input id="username" type="text" value={username} onChange={(e) => setUsername(e.target.value)}/>
                    </div>

                    <div className="flex flex-col mb-4">
                        <label htmlFor='password'>Password</label>
                        <input id="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
                    </div>

                    <button type="submit">Submit</button>
                    <button type="button" onClick={handleGuest}>Continue As Guest</button>
                    <Link href="/register">Register</Link>
                </form>
            </div>
        </main>
    );
}
