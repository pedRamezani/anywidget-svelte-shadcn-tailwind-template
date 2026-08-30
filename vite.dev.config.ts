import { defineConfig } from 'vite';
import { baseConfig } from './vite.config';

// https://vite.dev/config/
export default defineConfig({
	...baseConfig,
	build: {
		...baseConfig.build,
		sourcemap: 'inline',
		// Keep watch rebuilds from wiping the output dir each time.
		emptyOutDir: false,
		watch: {
			include: 'src/**',
			exclude: ['node_modules/**', 'notebooks/**', 'py/**']
		}
	}
});
