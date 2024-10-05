import axios from 'axios';

export async function requestDeviceDetails(): Promise<string> {
	const apiUrl = 'http://127.0.0.1:8000/api/running-device/';
	try {
		const res = await axios.get(apiUrl);
		return res.data;
	} catch (error) {
		return "Error " + error;
	}
}

export async function requestGPUUsageDetails(): Promise<string> {
	const apiUrl = 'http://127.0.0.1:8000/api/device-usage/';

	try {
		const res = await axios.get(apiUrl);
		return res.data;
	} catch (error) {
		return "Error " + error;
	}
}