import { createPinia, setActivePinia } from 'pinia';

function setup(): void {
	setActivePinia(createPinia());
}

setup();
