package com.star.service.impl;

import com.star.dao.LoginDAO;
import com.star.entity.Login;
import com.star.service.LoginService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * @Author: zzStar
 * @Date: 11-20-2020 13:26
 */
@Service
@Transactional
public class LoginServiceImpl implements LoginService {

    @Autowired
    private LoginDAO loginDAO;


    @Override
    public Login login(String username, String password) {
        return loginDAO.login(username, password);
    }
}
