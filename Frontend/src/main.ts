import { createApp } from 'vue';

import App from './App.vue';

import './assets/main.css';
import { piniaPlugin } from './plugins/pinia';
import { vuetifyPlugin } from './plugins/vuetify';
import { routerPlugin } from './plugins/router';
import { quasarPlugin } from '@/plugins/quasar';

const app = createApp(App);

app.use(piniaPlugin);
app.use(vuetifyPlugin);
app.use(routerPlugin);
app.use(quasarPlugin);

app.mount('#app');
