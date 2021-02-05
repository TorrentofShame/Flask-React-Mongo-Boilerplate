import checkPropTypes from "check-prop-types";

export const checkProps = (component, expectedProps) => {
  let propsError = checkPropTypes(component.propTypes, expectedProps, "props", component.name);
  return propsError;
};

export const capitalize = str => str[0].toUpperCase() + str.slice(1);


/* API Utils */
export const handleSuccess = res => res.body;

export const handleError = err => {
  if (err.response) { throw err.response; }
  else {
    const res = { status: 500, body: { message: "Internal Server Error" } };
    throw res;
  }
};
