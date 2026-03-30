import { svelte } from '@sveltejs/vite-plugin-svelte';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [tailwindcss(), svelte()],
	build: {
        assetsDir: '',
		outDir: './src/ipyfoo/static/',
        lib: {
            entry: ["./web/index.js"],
            formats: ["es"],
        },
		rollupOptions: {
			// input: './web/index.js',
			output: {
				entryFileNames: `assets/[name].js`,
				chunkFileNames: `assets/[name].js`,
				assetFileNames: `assets/[name].[ext]`
			}
		}
	}
});
