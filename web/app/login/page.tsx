"use client";

import { useState, SyntheticEvent } from "react";

export default function Login() {
  const [loading, setLoading] = useState<boolean>(false);

  const handleLogin = async (event: SyntheticEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);

    const formData = new FormData(event.currentTarget);
    
    // TODO: Ensure log messages are only displayed in development environment
    console.log("Sending login data to API");
    const response = await fetch("http://localhost:8001/api/v1/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams(formData as any),
    });

    console.log("Response status:", response.status);

    if(response.ok) {
      const result = await response.json();
      console.log("Success:", result);
    }
    else {
      const errorData = await response.json();
      console.log("Validation Error:", errorData);
    }

    setLoading(false);
  };

  return (
    <div className="">
      <header className="">
        <h1 className="text-white font-bold">Login</h1>
      </header>

      {/* LOGIN FORM */}
      <section>
        <form onSubmit={handleLogin} className="">
          {/* FORM FIELDS TODO: Make this a UI component */}
          <div className="text-white">
            <label htmlFor="username">Username</label>
            <input
              id="username"
              name="username"
              type="text"
              required
              placeholder="Enter Username..."
            />
            {/* Field description */}
          </div>

          {/* TODO: Should login require email? */}

          <div className="text-white">
            <label htmlFor="password">Password</label>
            <input
              id="password"
              name="password"
              type="password"
              placeholder="Enter Password..."
            />
          </div>

          <button className="text-white" type="submit">
            Submit
          </button>
        </form>
      </section>
    </div>
  );
}

// TODO: Should I include logins using 3rd party services like Google, etc?
