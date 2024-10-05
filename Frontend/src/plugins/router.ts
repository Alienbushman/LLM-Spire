import { createRouter, createWebHashHistory, type RouteRecordRaw } from 'vue-router';

type CustomRouteRecord = RouteRecordRaw & { icon: string };

export const routes: CustomRouteRecord[] = [
	{ path: '/', name: 'LLM', component: () => import('@/modules/llm/LlmPage.vue'), icon: 'mdi-robot' },
	{ path: '/devices', name: 'Devices', component: () => import('@/modules/devices/DeviceUsed.vue'), icon: 'mdi-devices' },
	// if you want to see a bit more about the page
	// { path: '/about', name: 'About', component: () => import('@/modules/about/AboutPage.vue'), icon: 'mdi-information' },
];

export const routerPlugin = createRouter({
	history: createWebHashHistory(),
	routes,
});
