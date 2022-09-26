import { defineConfig } from 'astro/config';
import svelte from '@astrojs/svelte';
import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  outDir: '../../dist/apps/website',
  integrations: [svelte(), sitemap(), tailwind()],
});
