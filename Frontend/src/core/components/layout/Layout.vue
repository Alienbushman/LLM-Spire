<script setup lang='ts'>

import { routes } from '@/plugins/router';
import ThemeButton from '@/core/components/layout/ThemeButton.vue';


</script>

<template>

	<v-app-bar density='compact' elevation='1'>
		<v-toolbar-title> Local LLM</v-toolbar-title>
		<v-spacer></v-spacer>
		<theme-button />
	</v-app-bar>
	<v-navigation-drawer app width="140" >
		<v-list>
			<v-list-item
				v-for="route in routes"
				:key="route.name"
				:to="route.path"
				router
			>
				<v-list-item-title>{{ route.name }}</v-list-item-title>
			</v-list-item>
		</v-list>
	</v-navigation-drawer>

</template>


