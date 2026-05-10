"use client";

import { useEffect } from "react";
import { logger } from "@/lib/logger";
import { Button } from "@/components/ui/button";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    logger.error("Global UI Crash", error);
  }, [error]);
// TODO: update error page layout
  return (
    <div className="">
        <h2 className="text-white">BackpackPal ran into Error!</h2>
        <Button onClick={() => reset()} size="lg">
            Try again
        </Button>
    </div>
  );
}
