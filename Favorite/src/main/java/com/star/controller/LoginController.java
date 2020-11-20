package com.star.controller;

import com.star.entity.Login;
import com.star.service.LoginService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Author: zzStar
 * @Date: 11-20-2020 13:30
 */
@RestController
@RequestMapping("login")
public class LoginController {

    @Autowired
    private LoginService loginService;

    @RequestMapping("login")
    @ResponseBody
    public Login login(@RequestParam String username, @RequestParam String password) {
        return loginService.login(username, password);
    }
}
