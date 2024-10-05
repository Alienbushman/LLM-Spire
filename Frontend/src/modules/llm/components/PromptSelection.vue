<script setup lang='ts'>

const emit = defineEmits(['update:questionType', 'update:techStack', 'update:model']);

const questionTypeSelected = ref('coding');
const techStackSelected = ref('vue');
const modelSelected = ref('gpt3');

const questionTypeItems = ['text', 'coding'];
const techStackItems = ['vue', 'java', 'python'];
const modelItems = ['gpt3', 't5-small', 'gpt2', 'mia', 'gpt-neo-2.7B', 'gpt-j-6b', 'experimental'];

watch(
	questionTypeSelected,
	(newValue) => {
		emit('update:questionType', newValue);
	},
	{ immediate: true }
);

watch(
	techStackSelected,
	(newValue) => {
		emit('update:techStack', newValue);
	},
	{ immediate: true }
);

watch(
	modelSelected,
	(newValue) => {
		emit('update:model', newValue);
	},
	{ immediate: true }
);
</script>

<template>
	<v-container>
		<v-row>
			<v-col cols='12' sm='4'>
				<v-select
					v-model='questionTypeSelected'
					:items='questionTypeItems'
					label='Coding or text'
				></v-select>
			</v-col>

			<v-col cols='12' sm='4'>
				<v-select
					v-model='techStackSelected'
					:disabled='questionTypeSelected!="coding"'
					:items='techStackItems'
					label='Tech stack'
				></v-select>
			</v-col>

			<v-col cols='12' sm='4'>
				<v-select
					v-model='modelSelected'
					:items='modelItems'
					label='Model'
				></v-select>
			</v-col>
		</v-row>
	</v-container>
</template>

<style scoped lang='scss'>

</style>
