import React from "react";
import { shallow } from "enzyme";
//import { checkProps } from "_utils";

import Header from "./Header";

describe("<Header />", () => {

  describe("Should Render", () => {
    let wrapper;
    beforeEach(() => wrapper = shallow(<Header />));

    it("Renders as a <div> element", () => {
      expect(wrapper.type()).toEqual("div");
    });

  });

});
