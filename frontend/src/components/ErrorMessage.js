// 다른 곳에서 에러 메세지를 받아와서 그 것을 div안에 띄워주기
// <ErrorMessage message={errorMessage(여기로 보낼 메세지 적기)} /> 로 사용

import React from "react";

const ErrorMessage = ({ message }) => (
  <p className="has-text-weight-bold has-text-danger">{message}</p>
);

export default ErrorMessage;
