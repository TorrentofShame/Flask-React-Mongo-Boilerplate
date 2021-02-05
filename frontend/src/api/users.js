const sa = require("superagent");

const { handleSuccess, handleError } = require("_utils");

export const newUser = user =>
  sa.post("api/users")
    .send(user)
    .then(handleSuccess)
    .catch(handleError);

export const getUser = username =>
  sa.get(`/api/users/${username}`)
    .then(handleSuccess)
    .catch(handleError);

export const updateUser = ({username, user}) =>
  sa.put(`/api/users/${username}`)
	.send(user)
    .then(handleSuccess)
    .catch(handleError);

export const deleteUser = username =>
  sa.delete(`/api/users/${username}`)
    .then(handleSuccess)
    .catch(handleError);

export const getAllUsers = () =>
  sa.get("/api/users/all")
    .then(handleSuccess)
    .catch(handleError);
