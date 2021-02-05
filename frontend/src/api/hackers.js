const sa = require("superagent");

const { handleSuccess, handleError } = require("_utils");

export const newhacker = hacker =>
  sa.post("api/hackers")
    .send(hacker)
    .then(handleSuccess)
    .catch(handleError);

export const gethacker = hackerID =>
  sa.get(`/api/hackers/${hackerID}`)
    .then(handleSuccess)
    .catch(handleError);

export const updatehacker = ({hackerID, hacker}) =>
  sa.put(`/api/hackers/${hackerID}`)
    .send(hacker)
    .then(handleSuccess)
    .catch(handleError);

export const deletehacker = hackerID =>
  sa.delete(`/api/hackers/${hackerID}`)
    .then(handleSuccess)
    .catch(handleError);

export const getAllhackers = () =>
  sa.get("/api/hackers/all")
    .then(handleSuccess)
    .catch(handleError);
