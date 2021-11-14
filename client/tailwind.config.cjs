const colors = require('tailwindcss/colors')

const config = {
	mode: 'jit',
	purge: ['./src/**/*.svelte', './src/**/*.css'],

	theme: {
		extend: {
			colors: {
				yellow: colors.yellow
			}
		}
	},

	plugins: [
		require("@tailwindcss/aspect-ratio"),
		require('@tailwindcss/forms'),
		require('@tailwindcss/typography'),
	]
};

module.exports = config;
