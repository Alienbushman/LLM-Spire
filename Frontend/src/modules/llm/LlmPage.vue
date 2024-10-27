<script setup lang='ts'>
import PromptSelection from '@/modules/llm/components/PromptSelection.vue';
import { useLLMStore } from '@/modules/llm/stores/llmStore';

const llmStore = useLLMStore();

let question = ref(useLLMStore().getLLMRequest.question);
let response = ref<String>(useLLMStore().getLLMRequest.response);

watch(
	() => llmStore.getLLMRequest.response,
	(newResponse) => {
		response.value = newResponse;
	}
);

const questionType = ref('');
const techStack = ref('');
const model = ref('');

const handleQuestionTypeChange = (newValue: string) => {
	questionType.value = newValue;
};

const handleTechStackChange = (newValue: string) => {
	techStack.value = newValue;
};

const handleModelChange = (newValue: string) => {
	model.value = newValue;
};

function submitQuestion(): void {
	llmStore.requestLLMResponse(question.value, model.value);
}

const loadingQuestion = computed(() => useLLMStore().loading);

</script>

<template>
	<v-container justify-center >
		<v-card>
			<v-card-title class="headline text-center">Welcome to the local LLM</v-card-title>
			<v-card-text v-if="model !== 'gpt4-mini'">
				<p class="text-center">
					This is running 100% locally
				</p>
			</v-card-text>
			<v-card-text v-else>
				<p class="text-center" style="color: red">
					Warning currently using online gpt as the model
				</p>
			</v-card-text>
		</v-card>
	</v-container>

	<prompt-selection
		@update:questionType="handleQuestionTypeChange"
		@update:techStack="handleTechStackChange"
		@update:model="handleModelChange"
	/>
	<v-container >
		<v-row>
			<v-textarea v-model='question' auto-grow label='Question' rows='10'
			/>
		</v-row>
		<v-row justify='end'>
			<v-btn @click='submitQuestion'>Submit</v-btn>
		</v-row>
		<v-row style='height: 20px;'></v-row>
		<v-row>
			<v-textarea :disabled='response==""||loadingQuestion' auto-grow label='Answer' :model-value='response'
						:loading="loadingQuestion" />
		</v-row>
	</v-container>
</template>

<style scoped>


</style>
