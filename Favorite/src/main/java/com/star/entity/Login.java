package com.star.entity;

import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.Accessors;

import java.util.Date;

/**
 * @Author: zzStar
 * @Date: 11-20-2020 13:06
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Accessors(chain = true)
public class Login {

    private String id;
    private String username;
    private String password;
    private boolean role;

    @JsonFormat(pattern = "yyyy-MM-dd", timezone = "GTM+8")
    private Date ctime;
}
