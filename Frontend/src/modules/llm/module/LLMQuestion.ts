export class LLMQuestion {
	question: string;
	model: string;
	response: string;

	constructor(request: string, model ="") {
		this.question = request
		this.model = model;
		this.response=""
	}
}