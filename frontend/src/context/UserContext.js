// context hooks , redux 역할 , 전체에 토큰인증?

import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import { createContext } from "react";

export const UserContext = createContext();

export const UserProvider = (props) => {
  const [token, setToken] = useState(localStorage.getItem("awesomeToken"));

  // 메인페이지에서 요청할 토큰 정보
  useEffect(() => {
    const fetchUser = async () => {
      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token,
        },
      };

      const response = await fetch("/api/users/main", requestOptions); // 아까 생성한 토큰 키 있는 아이디 가져오기

      // 처음에는 null값이 들어가있는듯 xx

      if (!response.ok) {
        setToken(null);
      }
      localStorage.setItem("awesomeToken", token);
    };
    fetchUser();
  }, [token]); // 토큰이 업데이트 될때마다

  // 여기가 메인이고 토큰값을 props로 하위 컴포넌트에 전달하는 듯
  return (
    <UserContext.Provider value={[token, setToken]}>
      {props.children}
    </UserContext.Provider>
  );
};
