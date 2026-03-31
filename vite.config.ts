import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

// https://vite.dev/config/
export default defineConfig({ 
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
