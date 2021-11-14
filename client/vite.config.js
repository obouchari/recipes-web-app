import { svelte } from "@sveltejs/vite-plugin-svelte";
import { defineConfig } from "vite";
import path from "path";

export default defineConfig({
  server: {
    port: 5000,
    proxy: {
      "/api": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true,
        secure: false,
      },
    },
  },

  plugins: [svelte()],

  resolve: {
    alias: {
      $lib: path.resolve("./src/lib"),
      $services: path.resolve("./src/services"),
      $stores: path.resolve("./src/stores"),
      $utils: path.resolve("./src/utils"),
    },
  },
});
