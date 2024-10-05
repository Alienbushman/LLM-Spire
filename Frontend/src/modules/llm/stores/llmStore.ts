import { defineStore, acceptHMRUpdate } from 'pinia';
import { LLMQuestion } from '@/modules/llm/module/LLMQuestion';
import { LLMQuestionRequest } from '@/modules/llm/requestHandling/llmRequest';

export const useLLMStore = defineStore('LLM', {
	state: () => ({
		llmRequest: new LLMQuestion('', ''),
		loading: false
	}),
	getters: {
		getLLMRequest: (state) => state.llmRequest
	},
	actions: {
		async requestLLMResponse(question: string, model: string): Promise<void> {

			this.loading = true;
			this.llmRequest.question = question;
			this.llmRequest.model = model;

			LLMQuestionRequest(question, model)
				.then(response => {
					console.log('LLM Response:', response);
					this.llmRequest.response = response;

				})
				.catch(error => {
					console.error('Error fetching LLM response:', error);
					this.llmRequest.response = error;
				}).finally(() => {
				this.loading = false;
			});
		}
	}
});


if (import.meta.hot) {
	import.meta.hot.accept(acceptHMRUpdate(useLLMStore, import.meta.hot));
}