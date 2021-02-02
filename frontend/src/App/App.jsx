import React from "react";
import { HelmetProvider } from "react-helmet-async";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import Header from "_components/Header";
import Footer from "_components/Footer";

/* Pages */
import HomePage from "_pages/HomePage";
import NotFoundPage from "_pages/NotFoundPage";

const helmetContext = {};


const App = () => {

  return (
    <HelmetProvider context={helmetContext}>
      <Router>
        
        <Header />

        {/* Routes */}
        <Switch>
          <Route path="/" exact component={HomePage} />
          <Route path="*" component={NotFoundPage} />
        </Switch>

        <Footer />

      </Router>
    </HelmetProvider>
  );
};

export default App;
