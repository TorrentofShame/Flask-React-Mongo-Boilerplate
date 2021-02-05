import React from "react";
import { shallow } from "enzyme";
//import { checkProps } from "_utils";

import Footer from "./Footer";

describe("<Footer />", () => {

  describe("Should Render", () => {
    let wrapper;
    beforeEach(() => wrapper = shallow(<Footer />));

    it("Renders as a <div> element", () => {
      expect(wrapper.type()).toEqual("div");
    });

  });

});
