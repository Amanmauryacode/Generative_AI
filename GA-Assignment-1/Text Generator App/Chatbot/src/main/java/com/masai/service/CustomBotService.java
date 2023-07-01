package com.masai.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.masai.DTO.GptRequest;
import com.masai.DTO.GptResponse;

@Service
public class CustomBotService {

	@Value("${openai.model}")
	private String model;
	
	
	@Value("${openai.api.url}")
	private String url;
	
	@Autowired
	private RestTemplate temp;
	
	public String getResponse(String prompt) {
		GptRequest req = new GptRequest(model, prompt);
		GptResponse resp = temp.postForObject(url, req, GptResponse.class);
		return resp.getChoices().get(0).getMessage().getContent();
	}
	
	
}
