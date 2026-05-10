export const config = {
    api: {
        baseUrl: (process.env.NEXT_PUBLIC_API_URL || "http://localhost:8001") + "/api/v1",
    },
    clerk: {
        publishableKey: process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY || "",
    },
    env: {
        isDev: process.env.NODE_ENV === "development",
        isProd: process.env.NODE_ENV === "production",
    },
} as const;

export type AppConfig = typeof config;