<script setup lang="ts">
import { requestDeviceDetails, requestGPUUsageDetails } from '@/modules/devices/requestHandling/deviceRequests';

const getDeviceDetails = async (): void => {
	location.value = await requestDeviceDetails();
};

const getGPUUsageDetails = async (): void => {
	gpu_usage.value = await requestGPUUsageDetails();

};
const isBannerVisible = ref(true);

const dismissBanner = (): void => {
	isBannerVisible.value = false;
};

let location = ref('Fetching data...');
let gpu_usage = ref('Fetching data...');

onMounted(() => {
	getDeviceDetails();
	getGPUUsageDetails();
});
</script>

<template>
	<q-banner v-if="isBannerVisible" class="bg-primary text-white" >
		This is a quick overview of the gpu usage
		<template v-slot:action>
			<q-btn flat color="white" label="Dismiss" @click="dismissBanner " />
		</template>
	</q-banner>
	<v-container class="d-flex flex-column align-center">
	<v-card min-width="75%" class="invisible-border mb-4">
		<v-card-title> Running on device</v-card-title>
		<v-card-text>{{ location }}</v-card-text>
	</v-card>
	<v-card min-width="75%" class="invisible-border mb-4">
		<v-card-title> GPU usage details</v-card-title>
		<v-card-text>{{ gpu_usage }}</v-card-text>
	</v-card>
	</v-container>
</template>

<style scoped lang="scss">

</style>
