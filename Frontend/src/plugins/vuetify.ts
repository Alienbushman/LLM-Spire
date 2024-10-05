// Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { mdi } from 'vuetify/iconsets/mdi';
import '@mdi/font/css/materialdesignicons.css';
import * as labs from 'vuetify/labs/components';

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides

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
}

export const vuetifyPlugin = createVuetify({
	components: { ...components, ...labs },
	directives,
	icons: {
		defaultSet: 'mdi',
		sets: {
			mdi,
		},
	},
	theme: {
		defaultTheme: 'myCustomDarkTheme',
		themes: {
			myCustomDarkTheme,
			myCustomLightTheme
		},
	},
});
