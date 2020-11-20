package com.star.dao;

import com.star.entity.Login;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

/**
 * @Author: zzStar
 * @Date: 11-20-2020 13:11
 */
@Mapper
@Repository
public interface LoginDAO {

    // 登录
    Login login(@Param("username") String username, @Param("password") String password);
}
