package com.masai.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.masai.DTO.GptResponse;
import com.masai.service.CustomBotService;

@RestController()
@RequestMapping("/bot")
@CrossOrigin("*")
public class CustomBotController {

	@Autowired
	private CustomBotService botService;
	
	@GetMapping("/jokes")
	public ResponseEntity<String> jokeGenerator(@RequestParam("prompt") String prompt) {
		String resp = botService.getResponse("Hey gpt give joke that is based on "+prompt);
		return new ResponseEntity<>(resp,HttpStatus.OK);
	}
	
	@GetMapping("/shayari")
	public ResponseEntity<String> shayariGenerator(@RequestParam("prompt") String prompt) {
		String resp = botService.getResponse("Hey gpt give shayari that is based on "+prompt);
		return new ResponseEntity<>(resp,HttpStatus.OK);
	}
	
	@GetMapping("/story")
	public ResponseEntity<String> storyGenerator(@RequestParam("prompt") String prompt) {
		String resp = botService.getResponse("Hey gpt give story that is based on "+prompt);
		return new ResponseEntity<>(resp,HttpStatus.OK);
	}
	
	@GetMapping("/quote")
	public ResponseEntity<String> quoteGenerator(@RequestParam("prompt") String prompt) {
		String resp = botService.getResponse("Hey gpt give quote that is based on "+prompt);
		return new ResponseEntity<>(resp,HttpStatus.OK);
	}
	
}
