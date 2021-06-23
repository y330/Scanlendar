import autoPreprocess from "svelte-preprocess"
import postcssImport, { postcss } from "postcss-import"
import resolve from "@rollup/plugin-node-resolve"
import commonjs from "@rollup/plugin-commonjs"
import livereload from "rollup-plugin-livereload"
import { terser } from "rollup-plugin-terser"
import svelte from "rollup-plugin-svelte-hot"
import Hmr from "rollup-plugin-hot"
import { scss } from "svelte-preprocess"
/*--------------------------------------*/
const production = !process.env.ROLLUP_WATCH
const assetsDir = "public/assets"
const buildDir = `public/build`
/*-------------------------------------*/
export default {
	preserveEntrySignatures: false,
	input: [`src/main.js`],
	output: {
		sourcemap: true,
		format: "esm",
		dir: buildDir,
		// for performance, disabling filename hashing in development
		chunkFileNames: `[name]${(production && "-[hash]") || ""}.js`,
	},

	plugins: [
		svelte({
			emitCss: false,
			// enable run-time checks when not in production
			dev: !production,
			// we'll extract any component CSS out into
			// a separate file - better for performance
			preprocess: [
				autoPreprocess({
					postcss: { plugins: [postcssImport()] },
					defaults: { style: postcss },
				}),
			],
		}),

		// If you have external dependencies installed from
		// npm, you'll most likely need these plugins. In
		// some cases you'll need additional configuration -
		// consult the documentation for details:
		// https://github.com/rollup/plugins/tree/master/packages/commonjs
		resolve({
			browser: true,
			dedupe: ["svelte"],
		}),
		commonjs(),

		// In dev mode, call `npm run start` once
		// the bundle has been generated
		!production && serve(),

		// Watch the `public` directory and refresh the
		// browser on changes when not in production
		!production && livereload("public"),

		// If we're building for production (npm run build
		// instead of npm run dev), minify
		production && terser(),
	],
	watch: {
		clearScreen: false,
	},
}

function serve() {
	let started = false

	return {
		writeBundle() {
			if (!started) {
				started = true

				require("child_process").spawn("npm", ["run", "start", "--", "--dev"], {
					stdio: ["ignore", "inherit", "inherit"],
					shell: true,
				})
			}
		},
	}
}
