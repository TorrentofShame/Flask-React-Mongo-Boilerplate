import checkPropTypes from "check-prop-types";

export const checkProps = (component, expectedProps) => {
  let propsError = checkPropTypes(component.propTypes, expectedProps, "props", component.name);
  return propsError;
};

export const capitalize = str => str[0].toUpperCase() + str.slice(1);

