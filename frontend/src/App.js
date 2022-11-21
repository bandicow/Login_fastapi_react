import React, { useEffect, useState } from "react";

import Header from "./components/Header";
import Login from "./components/Login";
// import Table from "./components/Table";

import { useContext } from "react";
import { UserContext } from "./context/UserContext";
import MainPage from "./components/MainPage";

const App = () => {
  const [message, setMessage] = useState("");
  const [token] = useContext(UserContext);

  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("/api", requestOptions);
    const data = await response.json();

    // console.log(data); -> 내가 awesome cool 해둔거옴
    if (!response.ok) {
      console.log("somethong messed up");
    } else {
      setMessage(data.message);
    }
  };

  // 아무것도 안하는 함수? 처음에 한번만 실행
  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    <div>
      <Header title={message} />
      <div>
        <div className="column m-5 is-two_thirds">
          {!token ? (
            <div className="columns">
              <Login />
            </div>
          ) : (
            <MainPage />
          )}
        </div>
      </div>
    </div>
  );
};

export default App;
