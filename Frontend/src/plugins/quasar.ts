// src/plugins/quasar.js
import { Quasar } from 'quasar';
import * as components from 'quasar'; // Import all components
import '@quasar/extras/material-icons/material-icons.css'; // Optional icons
import 'quasar/src/css/index.sass'; // Quasar styles
const myCustomDarkTheme = {
	dark: true,
	options: { customProperties: true },
	colors: {
		background: '#121212',
		surface: '#1E1E1E',
		'surface-bright': '#2E2E2E',
		'surface-light': '#424242',
		'surface-variant': '#FFFFFF',
		'on-surface-variant': '#000000',
		primary: '#2196F3',
		'primary-darken-1': '#1E88E5',
		secondary: '#FFC107',
		'secondary-darken-1': '#FFA000',
		error: '#B00020',
		info: '#03A9F4',
		success: '#4CAF50',
		warning: '#FF9800',
	},
	variables: {
		'border-color': '#FFFFFF',
		'border-opacity': 0.12,
		'high-emphasis-opacity': 0.87,
		'medium-emphasis-opacity': 0.60,
		'disabled-opacity': 0.38,
		'idle-opacity': 0.04,
		'hover-opacity': 0.04,
		'focus-opacity': 0.12,
		'selected-opacity': 0.08,
		'activated-opacity': 0.12,
		'pressed-opacity': 0.12,
		'dragged-opacity': 0.08,
		'theme-kbd': '#FFFFFF',
		'theme-on-kbd': '#000000',
		'theme-code': '#212529',
		'theme-on-code': '#FFFFFF',
	}
};

const myCustomLightTheme = {
	dark: false,
	options: { customProperties: true },
	colors: {
		background: '#FFFFFF',
		surface: '#FFFFFF',
		'surface-bright': '#FFFFFF',
		'surface-light': '#EEEEEE',
		'surface-variant': '#424242',
		'on-surface-variant': '#EEEEEE',
		primary: '#1867C0',
		'primary-darken-1': '#1F5592',
		secondary: '#48A9A6',
		'secondary-darken-1': '#018786',
		error: '#B00020',
		info: '#2196F3',
		success: '#4CAF50',
		warning: '#FB8C00',
	},
	variables: {
		'border-color': '#000000',
		'border-opacity': 0.12,
		'high-emphasis-opacity': 0.87,
		'medium-emphasis-opacity': 0.60,
		'disabled-opacity': 0.38,
		'idle-opacity': 0.04,
		'hover-opacity': 0.04,
		'focus-opacity': 0.12,
		'selected-opacity': 0.08,
		'activated-opacity': 0.12,
		'pressed-opacity': 0.12,
		'dragged-opacity': 0.08,
		'theme-kbd': '#212529',
		'theme-on-kbd': '#FFFFFF',
		'theme-code': '#F5F5F5',
		'theme-on-code': '#000000',
	}
};
export const quasarPlugin = {
	install(app) {
		app.use(Quasar, {
			config: {
				dark: true, // Set this to true to enable the dark theme by default
				brand: {
					primary: myCustomDarkTheme.colors.primary, // Set default primary color
					secondary: myCustomDarkTheme.colors.secondary, // Set default secondary color
				},
			},
			themes: {
				myCustomDarkTheme,
				myCustomLightTheme,
			},
			components
		});
	},
};