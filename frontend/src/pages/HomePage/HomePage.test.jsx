import React from "react";
import { shallow } from "enzyme";
//import { checkProps } from "_utils";

import HomePage from "./HomePage";

describe("<HomePage />", () => {

  describe("Should Render", () => {
    let wrapper;
    beforeEach(() => wrapper = shallow(<HomePage />));

    it("Renders as a <main> element", () => {
      expect(wrapper.type()).toEqual("main");
    });

  });

});
