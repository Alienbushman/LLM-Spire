import axios from 'axios';

export async function LLMQuestionRequest(question: string, model: string): Promise<string> {
	const apiUrl = 'http://127.0.0.1:8000/api/llm-opinion/';

	const postData = {
		model: model,
		question: question
	};

	const startTime = performance.now();

	try {
		const res = await axios.post(apiUrl, postData);
		const endTime = performance.now();
		const duration = ((endTime - startTime) / 1000).toFixed(4);
		console.log('Request for:', question, model);
		console.log(`Request took ${duration} seconds.`);
		return res.data.message;
	} catch (error) {
		console.error('Error in LLMQuestionRequest:', error);
		return 'Error ' + error;
	}
}