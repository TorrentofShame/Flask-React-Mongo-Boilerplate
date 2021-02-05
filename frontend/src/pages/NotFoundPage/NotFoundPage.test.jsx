import React from "react";
import { shallow } from "enzyme";
//import { checkProps } from "_utils";

import NotFoundPage from "./NotFoundPage";

describe("<NotFoundPage />", () => {

  describe("Should Render", () => {
    let wrapper;
    beforeEach(() => wrapper = shallow(<NotFoundPage />));

    it("Renders as a <main> element", () => {
      expect(wrapper.type()).toEqual("main");
    });

  });

});
