import { build, defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';
import path from 'path';

export default defineConfig({
    root: 'frontend',
    plugins: [
        tailwindcss({
            optimize: { minify: true }
        })
    ],

    build: {
        // Please place in dedicated subfolder in directory where non-vite static assets live. 
        // Parent directory should match a Django STATICFILES_DIRS entry 
        outDir: path.resolve(__dirname, './static/vite'),
        emptyOutDir: true, // can overwrite since this subfolder is just for vite stuff
        manifest: false, // don't need this for this specific set up

        rolldownOptions: {
            input: {
                'app': path.resolve(__dirname, 'frontend/src/css/app.css'),
                'basecoat': path.resolve(__dirname, 'frontend/src/js/basecoat.js')
            },

            output: {
                // Want stable names for the main files
                entryFileNames: `js/[name].js`,
                // Prevents filename collisions that I am not smart enough to forsee
                chunkFileNames: `js/[name]-[hash].js`,
                assetFileNames: (assetInfo) => {
                if (assetInfo.names?.some(name => name.endsWith('.css'))) {
                    return 'css/[name][extname]'
                }
                return `[ext]/[name]-[extname]`;
                }
            }
        }
    },

    resolve: {
        alias: {
            '@': path.resolve(__dirname, 'frontend'),
        },
    }
})