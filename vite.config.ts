import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import path from 'path/win32';

// https://vite.dev/config/
export default defineConfig({
    resolve: {
        alias: {
            $lib: path.resolve("./src/lib").replaceAll("\\", "/"),
        },
    },
    plugins: [tailwindcss(), svelte()],
    build: {
        assetsDir: '',
		outDir: './py/ipyfoo/static/',
        lib: {
            entry: ["./src/main.ts"],
            formats: ["es"],
        },
		rollupOptions: {
			output: {
				entryFileNames: `[name].js`,
				chunkFileNames: `[name].js`,
				assetFileNames: `[name].[ext]`
			}
		}
	}
});
