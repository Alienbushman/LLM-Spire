<script setup lang='ts'>

import { useTheme } from 'vuetify';
import { useQuasar } from 'quasar';

const theme = useTheme();

const isLightTheme = ref(theme.global.name.value === 'myCustomLightTheme');

const $q = useQuasar();

watch(isLightTheme, (newValue: boolean) => {
	const themeName = newValue ? 'myCustomLightTheme' : 'myCustomDarkTheme';
	theme.global.name.value = themeName;
	// todo investigate how to set the custom dark mode in quasar
	$q.dark.set(!newValue)
});


</script>

<template>
	<div class="d-flex justify-end">
		<v-switch
			class="pt-5 pr-3 "
			v-model="isLightTheme"
			color='primary'
			true-icon='mdi-weather-sunny'
			false-icon='mdi-weather-night'
			inset
		/>
	</div>
</template>

<style scoped lang='scss'>

</style>
