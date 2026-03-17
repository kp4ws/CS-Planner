"use client"

import {useState} from 'react';
import Link from "next/link";

export default function Register() {
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    
    const handleSubmit = async (event: React.SubmitEvent) => {
        event.preventDefault();
        
        const response = await fetch("http://localhost:8000/auth/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({username, password})
        });

        const data = await response.json();
        console.log(data);
    };

    return (
        <main>
            <div>
                <h1>Register </h1>
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
                    <Link href="/login">Login</Link>
                </form>
            </div>
        </main>
    );
}