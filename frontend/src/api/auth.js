const sa = require("superagent");

const { handleSuccess, handleError } = require("_utils");

export const Login = user =>
  sa.post("/api/auth/login")
    .send(user)
    .then(handleSuccess)
    .catch(handleError);

export const Logout = () =>
  sa.get("/api/auth/logout")
    .then(handleSuccess)
    .catch(handleError);
